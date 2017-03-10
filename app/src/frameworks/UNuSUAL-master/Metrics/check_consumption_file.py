# -*- coding: utf-8 -*-
import sys
import os

##################################################################################################
### Functions
##################################################################################################

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

consumption_file = sys.argv[1]

##################################################################################################
### Reading the Consumption File and checking whether it is ok.
##################################################################################################

#Get the recommender list
if not os.path.isfile(consumption_file):
	print 0
	exit(0)

#Load the history of each user
history = dict()
cont_lines = 0
fin = open(consumption_file, "r")
for i in fin:

	#incrementing the counter
	cont_lines += 1

	#read the values
	try:
		i = i.rstrip()
		line = i.split("\t")
		user = int(line[0])
		item = int(line[1])
		rating = float(line[2])
		time = int(line[3])

		#organize the user history
		if not history.has_key(user):
			history[user] = dict()
		if not history[user].has_key(item):
			history[user][item] = dict()
		if not history[user][item].has_key(time):
			history[user][item][time] = rating
	#if there is any problem, print 0 and leave
	except:
		print 0
		exit(0)
fin.close()

if cont_lines == 0:
	print 0
	exit(0)

#file ok
print 1
