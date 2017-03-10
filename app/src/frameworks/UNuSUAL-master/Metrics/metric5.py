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
    if (norm(a)*norm(b))==0:
        return 0
    return sum([a[i]*b[i] for i in range(len(a))])/(norm(a)*norm(b))

#Get the rating from the user's recommendation
def get_rating(recommendation):
    return float(recommendation.split(":")[1])

#Get the item id from the user's recommendation
def get_item(recommendation):
    return int(recommendation.split(":")[0])

#check whether the item is related to the user's preferences
def is_rel(item, user_history, items_info):
    MINIMUMAVGSIMMILARITY = 0.4
    i = get_item(item)
    avg_distance = 0
    for h in user_history:
        if items_info.has_key(i) and items_info.has_key(h):
            avg_distance += cossim(items_info[i], items_info[h])
    avg_distance /= len (user_history)
    if avg_distance>MINIMUMAVGSIMMILARITY:
        return 1
    else:
        return 0

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

recommender_list = sys.argv[1]
primitive_list = sys.argv[2]
history_list = sys.argv[3]
item_list = sys.argv[4]
top_n = int(sys.argv[5])
output_file = sys.argv[6]

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
    for i in line[1:]:
        RS[user] += [i]
fin.close()

#Get the primitive prediction model
fin = open(primitive_list, "r")
PM = dict()
for i in fin:
    i = i.rstrip()
    line = i.split(" ")
    user = int(line[0])
    if not PM.has_key(user):
        PM[user] = []
    for i in line[1:]:
        PM[user] += [i]
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
    history[user] = [item]
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
    itemset[item] = [float(j) for j in line[5:]]
fin.close()

##################################################################################################
### Calculating the evaluating metric
##################################################################################################

unexpectedness = dict()
for user in RS:
    unexpectedness[user] = 0
    for i in range(len(RS[user])):
        unexpectedness[user] += max(get_rating(RS[user][i])-get_rating(PM[user][i]), 0) * is_rel(RS[user][i], history[user], itemset)
    unexpectedness[user] /= len(RS[user])
    
##################################################################################################
### Printing output
##################################################################################################

fout = open(output_file, "w")
for user in unexpectedness:
    fout.write(str(unexpectedness[user])+"\n")
fout.close()

fout = open(output_file[:-4]+"_normalized.out", "w")
for user in unexpectedness:
    normalized = unexpectedness[user]/max(unexpectedness.values())
    fout.write(str(normalized)+"\n")
fout.close()
