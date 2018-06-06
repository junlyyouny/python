# -*- coding: UTF-8 -*-
# 1.先确定常数K，常数K意味着最终的聚类类别数
# 2.随机选定初始点为质心
# 3.计算每一个样本与质心之间的相似度(这里为欧几里得距离)
# 4.将样本点归到最相似的类中,重新计算每个类的质心(即为类中心)
# 5.重复整个过程，直到质心不再改变

from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(fileName):
    """读取tab分割的浮点数文件内容"""
    # assume last column is target value
    # 假定上一列是目标值
    dataMat = []
    fr = open(fileName, 'r')
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        # map all elements to float()
        fltLine = map(float, curLine)
        # python3 用list转换，python2去掉list
        dataMat.append(list(fltLine))
    return dataMat


def distEclud(vecA, vecB):
    """欧几里得距离"""
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    """生成初始点"""
    n = dataSet.shape[1]
    # create centroid mat
    # 创建质心垫
    centroids = mat(zeros((k, n)))
    # create random cluster centers, within bounds of each dimension
    # 创建随机聚类中心，在每一个维度的界限
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    """
    kMeans算法实现
    dataSet样本点,k 簇的个数
    disMeas距离量度，默认为欧几里得距离
    createCent,初始点的选取
    """
    # 样本数
    m = dataSet.shape[0]
    # m*2的矩阵
    clusterAssment = mat(zeros((m, 2)))
    # 初始化k个中心
    centroids = createCent(dataSet, k)
    clusterChanged = True
    # 当聚类不再变化
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            # 找到最近的质心
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            # 第1列为所属质心，第2列为距离
            clusterAssment[i, :] = minIndex, minDist ** 2
        print(centroids)

        # 更改质心位置
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


def showCluster(dataSet, k, centroids, clusterAssment):
    """展示结果"""
    numSamples, dim = dataSet.shape
    if dim != 2:
        print("Sorry! I can not draw because the dimension of your data is not 2!")
        return 1
    # 设定普通点颜色形状
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("Sorry! Your k is too large!")
        return 1

    # # 画出所有样例点 属于同一分类的绘制同样的颜色
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    # 设定质心颜色形状
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']

    # 画出质心
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()
