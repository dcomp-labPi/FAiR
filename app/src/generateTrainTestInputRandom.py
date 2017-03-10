# -*- coding: utf-8 -*


import sys
from random import randint

# get the parameters
file_data = sys.argv[1]
perc_train = float(sys.argv[2])
output_file = sys.argv[3]

# read the data for generate train and test data
file_data = open(file_data, 'r')

dic_data = {}
dic_data_test = {}

for line in file_data:
    line = line.rstrip()
    values = line.split("::")
    value_row = values[0]
    value_col = values[1]
    value_data = float(values[2])

    if value_row in dic_data.keys():
        dic_data[value_row][value_col] = value_data
    else:
        dic_data[value_row] = {}
        dic_data[value_row][value_col] = value_data

file_data.close()
print('read the data')

# get the amount of users
users = len(dic_data)

file_out_test = open(output_file + "ratings_test.txt", "w")
file_out_train = open(output_file + "ratings_train.txt", "w")

print('work in train and test')

for i, v in enumerate(dic_data):
    # calculates amount the items is consumed
    cont_items = len(dic_data[v].keys())
    # calculates amount the items for test data
    amount_test = int(round(cont_items * (1 - perc_train)))
    # calculates random positions for test
    positions = []
    data_keys = list(dic_data[v].keys())
    for j in range(amount_test):
        pos = randint(0, cont_items - 1)
        while pos in positions:
            pos = randint(0, cont_items - 1)
        positions.append(data_keys[pos])

    # salved values
    for j, w in enumerate(dic_data[v].keys()):
        if w in positions:
            file_out_test.write(
                "%s::%s::%f\n" % (v, w, dic_data[v][w]))
        else:
            file_out_train.write(
                "%s::%s::%f\n" % (v, w, dic_data[v][w]))
