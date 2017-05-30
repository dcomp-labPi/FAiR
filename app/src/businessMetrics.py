# -*- coding: utf-8 -*


import numpy as np
import os
import subprocess
import sys
import math

from plotGraphs import plot_graphs
from loadData import load_data_feature


def diversity_novelty_metrics(test_file, train_file, top_n_file, users, amount_n, output_file):
    # settings output Directory
    output_directory = output_file + 'diversityNovelty'

    # create output directory if it does not exist
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        print('error creating the folder in : %s' % output_directory)
        sys.exit(2)

    # settings output Directory
    output_file = output_directory + '/'


    command = "cd src/frameworks/vargas/src/ && make && ./getMetrics " \
              "-b " + train_file + " " \
              "-p " + top_n_file + " " \
              "-o " + output_file + "frameOut.txt " \
              "-l " + test_file + " "\
              "-n " + str(amount_n) +\
              " && make clean"

    if not subprocess.call("cd " + output_file , shell=True) or not subprocess.call("cd " + train_file , shell=True) or not subprocess.call("cd " + top_n_file , shell=True):
        print(output_file)
        subprocess.call(command, shell=True)
    else:
        train_file_change = train_file.replace(" ", "\ ")
        top_n_file_change = top_n_file.replace(" ", "\ ")
        test_file_change = test_file.replace(" ", "\ ")
        output_file_change = output_file.replace(" ", "\ ")
        command = "cd src/frameworks/vargas/src/ && make && ./getMetrics " \
              "-b " + train_file_change + " " \
              "-p " + top_n_file_change + " " \
              "-o " + output_file_change + "frameOut.txt " \
              "-l " + test_file_change + " "\
              "-n " + str(amount_n) +\
              " && make clean"
        subprocess.call(command, shell=True)
        

    #remove \ before space in outputfile
    output_file = output_file.replace("\ ", " ")

    try:
        file_in = open(output_file + "frameOut.txt.0", "r")
    except FileNotFoundError:
        print("There is a folder in output ṕath with space in name, please rename all folders with space in name")

    user_id = []
    novelty = []
    diversity = []
    for line in file_in:
        line = line.rstrip()
        values = line.split()
        user_id.append(values[0])
        novelty.append(values[3])
        diversity.append(values[6])

    # sorts the elements
    novelty = np.sort(novelty)[::-1]
    novelty = np.array(novelty, dtype=float).reshape(1, users)
    diversity = np.sort(diversity)[::-1]
    diversity = np.array(diversity, dtype=float).reshape(1, users)
    # saves the values novelty
    matrix_analysis = np.concatenate(
        (np.transpose(np.arange(1, users + 1).reshape(1, users)),
         np.transpose(novelty)),
        axis=1)
    np.savetxt(output_file + 'novelty.txt', matrix_analysis)
    # generated graphics
    plot_graphs((np.arange(users) / users) * 100, novelty[0], 'Users (%)',
                'novelty',
                output_file + 'novelty.eps', 'Novelty')
    # saves the values diversity
    matrix_analysis = np.concatenate(
        (np.transpose(np.arange(1, users + 1).reshape(1, users)),
         np.transpose(diversity)),
        axis=1)
    np.savetxt(output_file + 'diversity.txt', matrix_analysis)
    # generated graphics
    plot_graphs((np.arange(users) / users) * 100, diversity[0], 'Users (%)',
                'diversity',
                output_file + 'diversity.eps', 'Diversity')

    # set \ before space in outputfile
    if not subprocess.call("cd " + output_file + " && rm frameOut.txt.0", shell=True):
        pass;
    else:
        output_file_change = output_file.replace(" ", "\ ")
        subprocess.call("cd " + output_file_change + " && rm frameOut.txt.0", shell=True)


