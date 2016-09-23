#!/usr/bin/env python

"""
Take tsv file from BLAST, 
Filter entries that start at 1 and end at 1093
Convert to FASTA
Usage: <python> <tsv> >> <out>
Output: FilteredBLAST.fa (FASTA)?
"""

import sys

tsv = open(sys.argv[1])

for line in tsv.readlines():
    fields = line.rstrip("\r\n").split("\t")
    element = fields[0].split("|")
    #print element[2]
    
    start = (fields[1])
    end = (fields[2])
    ### if in sys file, start = 1 and end = 10293, continue
    if start == str(1) and end == str(10293) in fields[2]:
        print ( ">" + element[3] + "\n" +fields[3])



### print id: element[3]
