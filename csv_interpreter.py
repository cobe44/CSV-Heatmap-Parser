import os
import sys
import math
import numpy as np
from numpy import genfromtxt
import csv
from collections import defaultdict

with open('Without_Names.csv', 'rb') as csvfile:
    hits_table = csv.reader(csvfile, delimiter=",")
    list = list(hits_table)
    Hit_Genome = []
    for i in range(len(list)):
        Hit_Genome.append(list[i][2])
        Hit_Genome[i] = Hit_Genome[i][1:]



hits_table = genfromtxt('Without_Names.csv', delimiter=",")


Gene_IDs = np.zeros(hits_table.shape[0])
Identity = np.zeros(hits_table.shape[0])

for i in range(hits_table.shape[0]):
    Gene_IDs[i] = hits_table[i][1]
    Identity[i] = hits_table[i][4]
gene_list = []

for i in range(len(Gene_IDs)):
    if Gene_IDs[i] in gene_list:
        pass
    else:
        gene_list.append(Gene_IDs[i])

hit_list = []

for i in range(len(Hit_Genome)):
    if Hit_Genome[i] in hit_list:
        pass
    else:
        hit_list.append(Hit_Genome[i])

new_glist =[[i] for i in gene_list]
new_hlist =[[i] for i in hit_list]

GID_List = Gene_IDs.tolist()
ident_list = Identity.tolist()

all_list = []

all_list.append(GID_List)
all_list.append(Hit_Genome)
all_list.append(ident_list)

ziplist = zip(*all_list)

def iterator(new_glist, ziplist, hit_list):
    for i in range(len(new_glist)):
        for h in range(len(hit_list)):
            found = 0
            for k in range(len(ziplist)):
                if new_glist[i][0] == ziplist[k][0] and ''.join(hit_list[h]) == ziplist[k][1] and found > 0:
                        print "gene:", gene_list[i]
                        print "k:", k
                        print "h:", ''.join(hit_list[h])
                        print ziplist[k][2]
                if ziplist[k][0] == new_glist[i][0] and ''.join(hit_list[h]) == ziplist[k][1]:
                        new_glist[i].append(ziplist[k][2])
                        found += 1
            if (found == 0):
                new_glist[i].append(0)

    return new_glist

new_glist = iterator(new_glist, ziplist, hit_list)



for i in range(len(new_hlist)):
    new_hlist[i] = ''.join(new_hlist[i])

with open('IDs_Hits_identities.csv', 'wb') as writefile:
    csvwriter = csv.writer(writefile, delimiter=",")
    for row in range(len(ziplist)):
        csvwriter.writerow(ziplist[row])

with open('whoozit.csv', 'wb') as writefile:
    csvwriter = csv.writer(writefile, delimiter=",")
    new_hlist.insert(0, 'Gene IDs')
    csvwriter.writerow(new_hlist)
    print "hitlist:", len(new_hlist)
    for row in range(len(new_glist)):
        print "glist:", len(new_glist[row])
        if len(new_glist[row]) == 43:
            print new_glist[row][0]
        csvwriter.writerow(new_glist[row])

print "boogie"