def catalog_coverage(dic_u_test, dic_u_top, matrix_top_n, average_note_user, amount_n, users, items, output_file):
    # number of relevant items in the set topN
    nrs = 0
    dic_temp = {}
    for i in range(users):
        for j in range(amount_n):
            if dic_u_test[dic_u_top[i]].get(matrix_top_n[i][j], False) >= average_note_user[dic_u_top[i]]:
                if not (matrix_top_n[i][j] in dic_temp.keys()):
                    dic_temp[matrix_top_n[i][j]] = bool
                    nrs += 1

    catalog_cov = nrs / items
    fileout = open(output_file + "catalog-coverage.txt", 'w')
    fileout.write("%f" % catalog_cov)
    print("CATALOG COVERAGE : %f" % catalog_cov)


def genre_coverage(dic_u_training, matrix_top_n, average_note_user, users, amount_n, file_feature, output_file):
    # settings output Directory
    output_directory = output_file + 'genreCoverage'

    # create output directory if it does not exist
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        print('error creating the folder in : %s' % output_directory)
        sys.exit(2)

    # settings output Directory
    output_file = output_directory + '/'

    # load data of features
    dic_features, amount_features = load_data_feature(file_feature)

    # for each user u
    # ru+ is the set of relevanted rated items
    # su is the set of recommended items
    # ru+ intersection su / ru+
    ru = [0] * amount_features
    genre_cov = []
    cov = 0
    for u, u_id in enumerate(dic_u_training):
        # calculate Ru+
        for i, i_id in enumerate(dic_u_training[u_id].keys()):
            if dic_u_training[u_id][i_id] >= average_note_user[u_id]:
                ru = union(ru, dic_features[i_id])

        # calculate Su
        su = [0] * amount_features
        for n in range(amount_n):
            su = union(su, dic_features[matrix_top_n[u][n]])

        value_cov = (sum(intersection(ru, su))) / sum(ru)
        if value_cov == 0:
            genre_cov.append(0)
        else:
            genre_cov.append(value_cov)
            cov += value_cov

    # sorts the elements
    genre_cov = np.sort(genre_cov)[::-1]
    genre_cov = np.array(genre_cov).reshape(1, users)
    # saves the values
    matrix_analysis = np.concatenate(
        (np.transpose(np.arange(1, users + 1).reshape(1, users)),
         np.transpose(genre_cov)),
        axis=1)
    np.savetxt(output_file + 'genre-coverage.txt', matrix_analysis)
    # generated graphics
    plot_graphs((np.arange(users) / users) * 100, genre_cov[0], 'Users (%)',
                'Genre Coverage',
                output_file + 'genre-coverage-users.eps', 'Genre Coverage')

    fileout = open(output_file + "genre-coverage-unique-value.txt", 'w')
    fileout.write("%f" % (cov / users))
    print("GENRE COVERAGE : %f" % (cov / users))


def metric_serendipity(dic_u_training, dic_u_top, matrix_top_n, amount_n, users, file_feature, output_file):
    # settings output Directory
    output_directory = output_file + 'serendipity'

    # create output directory if it does not exist
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        print('error creating the folder in : %s' % output_directory)
        sys.exit(2)

    # settings output Directory
    output_file = output_directory + '/'

    # Load items information
    item_set = {}
    fin = open(file_feature, "r")
    fin.readline()
    for k in fin:
        k = k.rstrip()
        line = k.split(" ")
        item = line[0]
        if not item_set.get(item, False):
            item_set[item] = []
        item_set[item] = [int(j) for j in line[1:]]
    fin.close()

    ##################################################################################################
    # Calculating the auralist metric
    ##################################################################################################

    serendipity = []
    c_values = {}
    cont = 0
    for u in range(users):
        user = dic_u_top[u]
        unserendipity = 0
        for h in dic_u_training[user]:
            for i in matrix_top_n[u]:
                if item_set.get(i, False):
                    cont += 1
                    min_number, max_number = min_max(h, i)
                    if not c_values.get(min_number, False):
                        c_values[min_number] = {}
                    if not c_values[min_number].get(max_number, False):
                        c_values[min_number][max_number] = cossim(item_set[min_number], item_set[max_number]) / amount_n
                    unserendipity += c_values[min_number][max_number]
        unserendipity /= users * len(dic_u_training[user])
        if unserendipity == 0:
            serendipity.append(0)
        else:
            serendipity.append(1 / unserendipity)

    ##################################################################################################
    # Printing output
    ##################################################################################################

    # saves the values
    serendipity = np.array(serendipity, dtype=float)
    serendipity = np.sort(serendipity)[::-1]
    serendipity = serendipity / np.max(serendipity)

    f_out = open(output_file + "serendipity.txt", "w")
    for i in range(users):
        f_out.write("%d\t%f\n" % (i, serendipity[i]))

    # generated graphics
    plot_graphs((np.arange(users) / users) * 100, serendipity,
                'Users (%)', 'serendipity',
                output_file + 'serendipity.eps', 'Serendipity')


