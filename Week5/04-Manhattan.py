#!/usr/bin/env python

"""
Goal: Make Manhattan plot ( {-log p val} vs. {chr region})
Input: Output from plink2 -assoc (GWAS.P1.qassoc) 
Output: graph 
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# iterate through all GWAS files
##read P column
for f in sys.argv[1:]:
	df = pd.read_table(f, delim_whitespace = True)
	dP = df['P']

#define x = SNP, y = p val
	y_val = np.array(-1*np.log10(dP))
	x_val = range(len(dP.index))
#define thresh

	limit = -np.log10(10**-5)
	colors = ['yellow' if y_val[i] > limit else 'blue' for i in range(len(y_val))]

#plot x and y values, with diff color on those that reach threshold
	
	field = f.split(".")
	trait = field[1]
	plt.figure()
	plt.scatter(x_val, y_val, color=colors)
	plt.ylim([-0.555552,25])
	plt.title("Genome-wide Association with Trait " +trait)
	plt.xlabel("Chr position")
	plt.ylabel("-log10(p)")
	plt.savefig(f+".png")
