#!/usr/bin/env python

"""
access h5py file
calculate enrichment

"""

import h5py
import numpy as np

file = h5py.File("02-Out_enr.heat")
counts = file['0.counts'][...]
exp = file['0.expected'][...]

#tell it to ignore 0!!!
res = np.empty((counts.shape))
logratiolist=[]
for i in range(0,459):
	for j in range(0,459):
		if counts[i,j]==0:
			continue
		else:
			logratio = np.log(counts[i,j])-np.log(exp[i,j])
			logratiolist.append(logratio)
print len(logratiolist)
			#log_all = counts[(np.where(counts>0))]/exp[(np.where(counts>0))]
			
#res[np.where(counts>0)]=log_all
#print res


# Calculate where peaks print 
#How to explain this:
#pulling it out of harddrive to memory, analgous to readlines
#h5py is a library. 


#compare all my fragments through my CTCF file, then find the strngest binding. then save it here-- save 
#the region of chrom that strongly interacts with CTCF. 
