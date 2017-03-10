import sys
import os

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

output = sys.argv[1]
correlation = sys.argv[2]
metrics_file = sys.argv[3:]

##################################################################################################
### Calculating the correlation using Rscript
##################################################################################################

#calcuating the correlation between each metric
for i in range(len(metrics_file)):
	for j in range(i+1,len(metrics_file)):
		outputname = output+"/"+correlation+"_"+metrics_file[i].split("/")[-1].split(".")[0]+metrics_file[j].split("/")[-1].split(".")[0]+".out"
		os.system("Rscript correlation_metrics.r "+metrics_file[i]+" "+metrics_file[j]+" "+correlation+" > "+outputname)
