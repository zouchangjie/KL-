# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats
import pandas as pd

off_train = pd.read_csv('dataset/data_number1.csv', header=None)
file1 = open('dataset/data_KL_query.csv','w')
points1 = []

for col in range(len(off_train)):

    points1.append([off_train.iloc[col][0],off_train.iloc[col][1],off_train.iloc[col][2]])
points2 = np.array(points1, dtype=float)


y = []
for i in range(len(points2)):
    file1.write(str(i+1)+' ')
file1.write('\n')
for i in range(len(points2)):
    x = []
    for j in range(len(points2)):
        distance = scipy.stats.entropy(points2[i], points2[j])
        x.append(distance)
        file1.write(str(x[j])+' ')
    file1.write('\n')
file1.close()


print 11
print 11


# for i in range(len(x)):
#     KL += x[i] * np.log(x[i] / y[i])
#
# print(KL)