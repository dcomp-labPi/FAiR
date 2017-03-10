# -*- coding: utf-8 -*-
import sys

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

#getting the arguments
output = sys.argv[1]
metrics_file = sys.argv[2:]

##################################################################################################
### Reading the metrics
##################################################################################################

metricsinfo = []
for metric in metrics_file:
	info = []
	fin = open(metric, "r")
	for j in fin:
		j = j.rstrip()
		info += [j]
	fin.close()
	metricsinfo += [info]

##################################################################################################
### Writing the metrics
##################################################################################################

fout = open(output, "w")
for i in range(len(metricsinfo[0])):
	fout.write(metricsinfo[0][i])
	for j in range(1,len(metricsinfo)):
		fout.write(" "+metricsinfo[j][i])
	fout.write("\n")
fout.close()
