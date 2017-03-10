# -*- coding: utf-8 -*-
import sys
import math

##################################################################################################
### Functions
##################################################################################################

#Calculates the norm of the vector
def norm(a):
    return math.sqrt(sum([i*i for i in a]))

#Calculate the cosine simmilarity between two items.
#The calculus: cos(A,B) = (A*B)/(||A||*||B||).
#Dot product between A and B divided by the product of the norms of A and B.
def cossim(a,b):
    global contzero 
    if norm(a)*norm(b)==0:
         contzero+=1 
         return 0 
    return sum([a[i]*b[i] for i in range(len(a))])/(norm(a)*norm(b))

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

recommender_list = sys.argv[1]
history_list = sys.argv[2]
top_n = int(sys.argv[3])
item_list = sys.argv[4]
output_file = sys.argv[5]
contzero = 0

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

#Get the recommender list
fin = open(recommender_list, "r")
RS = dict()
for i in fin:
    i = i.rstrip()
    line = i.split(" ")
    user = int(line[0])
    if not RS.has_key(user):
        RS[user] = []
    for j in line[1:]:
        RS[user] += [int(j.split(":")[0])]
fin.close()

#Load the history of each user
history = dict()
fin = open(history_list, "r")
for i in fin:
    i = i.rstrip()
    line = i.split("\t")
    user = int(line[0])
    item = int(line[1])
    if not history.has_key(user):
        history[user] = []
    history[user] += [item]
fin.close()

#Load items information
itemset = dict()
fin = open(item_list, "r")
for i in fin:
    i = i.rstrip()
    line = i.split(" ")
    item = int(line[0])
    if not itemset.has_key(item):
        itemset[item] = []
    itemset[item] = [float(j) for j in line[1:]]
fin.close()

##################################################################################################
### Calculating the Auralist metric
##################################################################################################

serendipity = dict()
for user in RS:
	unserendipity = 0
	for h in history[user]:
		for i in RS[user]:
			if i in itemset:
				unserendipity += cossim(itemset[h],itemset[i])/top_n
	unserendipity /= len(RS)*len(history[user])
        if (unserendipity==0):
                serendipity[user] = 0
        else:
          	serendipity[user] = 1/unserendipity

##################################################################################################
### Printing output
##################################################################################################

#Printing normal file
fout = open(output_file, "w")
for user in serendipity:
    fout.write(str(serendipity[user])+"\n")
fout.close()

#Printing normalized file.
fout = open(output_file[:-4]+"_normalized.out", "w")
for user in serendipity:
    normalized = serendipity[user]/max(serendipity.values())
    fout.write(str(normalized)+"\n")
fout.close()
