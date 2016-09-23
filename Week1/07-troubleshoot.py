""
TROUBLESHOOTING: I've tried to troubleshoot the problem with a bunch of print statements, and I can't figure out the str issue. 
Calculate dS, dN, and dS-dN for each position among the top 1000 BLAST hits
Then, perform Z-test on deviation of dN from dS (dN-dS)
Input is an aligned nt fasta file
Query = week1_query.fa
Target = 05-nt_output
"""
import sys, fasta_fixed
import itertools
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

#Take two files: query, and alignment file

query = open(sys.argv[1])
target = open(sys.argv[2])

quer = ''
tar = []
for ident, seq in fasta_fixed.FASTAReader(query):
    quer = quer + seq
for ident, seq in fasta_fixed.FASTAReader(target):
    tar.append(seq)
        
#print quer

#Iterate by 3. 
## If the three nucleotides match query, continue

for q, nt in itertools.izip(quer,tar):
    nt_pos = 0
    dS_count = 0
    dN_count = 0
    for i in range(0,len(quer),3):
        if q[i]==nt[nt_pos:nt_pos+3]:
            nt_pos += 3
        elif q[i]=="---":
            nt_pos+=3  
        else: 
            if gencode.get(q[i])==gencode.get(nt[nt_pos:nt_pos+3]):
                dS_count+=1
                nt_pos += 3
            elif gencode.get(q[i])!=gencode.get(nt[nt_pos:nt_pos+3]):
                dN_count+=1
                nt_pos +=3

## If they do not match, 
    ## if  "-" in target, go to next line 
    # store query 3 nt seq as variable
    # look up 3 nt seq from first target in dictionary
    # For line 1 of target and query: if value does not match, dN_count+=1
    # if value does match, dS_count += 1
    # go to next line 
    # when finished, append values of count to respective lists
    # then iterate to next 3
# calculate dN-dS list
# create plot of list (which is y-axis), elements (x-axis)
# create y-axis line at y=1.0


#define nonsyn and syn mutations. 
# calculate dN  for each site, append to list
# calculate dS for each site, append to list
# calculate difference, append to listC




# TTT > TTA
#
#
# then, syn_count += 1
# elif non_count += 1
#
# at end of that, add value of count to respective lists
# then iterate the next three, and keep appending til you reach end of sequence
# then print syn and non list (which is in the order of genome position)
#
# then use matplotlib to
