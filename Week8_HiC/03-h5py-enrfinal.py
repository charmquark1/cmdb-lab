#!/usr/bin/env python
"""
access h5py file
calculate enrichment
extract enriched positions from positions matrix
"""
import h5py
import sys
import numpy as np

file = h5py.File("02-Out_enr.heat")

counts = file['0.counts'][...]
exp= file['0.expected'][...]
positions = file['0.positions'][...]

#1) calculate enrichment for each set of numbers
##calculate from counts/exp
#tell it to ignore 0!!!
# res = np.empty((counts.shape))
# log_all = counts[(np.where(counts>0))]/exp[(np.where(counts>0))]
#
# res[np.where(counts>0)]=log_all
# print res

enrich = counts/exp
log_all=(np.log(enrich))
new_pos = []
count_i = 0
count_j = 0

#2) find positions of enrichment
for i in (log_all):
	count_i+=1
	for j in (log_all[count_i-1]):
		count_j+=1
		if j > 2:
			new_pos.append([count_i,count_j,j])

#3) Find coordinates of enrichment peaks
x_coord = []
y_coord = []
## iterate through positions
for p in positions:
	x = p[0]
	#x=p.split(",")[0]
	y =p[1]
	x_coord.append(x)
	y_coord.append(y)
#print len(x_coord)
#print len(y_coord)

## Split enriched position to counts and append as coords
final_pos = []
for n in new_pos:
	# t +=1
	# if t==6:
	# 	break
	first= n[0]
	sec = n[1]
	if sec>len(y_coord):
		continue
	y = y_coord[sec] 
	x= x_coord[first] 
	final_pos.append([x,y])
print final_pos
