# -*- coding: utf-8 -*-
import sys

##################################################################################################
### Functions
##################################################################################################

#Function that compares the two lists and returns only the existing items in l1, but not in l2
def backslash_function(list1, list2):
    list_result = []
    for l1 in list1:
        insert = True
        for l2 in list2:
            if l1==l2:
                insert = False
                break
        if insert == True:
            list_result += [l1]
    return list_result

#Calculate the serendipity of the unexpected item of a user's recommendation list
def calculate_srdp(unexp, useful):
    srdp = 0
    for i in unexp:
        if i in useful:
       	    srdp += 1
    if len(unexp)!=0: 
        srdp/=float(len(unexp))
    else:
		srdp=0 
    return srdp

#Generate the useful items list
def generate_useful_items(itemsaverage, mean):

	#Compare the mean to check which one is a useful item.
	use = []
	for item in itemsrating:
		if itemsaverage[item]>mean:
			use += [item]
	return use

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

recommender_list = sys.argv[1]
primitive_list = sys.argv[2]
history_list = sys.argv[3]
top_n = int(sys.argv[4])
output_file = sys.argv[5]

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
        RS[user] += [int(i.split(":")[0])]
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
        PM[user] += [int(i.split(":")[0])]
fin.close()

#Load the history of each user
history = dict()
itemsrating = dict()
itemscount = dict()
ratings = dict()
fin = open(history_list, "r")
for i in fin:

	#read the values
	i = i.rstrip()
	line = i.split("\t")
	user = int(line[0])
	item = int(line[1])
	rating = float(line[2])

	#organize the user history
	if not history.has_key(user):
	    history[user] = []
	history[user] += [item]

	#organize the ratings
	if not itemsrating.has_key(item):
		itemsrating[item] = 0
	if not itemscount.has_key(item):
		itemscount[item] = 0
	itemsrating[item] += rating
	itemscount[item] += 1

	if not ratings.has_key(user):
		ratings[user] = []
	ratings[user] += [rating]

fin.close()

##################################################################################################
### Generating the Useful items
##################################################################################################

#Calculate items average
itemsaverage = dict()
for item in itemsrating:
	itemsaverage[item] = itemsrating[item]/itemscount[item]

#Calculating the mean of the ratings.
usefulness = dict()
for user in ratings:
	ratings[user].sort()
	mean = sum(ratings[user])/len(ratings[user])

	#generating vector of useful items
	usefulness[user] = generate_useful_items(itemsaverage, mean)

##################################################################################################
### Creating the vector of UNEXP and calculating the metric on the data
##################################################################################################

SRDP = dict()

countuser=0
for user in RS:
    UNEXP = backslash_function(RS[user], PM[user])
    SRDP[user] = calculate_srdp(UNEXP, usefulness[user])

##################################################################################################
### Printing output
##################################################################################################

#Printing normal file
fout = open(output_file, "w")
for user in SRDP:
    fout.write(str(SRDP[user])+"\n")
fout.close()

#Printing normalized file. 
fout = open(output_file[:-4]+"_normalized.out", "w")
for user in SRDP:
	normalized = SRDP[user]/max(SRDP.values())
	fout.write(str(normalized)+"\n")
fout.close()
