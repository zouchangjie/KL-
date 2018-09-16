from  sklearn.cluster  import  KMeans
import  numpy  as  np
import scipy.cluster.hierarchy as sch
# x = [[1,2],[2,2],[3,2],[1,2],[6,2],[8,2]]
# x = [[1,2],[1,2],[1,2]]
# x = [[1],[2],[3],[4]]
x = [[68684.0,22004.5,2.0],
[58872.0, 223.0, 2.0],
[254538.0, 100303.0, 43778.0],
[58872.0, 266.0, 2.0],
[19820.0, 2944.0, 18.5]]
disMat = sch.distance.pdist(x,'euclidean')
print 88
# x = [[1],[2],[3],[1],[6],[8]]
# model = KMeans(n_clusters=2)
#
# model.fit(x)
# x54 = model.labels_
# x1 = model.inertia_
# x2 = model.labels_
#
# x3 = model.cluster_centers_
#
# x4 = model.labels_