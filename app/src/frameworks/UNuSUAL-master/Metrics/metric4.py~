# -*- coding: utf-8 -*-
import sys

##################################################################################################
### Functions
##################################################################################################

#For each item, calculates the number of users that has consumed it
def calculate_number_consumption_item(itemset, history):
	items_consumption = dict()
	for item in itemset:
		items_consumption[item] = 0
		for user in history:
			if item in history[user]:
				items_consumption[item] += 1
	return items_consumption

#For each pair of items, calculates the number of users that has consumed it
def calculate_pair_consumption_item(itemset, history):
	items_consumption_pair = dict()
	for user in history:
		items_user = history[user]
		for i in range(len(items_user)):
			item1 = items_user[i]
			if not items_consumption_pair.has_key(item1):
				items_consumption_pair[item1] = dict()
			for j in range(i+1,len(items_user)):
				item2 = items_user[j]
				if not items_consumption_pair[item1].has_key(item2):
					items_consumption_pair[item1][item2] = 0
				items_consumption_pair[item1][item2] += 1
	return items_consumption_pair

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

recommender_list = sys.argv[1]
history_list = sys.argv[2]
top_n = int(sys.argv[3])
item_list = sys.argv[4]
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
    itemset[item] = 0
fin.close()

##################################################################################################
### Calculating the Metric
##################################################################################################

#Calculates the items consumption for each item
items_consumption = calculate_number_consumption_item(itemset, history)

#Calculate the items consumption for each pair of items
items_consumption_pair = calculate_pair_consumption_item(itemset, history)

#For each user
unexpectedness = dict()
for u in RS:

	#For each item in the user's recommendation list
	unexpectedness[u] = 0
	for recommended_item in RS[u]:
		
		#For each item in the user's consumption list, calculate Ni,j/(Ni+Nj-Ni,j), 
		#where i is the recommended item and j is the consumed item
		expected = 0
		for consumed_item in history[u]:
			if recommended_item in items_consumption_pair:
				if items_consumption_pair.has_key(recommended_item) and items_consumption_pair[recommended_item].has_key(consumed_item):
					item_i_j = items_consumption_pair[recommended_item][consumed_item]
				elif items_consumption_pair.has_key(consumed_item) and items_consumption_pair[consumed_item].has_key(recommended_item):
					item_i_j = items_consumption_pair[consumed_item][recommended_item]
				else:
					item_i_j = 0
				expected += item_i_j/float(items_consumption[recommended_item]+items_consumption[consumed_item]-item_i_j)
		expected /= len(history[u])

		#Sum in the unexpectedness of the user.
		if expected!=0: 
			unexpectedness[u] += 1/expected

##################################################################################################
### Printing output
##################################################################################################

#Printing normal file
fout = open(output_file, "w")
for user in unexpectedness:
    fout.write(str(unexpectedness[user])+"\n")
fout.close()

#Printing normalized file.
fout = open(output_file[:-4]+"_normalized.out", "w")
for user in unexpectedness:
    normalized = unexpectedness[user]/max(unexpectedness.values())
    fout.write(str(normalized)+"\n")
fout.close()
