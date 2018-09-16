# -*- coding: utf-8 -*-


from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
# from sklearn.cluster import kmedoids
import kmedoids
import pandas as pd
#用kmeans对179 X 3 数据矩阵聚类 聚成三类

data = pd.read_csv('dataset/result_data1.csv', header=None)

# result = open('dataset/result_data1_label.csv', 'w')
result1 = open('dataset/result_data1_labe2.csv', 'w')
points1 = []
for col in range(len(data)):
    points1.append([data.iloc[col][0],data.iloc[col][1],data.iloc[col][2]])
points2 = np.array(points1, dtype=float)



# 3 points in dataset
data = np.array([[1,1],
                [2,2],
                [10,10]])

# distance matrix
D = pairwise_distances(points2, metric='euclidean')

# split into 2 clusters
M, C = kmedoids.kMedoids(D, 3)

# print('medoids:')
# for point_idx in M:
#     print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, points2[point_idx]))
        a = ('{0}'.format(label))
        result1.write(str(points2[point_idx][0])+','+str(points2[point_idx][1])+','+str(points2[point_idx][2])+','+a+'\n')
        print a

result1.close()
# data_zs = 1.0*(data - data.mean())/data.std()
# model = KMeans(n_clusters=3, max_iter=400)
#
# model.fit(data_zs) #开始聚类
# x4 = model.labels_
# for i in range(len(points2)):
#     result.write(str(points2[i][0]) + ','+str(points2[i][1])+ ','+str(points2[i][2]) + ','+str(x4[i]) + '\n')
#
#
# #集群中心的坐标
# centers = model.cluster_centers_

#简单打印结果

##########################
# data1 = whiten(points2)
# # <type 'list'>: [-0.2125087921160807, -0.25536825591337592, -0.096051996670675613]
# # [ 2.403673    2.95287384  0.22865139]
# # [  3.81620168   3.74840226  12.87611141]
# centroid = kmeans(data1,3)[0]
# # codebook , distortio=kmeans(data1,3)
# # codebook ， distortio
# label=vq(data1,centroid)[0]
#
# for i in range(len(points2)):
#     result1.write(str(points2[i][0]) + ','+str(points2[i][1])+ ','+str(points2[i][2]) + ','+str(label[i]) + '\n')
#
# print label

