#!/usr/bin/env python

"""
Clean version of clustering gene expression data
"""


import numpy as np
import sys
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.cluster.vq import vq, kmeans2
from matplotlib import pyplot as plt

# 1) Load data into matrix
d = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,7))  
m = np.matrix(d)

Z = linkage(m, 'average') #calculate linkage distances
#m_order = leaves_list(Z) #Z leaves of histogram (~500)


# 2) Transpose to create cell type dendrogram
# n = np.transpose(m) #transpose m for cells
# Z_tr = linkage(n, 'average') 
# plt.figure()
# cells = dendrogram(Z_tr)
# plt.savefig('01-dendrogram.png')
# plt.show()

# # 3) Cluster heatmap by both genes and cell types
# idx1 = genes['leaves']
# idx2 = cells['leaves']
# m = m[idx1,:]
# m = m[:, idx2]
# # plt.show()
# plt.figure()
# im = plt.matshow(m, aspect='auto', origin='lower')
# plt.colorbar(im)
# plt.savefig('01-cluster_both_2low.png')
# plt.show()


#4) Cluster by k-means 
x = np.array(m[:, 0]) #cfc
y = np.array(m[:, 1]) #poly

#kmeans2
centroid, label = kmeans2(m, 2)
color1 = np.array(["red", "black"])
plt.scatter(x, y, c=color1[label])
plt.ylim(-0.15,20) 
plt.xlim(-0.05,16) 
plt.savefig("02-kmeans_k2.png")
plt.show()
