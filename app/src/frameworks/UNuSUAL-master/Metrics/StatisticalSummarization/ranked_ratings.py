import sys
import os
from scipy.stats import rankdata


##################################################################################################
### Functions
##################################################################################################

##################################################################################################
### Capturing the input from the parameters
##################################################################################################
metrics_file = sys.argv[1]
outputname = sys.argv[2]

##################################################################################################
### Reading the file
##################################################################################################

#Get the recommender list
fin = open(metrics_file, "r")
n_metrics = 0
for i in fin:
	i = i.rstrip()
	values = i.split(" ")
	n_metrics = len(values)
	break
fin.close()

#reading metrics
metrics = [[] for i in range(n_metrics)]
for i in range(n_metrics):
	fin = open(metrics_file, "r")
	for j in fin:
		j = j.rstrip()
		values = j.split(" ")
		metrics[i] += [float(values[i])]
	fin.close()

##################################################################################################
### Ranking
##################################################################################################

#ranking the metrics
for i in range(n_metrics):
	metrics[i].sort()
	metrics[i].reverse()

##################################################################################################
### Saving the information in a file and then plot it 
##################################################################################################

#save the file 
f = open(outputname, "w")
cont = 1
for i in range(len(metrics[0])):
	f.write(str(cont))
	for j in range(n_metrics):
		f.write(" "+str(metrics[j][i]))
	f.write("\n")
	cont += 1
f.close()

#ploting
os.system("gnuplot -e \"datafile='"+outputname+"';outputname='"+outputname[:-4]+".png' \" gnuplot_ranked_metrics.gp")