#!/usr/bin/env python
import numpy as np
import os
import sys
import pylab
import scipy
import scipy.cluster.hierarchy as sch
from scipy.stats import ttest_rel

data = open(sys.argv[1])

earl1=[]
earl2=[]
late1=[]
late2=[]
#calculate mean between early 2 per gene

#calculate mean between late2 per gene

labels = []
avg_e = []
avg_l = []
for i in data.readlines()[1:]:
	labels.append(i.rstrip('\n').split()[0])
	earl1.append(float(i.rstrip('\n').split()[1]))
	late1.append(float(i.rstrip('\n').split()[2]))
	earl2.append(float(i.rstrip('\n').split()[5]))
	late2.append(float(i.rstrip('\n').split()[3]))
print earl1[0], earl2[0]

#now watch me zip
#calculate avg for early 2
for i, j in zip(earl1, earl2):
	avg = float((i+j)/2)
	avg_e.append(avg)

#calculate averages for each
for x, y in zip(late1, late2):
	avg = float((x+y)/2)
	avg_l.append(avg)
#Calculate ratios between averages
diff_val = []
diff_genes = []
for x, y, g in zip(avg_e, avg_l, labels):
	ratio = float(y/x)
	if ratio>2:
		diff_val.append(ratio)	
		diff_genes.append(g)	
#print len(diff_val), len(diff_genes)

#is avg change in intensity among the two groups >2-fold?


f = open('03_listofGenes.txt', 'w')
f.write("#ttest between late and early programs")
t, pair = ttest_rel(avg_l, avg_e)
f.write("\n")
f.write("#ttest p value: "+str(pair))
f.write("\n")
f.write("#gene, fold_change")
f.write("\n")
for i, j in zip(diff_genes, diff_val):
	f.write(str(i)+"\t"+str(j))
	f.write("\n")

#how do i use ttest_rel on individual genes??
##I used ttest on early and late sets and found they were significantly different, but don't know how to use them to determine individual DE genes. 
