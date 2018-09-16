# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import date
from  sklearn.cluster  import  KMeans
#对数据每行用kmeans进行聚类 为三类


# off_train = pd.read_csv('dataset/data.csv', header=None)
off_train1 = open('dataset/data.csv','r')
result1 = open('dataset/result_data1.csv','w')

for i in off_train1:
    x = []
    i = i.split(',')
    j = 0

    while( i[j] and j<1186 ):
      x.append([i[j]])
      j = j + 1
    x_np = np.array(x, dtype=int)
    model = KMeans(n_clusters=3)
    model.fit(x_np)
    x_label = model.labels_
    centers = model.cluster_centers_
    # centers.sort(reverse=True)
    a = sorted([centers[0][0],centers[1][0],centers[2][0]])
    result1.write(str(a[2]) + ',' + str(a[1]) + ',' + str(a[0]) + '\n')
    # result1.write(str(centers[0][0]) + ',' + str(centers[1][0]) + ',' + str(centers[2][0]) + '\n')

result1.close()
print 11



