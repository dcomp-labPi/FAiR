# -*- coding: utf-8 -*
from __future__ import division


import numpy as np
import os
import sys

from plotGraphs import plot_graphs
from precisionRecall import precision_recall
from distributionPR import distribution_pr
from distributionCumulative import distribution_cumulative


def quality_analysis(dic_u_test,  dic_u_top, matrix_top_n, matrix_ratings,
                     average_note_user, users, amount_n, output_file, parameters):

    # settings output Directory
    output_directory = output_file + 'Effectiveness-based'

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

    if parameters['mae_mse_accuracy']:
        ############################################################################
        # calculates HITS, MAE and RMSE
        # MAE: mean absolute error and RMSE: root mean squared error
        ############################################################################
        vector_analysis = np.zeros(users)
        vector_analysis_RMSE = np.zeros(users)
        vector_hits = np.zeros(users)
        for i in range(users):
            mae_value = 0
            rmse_value = 0
            amount_items = 0
            for j in range(amount_n):
                id_item = matrix_top_n[i][j]
                id_user = dic_u_top[i]
                ri_rating = matrix_ratings[i][j]
                r_rating = 0
                if dic_u_test.get(id_user, False):
                    if dic_u_test[id_user].get(id_item, False):
                        r_rating = dic_u_test[id_user][id_item]
                if r_rating != 0:
                    amount_items += 1
                    mae_value += np.absolute((ri_rating - r_rating))
                    rmse_value += (ri_rating - r_rating) * (ri_rating - r_rating)
            # vector_hits get the amount of user items consumptions
            vector_hits[i] = amount_items
            if amount_items == 0:
                vector_analysis[i] = 0
                vector_analysis_RMSE[i] = 0
            else:
                vector_analysis[i] = mae_value / amount_items
                vector_analysis_RMSE[i] = np.sqrt((rmse_value / amount_items))
        # sorted the elements
        vector_analysis = np.sort(vector_analysis)
        vector_analysis_RMSE = np.sort(vector_analysis_RMSE)
        vector_hits = np.sort(vector_hits)[::-1]
        # remove users with values equals the zero
        vector_analysis = vector_analysis[vector_analysis != 0]
        vector_analysis_RMSE = vector_analysis_RMSE[vector_analysis_RMSE != 0]
        # calculates the size of vectors
        len_vector_analysis = np.size(vector_analysis)
        len_vector_analysis_RMSE = np.size(vector_analysis_RMSE)
        len_vector_hits = np.size(vector_hits)
        vector_analysis = np.array(vector_analysis).reshape(1, len_vector_analysis)
        vector_analysis_RMSE = np.array(vector_analysis_RMSE).reshape(1, len_vector_analysis_RMSE)
        vector_hits = np.array(vector_hits).reshape(1, len_vector_hits)
        # saves the values of MAE
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_analysis + 1).reshape(1, len_vector_analysis)),
             np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'mean-absolute-error.txt', matrix_analysis)
        # generated graphics of MAE
        plot_graphs((np.arange(len_vector_analysis) / len_vector_analysis) * 100, vector_analysis[0], 'Users (%)',
                    'MAE',
                    output_file + 'mean-absolute-error.eps', 'mean absolute error')
        # saves the values of RMSE
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_analysis_RMSE + 1).reshape(1, len_vector_analysis_RMSE)),
             np.transpose(vector_analysis_RMSE)), axis=1)
        np.savetxt(output_file + 'root-mean-squared-error.txt', matrix_analysis)
        # generated graphics of RMSE
        plot_graphs((np.arange(len_vector_analysis_RMSE) / len_vector_analysis_RMSE) * 100, vector_analysis_RMSE[0],
                    'Users (%)', 'RMSE',
                    output_file + 'root-mean-squared-error.eps', 'root mean squared error')
        # saves the hits values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_hits+ 1).reshape(1, len_vector_hits)),
             np.transpose(vector_hits)), axis=1)
        np.savetxt(output_file + 'accuracy.txt', matrix_analysis)
        # generated graphics of Hits
        plot_graphs((np.arange(len_vector_hits) / len_vector_hits) * 100, vector_hits[0], 'Users (%)',
                    'Accuracy',
                    output_file + 'accuracy.eps', 'Accuracy')

    if parameters['precision_recall']:
        ############################################################################
        # calculate the precision and recall values for all users
        ############################################################################
        precision = np.zeros(users)
        recall = np.array(precision)
        average_precision = np.array(precision)
        for i in range(users):
            (precision[i], recall[i], average_precision[i]) = precision_recall(dic_u_test, matrix_top_n[i],
                                                                               average_note_user[dic_u_top[i]], amount_n,
                                                                               dic_u_top[i])

        ############################################################################
        #  probability distribution of occurrence of precision and recall
        ############################################################################
        distribution_pr(precision, recall, users, output_file)
        # cumulative distribution of precision and recall
        distribution_cumulative(precision, recall, users, output_file)


        ############################################################################
        # calculate harmonic mean of precision and recall
        ############################################################################
        vector_analysis = np.zeros(users)
        for k in range(users):
            if (precision[k] + recall[k]) == 0:
                vector_analysis[k] = (2 * precision[k] + recall[k]) / 1
            else:
                vector_analysis[k] = (2 * precision[k] + recall[k]) / (precision[k] + recall[k])
        vector_analysis = np.array(vector_analysis[np.invert(np.isnan(vector_analysis))])
        # sort the vector
        vector_analysis = np.sort(vector_analysis)[::-1]
        len_vector_analysis = np.size(vector_analysis)
        vector_analysis = np.array(vector_analysis).reshape(1, len_vector_analysis)
        # saves the values of harmonic mean of precision and recall
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, len_vector_analysis + 1).reshape(1, len_vector_analysis)),
             np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'harmonic-mean-precision-recall.txt', matrix_analysis)
        # generated graphics of harmonic mean of precision and recall
        plot_graphs((np.arange(len_vector_analysis) / len_vector_analysis) * 100, vector_analysis[0],
                    'Users (%)', 'harmonic mean',
                    output_file + 'harmonic-mean-precision-recall.eps', 'harmonic mean precision recall')


        ############################################################################
        # calculate the average precision and MAP: mean average precision
        ############################################################################
        # sort the vector
        vector_analysis = np.sort(average_precision)[::-1]
        vector_analysis = np.array(vector_analysis).reshape(1, users)
        # saves the values
        matrix_analysis = np.concatenate(
            (np.transpose(np.arange(1, users + 1).reshape(1, users)),
             np.transpose(vector_analysis)), axis=1)
        np.savetxt(output_file + 'average-precision.txt', matrix_analysis)
        # generated graphics
        plot_graphs((np.arange(users) / users) * 100, vector_analysis[0],
                    'Users (%)', 'average precision',
                    output_file + 'average-precision.eps', 'Average precision')
        # MAP
        fileout = open(output_file + "mean-average-precision.txt", 'w')
        fileout.write("%f" % (np.sum(vector_analysis) / users))
        print("mean average precision: %f" % (np.sum(vector_analysis) / users))
