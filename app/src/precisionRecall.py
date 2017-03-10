# -*- coding: utf-8 -*
from __future__ import division


import numpy as np


def precision_recall(dic_u_test, vector_top_n, average_note_user, amount_n, i):
    nrs = 0  # Selected items and relevant
    # ns - all selected items
    # nr - all relevant items
    # nm_users - average grade
    average_precision = 0

    # set line the items for this user
    vector_test_line_items = np.empty(len(dic_u_test[i]))
    for j, w in enumerate(dic_u_test[i].keys()):
        vector_test_line_items[j] = dic_u_test[i][w]

    # number of relevant items in the test base for this user
    nr = np.size(np.where(vector_test_line_items >= average_note_user))

    # number of selected items in the topN for this user
    ns = amount_n

    # number of relevant items in the set topN
    for j in range(amount_n):
        if dic_u_test[i].get(vector_top_n[j], False) >= average_note_user:
            nrs += 1
            # manipulations for average precision
            average_precision += nrs / (j + 1)

    # calculate the precision, recall and average
    if ns == 0:
        precision = 0
    else:
        precision = nrs / ns
    if nr == 0:
        recall = 0
    else:
        recall = nrs / nr
    if nrs == 0:
        average_precision /= 1
    else:
        average_precision /= nrs

    # returns precision and recall
    return precision, recall, average_precision
