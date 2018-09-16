# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:37:21 2015

@author: Eddy_zheng
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#对三类聚类结果可视化，看成三维的图

data = pd.read_csv('dataset/result_data1_labe2.csv', header=None)
points1 = []
x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []
x3 = []
y3 = []
z3 = []
for col in range(len(data)):
    if data.iloc[col][3] == 0:
        x1.append([data.iloc[col][0]])
        y1.append([data.iloc[col][1]])
        z1.append([data.iloc[col][2]])
    elif data.iloc[col][3] == 1:
        x2.append([data.iloc[col][0]])
        y2.append([data.iloc[col][1]])
        z2.append([data.iloc[col][2]])
    elif data.iloc[col][3] == 2:
        x3.append([data.iloc[col][0]])
        y3.append([data.iloc[col][1]])
        z3.append([data.iloc[col][2]])

ax = plt.subplot(111,projection='3d') #创建一个三维的绘图工程


#将数据点分成三部分画，在颜色上有区分度
ax.scatter(x1,y1,z1,c='y') #绘制数据点
ax.scatter(x2,y2,z2,c='r')
ax.scatter(x3,y3,z3,c='g')

ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.savefig("picture_2.png")
plt.show()


points3 = []
train_yi = pd.read_csv('dataset/data_yi.csv', header=None)
for col in range(len(train_yi)):

    points3.append([train_yi.iloc[col][0],train_yi.iloc[col][1]])
points4 = np.array(points3, dtype=float)

row_number = pd.read_csv('dataset/row_number.csv', header=None)
x = 0
for i in range(len(row_number)):
    print i
    if data.iloc[i][3] == 0 :
        for j in range(1,row_number.iloc[i]+1):

            y = points4[x][1]
            plt.scatter(x, y,s = 2, c='b')
            x = x + 1
        # plt.show()
    elif data.iloc[i][3] == 1 :
        for j in range(1,row_number.iloc[i]+1):

            y = points4[x][1]
            plt.scatter(x, y,s = 2, c='r')
            x = x + 1
        # plt.show()
    elif data.iloc[i][3] == 2 :
        for j in range(1,row_number.iloc[i]+1):

            y = points4[x][1]
            plt.scatter(x, y,s = 2, c='darkcyan')
            x = x + 1
plt.savefig("picture_1.png")
plt.show()



