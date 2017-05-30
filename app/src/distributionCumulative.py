from __future__ import division
# -*- coding: utf-8 -*


import numpy as np

from plotGraphs import plot_graphs

def distribution_cumulative(precision, recall, users, output_file):

    # truncate to two decimal places
    round_p = np.round(precision * 100) / 100
    round_r = np.round(recall * 100) / 100

    # amount of values ​​less than or equal to the precision and the recall list
    dist_p = np.array(round_p, dtype=int)
    dist_r = np.array(dist_p)
    for i in range(users):
        dist_p[i] = np.size(np.where(round_p[1:] <= round_p[i]))
        dist_r[i] = np.size(np.where(round_r[1:] <= round_r[i]))

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
    file_precision = open(output_file + 'distributionPrecisionCumulative.txt', 'wt')
    file_recall = open(output_file + 'distributionRecallCumulative.txt', 'wt')
    for i in range(users):
        file_precision.write('%f \t %f \n' % (sort_p[i], dist_p_aux[i]))
        file_recall.write('%f \t %f \t \n' % (sort_r[i], dist_r_aux[i]))
    file_precision.close()
    file_recall.close()

    # generated graphics
    plot_graphs(sort_p, (dist_p_aux / users) * 100, 'Precision', 'Users (%)', output_file + 'distributionPrecisionCumulative.eps', 'Cumulative distribution')
    plot_graphs(sort_r, (dist_r_aux / users) * 100, 'Recall', 'Users (%)', output_file + 'distributionRecallCumulative.eps', 'Cumulative distribution')