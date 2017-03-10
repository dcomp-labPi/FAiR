# -*- coding: utf-8 -*
from __future__ import division


import numpy as np

from plotGraphs import plot_graphs


def distribution_pr(precision, recall, users, output_file):
    # truncate to two decimal places
    round_p = np.round(precision * 100) / 100
    round_r = np.round(recall * 100) / 100

    # amount of times the precision and recall occurs in the list
    dist_p = np.array(round_p, dtype=int)
    dist_r = np.array(dist_p)
    for i in range(users):
        dist_p[i] = np.size(np.where(round_p == round_p[i]))
        dist_r[i] = np.size(np.where(round_r == round_r[i]))

    # normalizes for amount the users
    dist_p = dist_p / users
    dist_r = dist_r / users

    # get the indexes of the sorted roundPR
    pos_p = np.argsort(round_p)
    pos_r = np.argsort(round_r)
    # sorts the elements in order of probability
    sort_p = np.array(round_p)
    sort_r = np.array(round_r)
    dist_p_aux = np.array(dist_p)
    dist_r_aux = np.array(dist_r)
    for i in range(users):
        sort_p[i] = round_p[pos_p[i]]
        sort_r[i] = round_r[pos_r[i]]
        dist_p_aux[i] = dist_p[pos_p[i]]
        dist_r_aux[i] = dist_r[pos_r[i]]

    # saved to a file generated rank
    file_precision = open(output_file + 'distributionPrecision.txt', 'wt')
    file_recall = open(output_file + 'distributionRecall.txt', 'wt')
    for i in range(users):
        file_precision.write('%f \t %f \n' % (sort_p[i], dist_p_aux[i]))
        file_recall.write('%f \t %f \t \n' % (sort_r[i], dist_r_aux[i]))
    file_precision.close()
    file_recall.close()

    # generated graphics
    plot_graphs(sort_p, dist_p_aux * 100, 'Precision', 'Probability of Occurrence (%)',
                output_file + 'distributionPrecision.eps', 'Distribution Precision')
    plot_graphs(sort_r, dist_r_aux * 100, 'Recall', 'Probability of Occurrence (%)',
                output_file + 'distributionRecall.eps', 'Distribution Recall')
