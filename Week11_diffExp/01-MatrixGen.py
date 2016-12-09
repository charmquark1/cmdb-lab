#!/usr/bin/env python

"""
Convert my table to a numpy matrix

"""

import numpy as np
import sys
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage, leaves_list
from matplotlib import pyplot as plt

# 1) Calc pair-wise linkage
###500 genes, 124,750 possible pair-wise
d = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,7))  
m = np.matrix(d)
print m.dtype
#print m, m.shape

Z = linkage(m, 'average')#euclidean is default
#4 columns output-- 3rd is linkage distance, 4th is numb of genes in cluster. 
#m_order = leaves_list(Z)#reorder rows to make leaves
#print Z, Z.shape
#print m_order, m_order.shape


### 2) Transpose to create cell type dendrogram
#m_transp = np.transpose(m)
# labels = d.columns[1:]
# print labels

#3) test
# Z = linkage(m, 'average')
# plt.figure()

# genes = dendrogram(Z, orientation='right')
n = np.transpose(m) #transpose m for cells
Z_cells = linkage(n, 'average')
plt.figure()
cells = dendrogram(Z_cells)
plt.savefig('01-dendrogram.png')
plt.show()

#this code makes a heatmap gridspec
idx1 = genes['leaves']
idx2 = cells['leaves']
m = m[idx1,:]
m = m[:, idx2]
# plt.show()
plt.figure()
im = plt.matshow(m, aspect='auto', origin='lower')
plt.colorbar(im)
plt.savefig('01-cluster_both_2low.png')
plt.show()

#plot 
x_= np.array(m[]) #cfc
y = np.array() #poly
plt.scatter

#kmeans 
kmeans2 

