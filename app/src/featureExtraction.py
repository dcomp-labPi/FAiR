# -*- coding: utf-8 -*
from __future__ import division


import os
import sys
import numpy as np
from collections import Counter

from plotGraphs import plot_graphs
from plotGraphs import plot_graphs_bar


def feature_extraction(dic_u_training, dic_i_training, users, items, amount_ratings, output_file, parameters):

    # settings output Directory
    output_directory = output_file + 'Domain Profiling'

    # create output directory if it does not exist
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        print('error creating the folder in : %s' % (output_directory))
        sys.exit(2)

    # settings output Directory
    output_file = output_directory + '/'

    ############################################################################
    #  Features of Items
    ############################################################################
    if parameters['feature_items']:
        # assembling the characterization groups
        # popularity of items
        historic = np.zeros(items)
        sum_ratings = np.array(historic)
        variance = np.empty(items)
        for i, v in enumerate(dic_i_training):
            historic[i] = len(dic_i_training[v].keys())
            vector_aux = []
            for j, w in enumerate(dic_i_training[v].keys()):
                sum_ratings[i] += dic_i_training[v][w]
                if dic_i_training[v][w] != 0:
                    vector_aux.append(dic_i_training[v][w])
            if len(vector_aux) != 0:
                variance[i] = np.var(vector_aux)
            else:
                variance[i] = 0
        vector_analysis = np.array(historic)
        vector_analysis = np.sort(vector_analysis)[::-1]
        vector_analysis = np.array(vector_analysis).reshape(1, items)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, items + 1).reshape(1, items)), np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'popularity.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(items) / items) * 100, (vector_analysis[0] / users) * 100, 'Items (%)', 'Users (%)',
                    output_file + 'popularity.eps', 'Popularity')

        # average note of items
        historic[historic == 0] = 1
        vector_analysis = sum_ratings / historic
        # sorts the elements
        vector_analysis = np.sort(vector_analysis)[::-1]
        vector_analysis = np.array(vector_analysis).reshape(1, items)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, items + 1).reshape(1, items)), np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'averageNote-items.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(items) / items) * 100, vector_analysis[0], 'Items (%)', 'Average note',
                    output_file + 'averageNote-items.eps', 'Average note items')

        # variance of note of items
        len_vector_analysis = np.size(variance)
        # sorts the elements
        variance = np.sort(variance)[::-1]
        variance = np.array(variance).reshape(1, len_vector_analysis)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_analysis + 1).reshape(1, len_vector_analysis)), np.transpose(variance)),
            axis=1)
        np.savetxt(output_file + 'variance-items.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(len_vector_analysis) / len_vector_analysis) * 100, variance[0], 'Items (%)',
                    'Variance notes',
                    output_file + 'variance-items.eps', 'Variance items')

    ############################################################################
    #  Features of Users
    ############################################################################
    average_note = None
    if parameters['feature_users']:
        # historic of user consumption
        historic = np.zeros(users)
        sum_ratings = np.array(historic)
        variance = np.empty(users)
        # ratings_no_zeros for calculate probability of ratings
        ratings_no_zeros = []
        for i, v in enumerate(dic_u_training):
            historic[i] = len(dic_u_training[v].keys())
            vector_aux = []
            for j, w in enumerate(dic_u_training[v].keys()):
                sum_ratings[i] += dic_u_training[v][w]
                if dic_u_training[v][w] != 0:
                    vector_aux.append(dic_u_training[v][w])
                    ratings_no_zeros.append(dic_u_training[v][w])
            if len(vector_aux) != 0:
                variance[i] = np.var(vector_aux)
            else:
                variance[i] = 0
        vector_analysis = np.array(historic)
        vector_analysis = np.sort(vector_analysis)[::-1]
        vector_analysis = np.array(vector_analysis).reshape(1, users)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, users + 1).reshape(1, users)), np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'historic.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(users) / users) * 100, (vector_analysis[0] / items) * 100, 'Users (%)', 'Items (%)',
                    output_file + 'historic.eps', 'Consumption history')

        # average note of user
        historic[historic == 0] = 1
        vector_analysis = sum_ratings / historic
        average_note = np.array(vector_analysis)
        # sorts the elements
        vector_analysis = np.sort(vector_analysis)[::-1]
        vector_analysis = np.array(vector_analysis).reshape(1, users)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, users + 1).reshape(1, users)), np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'averageNote-users.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(users) / users) * 100, vector_analysis[0], 'Users (%)', 'Average note',
                    output_file + 'averageNote-users.eps', 'Average note users')

        # variance of note of users
        len_vector_analysis = np.size(variance)
        # sorts the elements
        variance = np.sort(variance)[::-1]
        variance = np.array(variance).reshape(1, len_vector_analysis)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_analysis + 1).reshape(1, len_vector_analysis)), np.transpose(variance)),
            axis=1)
        np.savetxt(output_file + 'variance-users.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(len_vector_analysis) / len_vector_analysis) * 100, variance[0], 'Users (%)',
                    'Variance notes',
                    output_file + 'variance-users.eps', 'Variance note users')

        # probability of ratings
        vector_analysis = []
        vector_aux = []
        dic_counter_ratings = Counter(ratings_no_zeros)
        dic_counter_ratings_tmp = {}
        if len(dic_counter_ratings) <= 15:
            for i, j in enumerate(dic_counter_ratings):
                if j < 0:
                    floor = np.floor(j)
                else:
                    floor = np.trunc(j)
                rest = j - floor

                if 0.7 < rest < 1:
                    result = floor + 1
                elif 0 <= rest <= 0.3:
                    result = floor
                else:
                    result = floor + 0.5

                if j != floor:
                    if dic_counter_ratings_tmp.get(result, False):
                        dic_counter_ratings_tmp[result] += dic_counter_ratings[j]
                    else:
                        dic_counter_ratings_tmp[result] = dic_counter_ratings[j]
                else:
                    dic_counter_ratings_tmp[j] = dic_counter_ratings[j]
        else:
            for i, j in enumerate(dic_counter_ratings):
                if j < 0:
                    floor = np.floor(j)
                else:
                    floor = np.trunc(j)
                rest = j - floor

                if 0.5 <= rest < 1:
                    result = floor + 1
                else:
                    result = floor

                if j != floor:
                    if dic_counter_ratings_tmp.get(result, False):
                        dic_counter_ratings_tmp[result] += dic_counter_ratings[j]
                    else:
                        dic_counter_ratings_tmp[result] = dic_counter_ratings[j]
                else:
                    dic_counter_ratings_tmp[j] = dic_counter_ratings[j]

        for i, j in enumerate(dic_counter_ratings_tmp):
            vector_analysis.append(j)
            vector_aux.append(dic_counter_ratings[j])

        # saves the values
        file_out = open(output_file + 'probability_ratings.txt', 'w')
        len_vector_analysis = len(vector_analysis)
        for i in range(len_vector_analysis):
            file_out.write("%f\t%d\n" % (vector_analysis[i], vector_aux[i]))
            vector_aux[i] = (vector_aux[i] / amount_ratings) * 100
        file_out.close()

        # generated graphics
        plot_graphs_bar(vector_analysis, vector_aux, 'Ratings', 'Probability (%)',
                        output_file + 'probability_occurrence.eps', 'Probability occurrence')

        """for i in range(len(ratings_no_zeros)):
            if ratings_no_zeros[i] < 0:
                floor = np.floor(ratings_no_zeros[i])
            else:
                floor = np.trunc(ratings_no_zeros[i])
            rest = ratings_no_zeros[i] - floor

            if 0.7 < rest < 1:
                result = floor + 1
            elif 0 <= rest <= 0.3:
                result = floor
            else:
                result = floor + 0.5

            if result in vector_analysis:
                for j in range(len(vector_analysis)):
                    if vector_analysis[j] == result:
                        vector_aux[j] += 1
            else:
                vector_analysis.append(result)
                vector_aux.append(1)
                print(len(vector_analysis))

            if len(vector_analysis) > 15:
                exit_probability = True
                break

        if not exit_probability:
            # saves the values
            file_out = open(output_file + 'probability_ratings.txt', 'w')
            len_vector_analysis = len(vector_analysis)
            for i in range(len_vector_analysis):
                file_out.write("%f\t%d\n" % (vector_analysis[i], vector_aux[i]))
                vector_aux[i] = (vector_aux[i] / amount_ratings) * 100
            file_out.close()

            # generated graphics
            plot_graphs_bar(vector_analysis, vector_aux, 'Ratings', 'Probability (%)',
                            output_file + 'probability_occurrence.eps', 'Probability occurrence')"""
    else:
        if parameters['quality_analysis'] or parameters['catalog_coverage'] \
                or parameters['genre_coverage']:
            average_note = average_note_users(dic_u_training, users)

    return average_note


def average_note_users(dic_u_training, users):
    # historic of user consumption
    historic = np.zeros(users)
    sum_ratings = np.array(historic)
    for i, v in enumerate(dic_u_training):
        historic[i] = len(dic_u_training[v].keys())
        for j, w in enumerate(dic_u_training[v].keys()):
            sum_ratings[i] += dic_u_training[v][w]

    # average note of user
    historic[historic == 0] = 1
    vector_analysis = sum_ratings / historic
    average_note = np.array(vector_analysis)

    return average_note
