#-*- coding: UTF-8 -*-
# kMeans算法测试

from numpy import *
import kMeans
  
print("loading data...")
dataSet = mat(kMeans.loadDataSet('testSetForKMeans.txt'))

k = 4
centroids, clusterAssment = kMeans.kMeans(dataSet, k)  

print("show the result...")
kMeans.showCluster(dataSet, k, centroids, clusterAssment) 