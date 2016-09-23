#!/usr/bin/env python

"""
Parse amino acid sequence in FASTA file. 
Convert amino acid to 3 nucleotide seq, append to variable 'new'
When you see a -, replace with ---
Print gene id (ident), converted seq, new line \n, print new seq
Usage: xxx.py 04-AA.fa 02-nt.fa
"""

import fasta_fixed
import sys
import itertools

#inputs: 1) amino acid FASTA, 2) original nt FASTA

AA_query = open(sys.argv[1])
nt_query = open(sys.argv[2])

#prepare inputs for parallel parsing
AA_seq = []
nt_seq = []

for ident, sequence in fasta_fixed.FASTAReader(AA_query):
    AA_seq.append(sequence)
    
for ident1, sequence in fasta_fixed.FASTAReader(nt_query):
    nt_seq.append(sequence)

# parse parallel 
# read ith element of aa sequence. If not "-", then take three first elements from nt_seq file and add to empty string, new
# at the end of the gene, append string new to list. Then restart for loop for next gene.
# I made list to make it easier to format for later.  

list=[]
for aa, nt in itertools.izip(AA_seq, nt_seq):
    new = ''
    nt_pos = 0
    for i in range(0, len(aa)):
        if aa[i] == '-':
            new = new + ("---")
        else:
            codon = nt[nt_pos:nt_pos+3] #take 3 characters
            new = new + codon
            nt_pos = nt_pos + 3
    #print new
    list.append(new)
print ">x\n" +"\n>x\n".join(list)
