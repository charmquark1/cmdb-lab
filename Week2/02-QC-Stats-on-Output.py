#!/usr/bin/env python
"""
Goal: For assembly output, compute: 1) min, max, avg contig length, 2) the length of the N50 contig

Input: xxx.py <contigs.fa> 
Output: See print comment in this script. 

"""

import sys, fasta_fixed

input_s = (sys.argv[1])
input_o = open(input_s)

c_lengths = []

#Parse file for length and append to list
for n, seq in fasta_fixed.FASTAReader(input_o):
    field = n.rstrip("\r\n").split("_")
    length = int(field[3])
    c_lengths.append(length)

c_lengths.sort()

mini = c_lengths[0]
maxi = c_lengths[-1]
count = len(c_lengths)
sigma_all = 0 #sum of all elements in list
for i in c_lengths:
    sigma_all = sigma_all + i

index_all = len(c_lengths) #length of list
avg = sigma_all /index_all

#Calculate the length of the N50 contig:
#50% of contigs are longer than or equal to ___.
## organize your contigs, divide sigma by 2. Sum until reached sigma/2. Then return length of that index in the list.
sigma_two = sigma_all/2
N_sum = 0
n_50 = None
for i in range(0, len(c_lengths)):
	if N_sum <= sigma_two:
		N_sum = N_sum + c_lengths[i]
	else:
                N_50_index = i
                n_50 = c_lengths[i]
	#else: 
	#	print "Error: Some stats cannot be determined for input."
	#	break

# #Print stats:
print "Stats For", input_s, ": "
print " "
print "Number of Contigs:", count
print "Lengths (min, max, avg, N50): ", mini, ", ", maxi, ", ", avg, ", ", n_50
if n_50 == None:
    print "error: N50 cannot be determined. Bad comparison"
elif n_50 <= avg:
    print "N50 is less than the Average."
elif n_50 >= avg:
    print "N50 is greater than the Average."
elif n_50 == avg:
    print "N50 and Avg are equal"

