#-*- coding: UTF-8 -*-

from numpy import *
import matplotlib.pyplot as plt

#读取tab分割的浮点数文件内容
def loadDataSet(fileName): 
    #assume last column is target value
    #假定上一列是目标值
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        #map all elements to float()
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

# 欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

# 生成初始点
def randCent(dataSet, k):
    n = dataSet.shape[1]
    #create centroid mat
    #创建质心垫
    centroids = mat(zeros((k,n)))
    #create random cluster centers, within bounds of each dimension
    #创建随机聚类中心，在每一个维度的界限
    for j in range(n):
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

# dataSet样本点,k 簇的个数
# disMeas距离量度，默认为欧几里得距离
# createCent,初始点的选取
def kMeans(dataSet, k, distMeas = distEclud, createCent = randCent):
    m = dataSet.shape[0] #样本数
    clusterAssment = mat(zeros((m,2))) #m*2的矩阵
    centroids = createCent(dataSet, k) #初始化k个中心
    clusterChanged = True             
    while clusterChanged:      #当聚类不再变化
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k): #找到最近的质心
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            # 第1列为所属质心，第2列为距离
            clusterAssment[i,:] = minIndex,minDist**2
        print centroids

        # 更改质心位置
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis = 0) 
    return centroids, clusterAssment

def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print("Sorry! I can not draw because the dimension of your data is not 2!")
        return 1
    #设定普通点颜色形状    
    mark = ['or','ob','og','ok','^r','+r','sr','dr','<r','pr']
    if k > len(mark):
        print("Sorry! Your k is too large!")
        return 1
     
    ## 画出所有样例点 属于同一分类的绘制同样的颜色   
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    
    #设定质心颜色形状   
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    
    #画出质心
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
    
    plt.show()