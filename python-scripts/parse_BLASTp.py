# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:10:12 2020

@author: alaguillog
"""

def get_mean(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

BLASTp = open(r"path").read()
BLASTp = BLASTp.split("BLASTP 2.2.26 [Sep-21-2011]")
BLASTp = BLASTp[1:len(BLASTp)-1]     

#results format: (DECOY_ID, [[protein, score, e_value], [protein, score, e_value], ...])
results = []
for query in BLASTp:
    query = query.split("\n")
    query = [line for line in query if line.strip()]
    hits = []
    for i in range(len(query) - 1):
        line = query[i]
        if line[0:6] == "Query=":
            decoy_id = line
        if line == " ***** No hits found ******":
            status = 0
        if line[0:42] == "Sequences producing significant alignments":
            status = 1
            while i < (len(query) - 2):
                i = i + 1
                next_line = query[i]
                if next_line[0] == ">":
                    break
                else:
                    next_line = next_line.split("   ")
                    next_line[1] = float(next_line[1].strip())
                    next_line[2] = float(next_line[2].strip())
                    hits.append(next_line)
    results.append((decoy_id, hits))     

# Generate Report
significant_alignments = 0
scores = []
e_values = []
for i in results:
    if i[1]:
        significant_alignments = significant_alignments + 1
        scores.append(i[1][0][1])
        e_values.append(i[1][0][2])
        
print(significant_alignments, "decoys with significant alignments found.")
print("The mean score is", get_mean(scores))
print("The mean e-value is", get_mean(e_values))

# The lower the E-value, or the closer it is to zero, the more "significant"
# the match is. However, keep in mind that virtually identical short
# alignments have relatively high E values. This is because the calculation
# of the E value takes into account the length of the query sequence. These
# high E values make sense because shorter sequences have a higher
# probability of occurring in the database purely by chance.

