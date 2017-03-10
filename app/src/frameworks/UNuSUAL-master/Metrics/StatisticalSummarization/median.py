# -*- coding: utf-8 -*-
import sys
import os
import math

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

metrics_file = sys.argv[1]
outputfile = sys.argv[2]

##################################################################################################
### Performing the calculation
##################################################################################################

#Get the recommender list
fin = open(metrics_file, "r")
metrics = []
for i in fin:
	i = i.rstrip()
	values = i.split(" ")
	values = [float(i) for i in values]
	metrics += [values]
fin.close()

#organizing the vectors
median_vector = [[] for i in range(len(metrics[0]))]
for i in range(len(metrics)):
	for j in range(len(metrics[i])):
		median_vector[j] += [metrics[i][j]]

#Calculating the metrics
median = [0 for i in range(len(metrics[0]))]
for j in range(len(median_vector)):
	vector = median_vector[j]
	vector.sort()
	if len(vector)%2!=0:
		median[j] = vector[len(vector)/2+1]
	else:
		median[j] = (vector[len(vector)/2]+vector[len(vector)/2+1])/float(2)

##################################################################################################
### Printing the results in the file and ploting the results
##################################################################################################

#printing results
f = open(outputfile, "w")
for j in range(0, len(median)):
	f.write("Metric"+str(j+1)+"\t"+str(median[j])+"\n")
f.close()

#calling the plot
os.system("gnuplot -e \"datafile='"+outputfile+"'; outputname='"+outputfile[:-4]+".png"+"'; maxy='"+str(max(median)+0.05)+"'\" gnuplot_median.gp")