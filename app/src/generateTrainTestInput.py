# -*- coding: utf-8 -*


import sys

# get the parameters
file_data = sys.argv[1]
percTrain = float(sys.argv[2])
output_file = sys.argv[3]

# read the data for generate train and test data
file_data = open(file_data, 'r')

dic_data = {}
dic_time = {}
dic_data_test = {}
dic_time_test = {}

for line in file_data:
    line = line.rstrip()
    values = line.split(",")
    value_row = values[0]
    value_col = values[1]
    value_data = float(values[2])
    value_time = float(values[3])

    if value_row in dic_data.keys():
        dic_data[value_row][value_col] = value_data
        dic_time[value_row][value_col] = value_time
    else:
        dic_data[value_row] = {}
        dic_data[value_row][value_col] = value_data
        dic_time[value_row] = {}
        dic_time[value_row][value_col] = value_time

file_data.close()
print('read the data')

# get the amount of users
users = len(dic_data)

file_out_test = open(output_file + "ratings_test.txt", "w")
file_out_train = open(output_file + "ratings_train.txt", "w")

print('work in train and test')

for i, v in enumerate(dic_time):
    # calculates amount the items is consumed
    cont_items = len(dic_time[v].keys())
    # sorted by timestamp
    pos_time = sorted(dic_time[v], key=dic_time[v].__getitem__, reverse=True)
    # calculates amount the items for test data
    amount_test = int(round(cont_items * (1 - percTrain)))
    pos_time = pos_time[:amount_test]

    # salved values
    for j, w in enumerate(dic_time[v].keys()):
        if w in pos_time:
            file_out_test.write(
                "%s::%s::%f::%f\n" % (v, w, dic_data[v][w], dic_time[v][w]))
        else:
            file_out_train.write(
                "%s::%s::%f::%f\n" % (v, w, dic_data[v][w], dic_time[v][w]))
