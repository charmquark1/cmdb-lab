#!/usr/bin/env python

"""
Make PCA plot from plink2 --pca output (eigenvectors)
"""

import sys
import matplotlib.pyplot as plt

evector = open(sys.argv[1])

#Convert columns into x and y arrays
x_vect = []
y_vect = []
#
for line in evector.readlines():
	field = line.rstrip("\r\n").split()
	x_vect.append(field[2])
	y_vect.append(field[3])

x_map = map(float, x_vect)
y_map = map(float, y_vect)

plt.scatter(x_map, y_map)
plt.ylabel('PCA 2')
plt.xlabel('PCA 1')
plt.title('Genetic Diversity among Yeast Strains')
plt.savefig("01-PCA_plot.png")
plt.close()