"""def business_metrics_old(dic_u_test, dic_i_test, dic_u_training, dic_i_training, dic_u_top, matrix_top_n,
                         matrix_ratings,
                         average_note_user, amount_n, users, output_file):
    # settings output Directory
    output_directory = output_file + 'businessMetrics'

    # create output directory if it does not exist
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        print('error creating the folder in : %s' % output_directory)
        sys.exit(2)

    # settings output Directory
    output_file = output_directory + '/'

    # calculates the diversity measures
    vector_analysis = np.zeros(users)
    dic_diversity = {}
    for i in range(users):
        vector_recommendations = matrix_top_n[i]
        for j, item_current in enumerate(vector_recommendations):
            vector_item_current = list(dic_i_training[item_current].keys())
            for k, item_others in enumerate(vector_recommendations):
                if item_current != item_others:
                    min_number, max_number = min_max(item_current, item_others)
                    if not dic_diversity.get(min_number, False):
                        dic_diversity[min_number] = {}
                    if not dic_diversity[min_number].get(max_number, False):
                        vector_item_others = list(dic_i_training[item_others].keys())
                        dic_diversity[min_number][max_number] = (
                            1 - jaccard_similarity(vector_item_current, vector_item_others))
                    vector_analysis[i] += dic_diversity[min_number][max_number]
                    # print('%d : %d : %d' % (i, j, k))
        vector_analysis[i] /= (amount_n * (amount_n - 1))
    print(vector_analysis)
    # sort the vector
    vector_analysis = np.sort(vector_analysis)[::-1]
    vector_analysis = np.array(vector_analysis).reshape(1, users)
    # saves the values
    matrix_analysis = np.concatenate(
        (np.transpose(np.arange(1, users + 1).reshape(1, users)),
         np.transpose(vector_analysis)), axis=1)
    np.savetxt(output_file + 'diversity-metric.txt', matrix_analysis)
    # generated graphics
    plot_graphs((np.arange(users) / users) * 100, vector_analysis[0],
                'Users (%)', 'diversity-metric',
                output_file + 'diversity-metric.png')"""


def intersection(A, B):
    result = []
    for n, m in enumerate(A):
        result.append((A[n] and B[n]))
    return result


def union(A, B):
    result = []
    for n, m in enumerate(A):
        result.append((A[n] or B[n]))
    return result


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)


def min_max(x, y):
    if x < y:
        return x, y
    else:
        return y, x


# Calculates the norm of the vector
def norm(a):
    return math.sqrt(sum([l * l for l in a]))


# Calculate the cosine similarity between two items.
# The calculus: cos(A,B) = (A*B)/(||A||*||B||).
# Dot product between A and B divided by the product of the norms of A and B.
def cossim(a, b):
    normAB = norm(a) * norm(b)
    if normAB == 0:
        return 0
    return sum([a[l] * b[l] for l in range(len(a))]) / normAB
