#!/usr/bin/env python

"""
Purpose: ...to make plink 2 input. 
............to format phenotype txt file for plink2 input. 

"""

import sys
phen = open(sys.argv[1])

#add header
#read line, split 0, split by _, print to new column then print rest of line
for line in phen.readlines():
    if line.startswith("A"):
        field = line.rstrip("\r\n").split()
        ID = field[0]
        ID_0 = ID.split("_")
        fam = ID_0[0]
        samp = ID_0[1]
        print fam + "\t" + samp + "\t" + "\t".join(field[1:])
    else:
        field = line.rstrip("\r\n").split("C")
        print "F_ID" + "\t" + "I_ID" + line.rstrip("\r\n")


