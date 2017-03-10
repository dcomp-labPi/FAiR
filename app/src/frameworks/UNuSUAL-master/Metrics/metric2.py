# -*- coding: utf-8 -*-
import sys

##################################################################################################
### Functions
##################################################################################################

#Generate the useful items list
def generate_useful_items(itemsaverage, mean):

	#Compare the mean to check which one is a useful item.
	use = []
	for item in itemsaverage:
		if itemsaverage[item]>=mean:
			use += [item]
	return use


##################################################################################################
### Capturing the input from the parameters
##################################################################################################

#read the inputs
recommender_list = sys.argv[1]
primitive_list = sys.argv[2]
history_list = sys.argv[3]
top_n = int(sys.argv[4])
output_file = sys.argv[5]

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

#Get the recommender list
RS = dict()
fin = open(recommender_list, "r")
for i in fin:
    i = i.rstrip()
    line = i.split(" ")
    user = int(line[0])
    if not RS.has_key(user):
        RS[user] = []
    for i in line[1:]:
        RS[user] += [int(i.split(":")[0])]
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
	history[user] = [item]

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

##################################################################################################
### Generating the Useful items
##################################################################################################

#Calculate items average
itemsaverage = dict()
for item in itemsrating:
	itemsaverage[item] = itemsrating[item]/itemscount[item]

#Calculating the mean of the ratings.
useful = dict()
for user in ratings:
	ratings[user].sort()
	mean = sum(ratings[user])/len(ratings[user])
	useful[user] = generate_useful_items(itemsaverage, mean)

##################################################################################################
### Calculating unexpectedness
##################################################################################################

#For each user
UNEXPECTEDNESS = dict()
for user in RS:

	#generate the list of not expected items. An item is not expected if it wasn't recommended by
	#a primitive recommender 
	not_expected = []
	for item in RS[user]:
		if item not in PM[user]:
			not_expected += [item]
	#Generate the not expected items are also useful, 
	unexpected = []
	for item in not_expected:
		if item in useful[user]:
			unexpected += [item]
	UNEXPECTEDNESS[user] = len(unexpected)/float(top_n)

##################################################################################################
### Printing output
##################################################################################################

#Printing normal file
fout = open(output_file, "w")
for user in UNEXPECTEDNESS:
    fout.write(str(UNEXPECTEDNESS[user])+"\n")
fout.close()

#Printing normalized file.
fout = open(output_file[:-4]+"_normalized.out", "w")
for user in UNEXPECTEDNESS:
	normalized = UNEXPECTEDNESS[user]/max(UNEXPECTEDNESS.values())
	fout.write(str(normalized)+"\n")
fout.close()