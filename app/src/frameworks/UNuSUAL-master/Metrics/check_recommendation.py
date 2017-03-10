# -*- coding: utf-8 -*-
import sys
import os

##################################################################################################
### Functions
##################################################################################################

recommendation_list = sys.argv[1]
top = int(sys.argv[2])

##################################################################################################
### Reading the features file.
##################################################################################################

#Get the recommender list
if not os.path.isfile(recommendation_list):
	print 0
	exit(0)


#Load recommendation information
cont_lines = 0
fin = open(recommendation_list, "r")
RS = dict()
for i in fin:

	cont_lines += 1

	#check if the recommendation file is ok
	try:

		#reading
		i = i.rstrip()
		line = i.split(" ")
		user = int(line[0])

		#checking user
		if not RS.has_key(user):
		    RS[user] = dict()

		#inserting all the items
		for j in line[1:]:
		    RS[user][int(j.split(":")[0])] = float(j.split(":")[1])

		#check if the size of the recommendation is the same for all users.
		print len(line[1:])
		if len(line[1:])!=top:
			print 0
			exit(0)

	#if there is any problem with the recommdation file
	except:
		print 0
		exit(0)

fin.close()

if cont_lines == 0:
	print 0
	exit(0)

#file is ok
print 1

