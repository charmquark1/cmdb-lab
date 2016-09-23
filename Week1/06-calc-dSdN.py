#!/usr/bin/env python
"""
Calculate dS, dN, and dS-dN for each position among the top 1000 BLAST hits
Then, perform Z-test on deviation of dN from dS (dN-dS)
Input is an aligned nt fasta file
Query = week1_query.fa
Target = 05-nt_output
"""
import sys, fasta_fixed
import itertools
import scipy.stats as stats
import matplotlib.pyplot as plt

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', '---':'-', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'X', 'TAG':'X', 'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

#Take three files: query, alignment file and 06_first_target_sequence

query = open(sys.argv[1])
targ1 = open(sys.argv[3])
target = open(sys.argv[2])

quer = ''
tar = []
for ident, seq in fasta_fixed.FASTAReader(query):
    quer = quer + seq
for ident, seq in fasta_fixed.FASTAReader(targ1):
    tar.append(seq)
for ident, seq in fasta_fixed.FASTAReader(target):
    tar2.append(seq)
        
#print quer

#First, Iterate tar1 and query by 3: 
## If the three nucleotides match query, continue
# when finished reading tar1, you should get a list of dS and dN at every position
## make first dS and dN list from sequence
# then, start reading new target file line by line,
# at the end of every line, SUM your list with dS list and dN list. iterate till end. 
dS_count = []
dN_count = []

#First, Iterate tar1 and query by 3: 
for q, nt in itertools.izip(quer,tar):
    nt_pos = 0
    for i in range(0,len(quer),3):
        if q[i]==nt[nt_pos:nt_pos+3]: #THIS IS WHERE I GET MY STR ERROR.
            nt_pos += 3
            dN_count.append(0)
            dS_count.append(0)
        elif q[i]=="---":
            nt_pos+=3 
            dS_count.extend([0,0,0])
            dN_count.extend([0,0,0])
        else: 
            if gencode.get(q[i])==gencode.get(nt[nt_pos:nt_pos+3]):
                dS_count.append(1)
                dN_count.append(0)
                nt_pos += 3
            elif gencode.get(q[i])!=gencode.get(nt[nt_pos:nt_pos+3]):
                dN_count.append(1)
                dS_count.append(0)
                nt_pos +=3
#now parse target2 file, and sum to master lists when you finish iterating through one gene
## If they do not match, 
    ## if  "-" in target, go to next line 
    # store query 3 nt seq as variable
    # look up 3 nt seq from first target in dictionary
    # For line 1 of target and query: if value does not match, append to dN_count as first element
    # if value does match, dS_count += 1
    # iterate through  
    # when finished, append values of count to respective lists
    # then iterate to next 3


for q, nt in itertools.izip(quer,tar2):
    nt_pos = 0
    list_pos = 0
    for i in range(0,len(quer),3):
        if q[i]==nt[nt_pos:nt_pos+3]: #THIS IS WHERE I GET MY STR ERROR.
            nt_pos += 3
            list_pos +=1
        elif q[i]=="---":
            nt_pos+=3
            list_pos +=3  
        else: 
            if gencode.get(q[i])==gencode.get(nt[nt_pos:nt_pos+3]):
                dS_count[list_pos]+=1
                list_pos+=1 
                nt_pos += 3
            elif gencode.get(q[i])!=gencode.get(nt[nt_pos:nt_pos+3]):
                dN_count[list_pos]+=1
                list_pos+=1
                nt_pos +=3

# calculate dN-dS list
dN_minus_dS = [y-x for x, y in zip(dS_count, dN_count)]
dN_dS_x = []
j = 0
for i in range(len(dN_minus_dS)):
    dN_dS_x.append(j)
    j+=1
    

#dN_minus_dS = [dN_count[j]-dS_count[j] for j in range(len(dN_count)]
# create plot of list (which is y-axis), elements (x-axis)

plt.figure()
plt.plot(dN_minus_dS, dN_dS_x)
plt.title("dN-dS of WNV-related proteins")
plt.xlabel("position")
plt.ylabel("dN-dS")
plt.savefig("07-dNdS_of_regions.png")


# z-score of dN, dS
z_score = stats.zscore(dN_minus_dS)

plt.figure()
plt.plot(z_score, dN_dS_x)
plt.xlabel("position")
plt.ylabel("Z score")
plt.savefig("Z score of mutation over position")
