#!/usr/bin/env python

"""
Calculate how many SNPs per allelic freq bin
Input: Use vcf (optional columns contains strain info)
Output: plot of {# of sNPs} vs {allelic freq}
"""

import sys
import matplotlib.pyplot as plt
from collections import Counter

#read vcf file line by line
vcf = open(sys.argv[1])
# count number of strains that have "1" on each line
freq_SNP = []
for line in vcf.readlines():
    if line.startswith("#"):
        continue
    data = line.rstrip("\r\n").split("\t")[9:]
    row = [int(x) for x in data]
    freq = (sum(row)/float(len(row)))
    freq_SNP.append(freq)
print freq_SNP
#this should append freq per SNP into array
plt.hist(freq_SNP)
plt.xlabel('Allelic Frequency')
plt.ylabel('# of SNPs')
plt.title('SNP Frequency over Yeast Strains')
plt.savefig('02-SNP_hist.png')
plt.close()
##use Counter to count how many times each SNP freq appears in freq_array, and output number of SNPs appears
## parse Counter output "for x, y in counter output"

