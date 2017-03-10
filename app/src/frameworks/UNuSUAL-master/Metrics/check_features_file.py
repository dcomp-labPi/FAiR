# -*- coding: utf-8 -*-
import sys
import os

##################################################################################################
### Functions
##################################################################################################

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

item_list = sys.argv[1]

##################################################################################################
### Reading the features file.
##################################################################################################

#Get the recommender list
if not os.path.isfile(item_list):
	print 0
	exit(0)

#Load items information
itemset = dict()
sizefeatures = 0
cont_lines = 0
fin = open(item_list, "r")
for i in fin:

	#incrementing the counter
	cont_lines += 1

	#testing each line of the file
	try:

		#reading parameters and making the file
		i = i.rstrip()
		line = i.split(" ")
		item = int(line[0])
		if not itemset.has_key(item):
			itemset[item] = []
		itemset[item] = [float(j) for j in line[1:]]

		#checking if all files have the same length
		if sizefeatures==0:
			sizefeatures = len(itemset[item])
		elif sizefeatures!= len(itemset[item]):
			print 0
			exit(0)
	#if there is any problem
	except:
		print 0
		exit(0)
fin.close()

if cont_lines == 0:
	print 0
	exit(0)

#file ok
print 1
