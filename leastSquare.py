# _*_ coding: utf-8 _*_
# 运行环境: python3
# 通过最小化误差的平方和寻找数据的最佳函数匹配
# 最终求得的数据与实际数据之间误差的平方和最小

# 科学计算库
import numpy as np
# 在numpy基础上实现的部分算法库
import pylab as pl
# 引入最小二乘函数
from scipy.optimize import leastsq

# 多项式次数
n = 9


def real_func(x):
    """目标函数"""
    return np.sin(2 * np.pi * x)


def fit_func(p, x):
    """多项式函数"""
    f = np.poly1d(p)
    return f(x)


# 正则化系数lambda
# regularization = 0.1

def residuals_func(p, y, x):
    """残差函数"""
    ret = fit_func(p, x) - y
    # 将lambda^(1/2)p加在了返回的array的后面 
    # ret = np.append(ret, np.sqrt(regularization) * p)
    return ret


# 随机选择9个点作为x
x = np.linspace(0, 1, 9)
# 画图时需要的连续点
x_points = np.linspace(0, 1, 1000)

# 目标函数
y0 = real_func(x)
# 添加正太分布噪声后的函数
y1 = [np.random.normal(0, 0.1) + y for y in y0]

# 随机初始化多项式参数
p_init = np.random.randn(n)

plsq = leastsq(residuals_func, p_init, args=(y1, x))

# 输出拟合参数
print('Fitting Parameters: ', plsq[0])

pl.plot(x_points, real_func(x_points), label='real')
pl.plot(x_points, fit_func(plsq[0], x_points), label='fitted curve')
pl.plot(x, y1, 'bo', label='with noise')
pl.legend()
pl.show()
