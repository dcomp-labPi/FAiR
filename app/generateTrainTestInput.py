# -*- coding: utf-8 -*


import os
from random import randint


def gen_train_test(dic_train_rating, dic_train_time, users, perc_train, output_file):
    try:
        # create variables
        dic_test_rating = {}
        dic_test_time = {}
        file_out_test = open(output_file + "test.txt", "w")
        file_out_train = open(output_file + "train.txt", "w")

        for i, v in enumerate(dic_train_time):
            # calculates amount the items is consumed
            cont_items = len(dic_train_time[v].keys())
            # sorted by timestamp
            pos_time = sorted(dic_train_time[v], key=dic_train_time[v].__getitem__, reverse=True)
            # calculates amount the items for test data
            amount_test = int(round(cont_items * (1 - perc_train)))
            pos_time = pos_time[:amount_test]

            # salved values
            for j, w in enumerate(dic_train_time[v].keys()):
                if w in pos_time:
                    file_out_test.write(
                        "%s::%s::%f::%f\n" % (v, w, dic_train_rating[v][w], dic_train_time[v][w]))
                else:
                    file_out_train.write(
                        "%s::%s::%f::%f\n" % (v, w, dic_train_rating[v][w], dic_train_time[v][w]))

        return True
    except:
        return False


def gen_train_test_random(dic_train_rating, users, perc_train, output_file):
    try:
        file_out_test = open(output_file + "test.txt", "w")
        file_out_train = open(output_file + "train.txt", "w")

        for i, v in enumerate(dic_train_rating):
            # calculates amount the items is consumed
            cont_items = len(dic_train_rating[v].keys())
            # calculates amount the items for test data
            amount_test = int(round(cont_items * (1 - perc_train)))
            # calculates random positions for test
            positions = []
            data_keys = list(dic_train_rating[v].keys())
            for j in range(amount_test):
                pos = randint(0, cont_items - 1)
                while pos in positions:
                    pos = randint(0, cont_items - 1)
                positions.append(data_keys[pos])

            # salved values
            for j, w in enumerate(dic_train_rating[v].keys()):
                if w in positions:
                    file_out_test.write(
                        "%s::%s::%f\n" % (v, w, dic_train_rating[v][w]))
                else:
                    file_out_train.write(
                        "%s::%s::%f\n" % (v, w, dic_train_rating[v][w]))

        return True
    except:
        return False


def generate_train_test_input(file_data, window, perc_train, delimeter, output_file):
    # Get the recommender list
    if not os.path.isfile(file_data):
        window.msgError('Sorry, but your file data ' + file_data +
                        ' not exist')
        return False

    # set config and read file data
    fdata = open(file_data, 'r')

    output_file = output_file + '/'

    # create variables
    dic_train_rating = {}
    dic_train_time = {}
    perc_train = float(perc_train)
    type_code = "default"

    for line in fdata:
        try:
            line = line.rstrip()
            values = line.split(delimeter)
            if len(values) == 4:
                id_user = values[0]
                id_item = values[1]
                rating = float(values[2])
                timestamp = float(values[3])

                if dic_train_rating.get(id_user, False):
                    dic_train_rating[id_user][id_item] = rating
                    dic_train_time[id_user][id_item] = timestamp
                else:
                    dic_train_rating[id_user] = {}
                    dic_train_time[id_user] = {}
                    dic_train_rating[id_user][id_item] = rating
                    dic_train_time[id_user][id_item] = timestamp

                type_code = "normal"
            elif len(values) == 3:
                id_user = values[0]
                id_item = values[1]
                rating = float(values[2])

                if dic_train_rating.get(id_user, False):
                    dic_train_rating[id_user][id_item] = rating
                else:
                    dic_train_rating[id_user] = {}
                    dic_train_rating[id_user][id_item] = rating

                type_code = "random"
            else:
                print('error in format of test file: %s' % fdata.name)
                window.msgError('error in format of test file: %s' % fdata.name)
                return False

        except:
            print('error in format of test file: %s' % fdata.name)
            window.msgError('error in format of test file: %s' % fdata.name)
            return False

    fdata.close()

    # get the amount of users
    users = len(dic_train_rating)

    if type_code == "normal":
        result = gen_train_test(dic_train_rating, dic_train_time, users, perc_train, output_file)
    elif type_code == "random":
        result = gen_train_test_random(dic_train_rating, users, perc_train, output_file)
    else:
        print('error in type code')
        window.msgError('error in format file')
        result = False

    return result
