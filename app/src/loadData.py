# -*- coding: utf-8 -*


import numpy as np
import sys


def load_data_test(file_test, window):
    # read the test data and mount the matrix
    file_test = open(file_test, 'r')

    dic_u_test = {}
    dic_i_test = {}

    for line in file_test:
        try:
            line = line.rstrip()
            values = line.split("::")
            value_row = values[0]
            value_col = values[1]
            value_data = float(values[2])
            # test = values[4]

            if dic_u_test.get(value_row, False):
                dic_u_test[value_row][value_col] = value_data
            else:
                dic_u_test[value_row] = {}
                dic_u_test[value_row][value_col] = value_data

            if dic_i_test.get(value_col, False):
                dic_i_test[value_col][value_row] = value_data
            else:
                dic_i_test[value_col] = {}
                dic_i_test[value_col][value_row] = value_data
        except:
            print(str(sys.exc_info()[0]))
            print('error in format of test file: %s' % file_test.name)
            window.loader_window.windowApp.destroy()
            window.msgError('error in format of test file: %s' % file_test.name)
            raise

    file_test.close()
    print('read the test data')
    # reading end

    # return the data matrix
    return dic_u_test, dic_i_test


def load_data_training(file_training, window):
    # read the training data and mount the matrix
    file_training = open(file_training, 'r')

    dic_u_training = {}
    dic_i_training = {}
    amount_ratings = 0

    for line in file_training:
        try:
            amount_ratings += 1
            line = line.rstrip()
            values = line.split("::")
            value_row = values[0]
            value_col = values[1]
            value_data = float(values[2])
            # test = values[4]

            if dic_u_training.get(value_row, False):
                dic_u_training[value_row][value_col] = value_data
            else:
                dic_u_training[value_row] = {}
                dic_u_training[value_row][value_col] = value_data

            if dic_i_training.get(value_col, False):
                dic_i_training[value_col][value_row] = value_data
            else:
                dic_i_training[value_col] = {}
                dic_i_training[value_col][value_row] = value_data
        except:
            print(str(sys.exc_info()[0]))
            print('error in format of training file: %s' % file_training.name)
            window.loader_window.windowApp.destroy()
            window.msgError('error in format of training file: %s' % file_training.name)
            raise

    file_training.close()
    print('read the training data')
    # reading end

    # return the data matrix
    return dic_u_training, dic_i_training, amount_ratings


def load_data_topN(file_top_n):
    file_top_n = open(file_top_n, "r")
    lines = []
    ids = []
    ratings = []
    dic_u_top = {}
    cont_u = 0
    for line in file_top_n:
        aux = line.split()
        lines.append(aux[1:])
        dic_u_top[cont_u] = aux[0]
        cont_u += 1

    for i in range(len(lines)):
        if len(lines[i]) != 100:
            print('i : %d l : %d' % (i, len(lines[i])))
        id_aux = []
        ra_aux = []
        for j in range(len(lines[i])):
            id_aux.append(lines[i][j].split(":")[0])
            ra_aux.append(float(lines[i][j].split(":")[1]))
        ids.append(id_aux)
        ratings.append(ra_aux)

    matrix_top_n = np.array(ids)
    matrix_ratings = np.array(ratings)
    file_top_n.close()
    print('read the topN data')
    # reading end

    return dic_u_top, matrix_top_n, matrix_ratings


def load_data_mymedialite(file_top_n):
    file_top_n = open(file_top_n, "r")
    lines = []
    ids = []
    ratings = []
    dic_u_top = {}
    cont_u = 0
    for line in file_top_n:
        aux = line.split()
        dic_u_top[cont_u] = aux[0]
        cont_u += 1
        aux = aux[1][1:]
        aux = aux[:-1].split(",")
        lines.append(aux)

    for i in range(len(lines)):
        if len(lines[i]) != 100:
            print('i : %d l : %d' % (i, len(lines[i])))
        id_aux = []
        ra_aux = []
        for j in range(len(lines[i])):
            id_aux.append(lines[i][j].split(":")[0])
            ra_aux.append(float(lines[i][j].split(":")[1]))
        ids.append(id_aux)
        ratings.append(ra_aux)

    matrix_top_n = np.array(ids)
    matrix_ratings = np.array(ratings)
    file_top_n.close()
    print('read the topN data')
    # reading end

    return dic_u_top, matrix_top_n, matrix_ratings


def convert_file_mymedialite(file_top_n, output_file):
    # read the training data and mount the matrix
    file_top_n = open(file_top_n, 'r')

    file_out = open(output_file + "file_mymedialite_topn.txt", 'w')

    lines = []
    ids = []
    ratings = []
    dic_u_top = {}
    cont_u = 0
    for line in file_top_n:
        aux = line.split()
        user = aux[0]
        aux = aux[1][1:]
        aux = aux[:-1].split(",")
        file_out.write("%s %s\n" % (user, " ".join(aux)))


def load_data_feature(file_feature):
    # create the dictionary of features
    file_in = open(file_feature, "r")

    dic_features = {}
    amount_features = len(file_in.readline().split("::"))
    for line in file_in:
        line = line.rstrip()
        values = line.split(" ")
        values = list(map(int, values))
        dic_features[str(values[0])] = values[1:]

    file_in.close()
    # reading end

    return dic_features, amount_features
