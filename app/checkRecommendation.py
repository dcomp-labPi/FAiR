# -*- coding: utf-8 -*-
import os


def check_recommendation(recommendation_list, amount_n, window):
    # Get the recommender list
    if not os.path.isfile(recommendation_list):
        window.msgError('Sorry, but your file recommender ' + recommendation_list +
                        ' not exist')
        return False

    # Load recommendation information
    cont_lines = 0
    fin = open(recommendation_list, "r")
    RS = {}
    for i in fin:

        cont_lines += 1

        # check if the recommendation file is ok
        try:
            # reading
            i = i.rstrip()
            line = i.split(" ")
            user = line[0]

            # checking user
            if not RS.get(user, False):
                RS[user] = dict()

            # inserting all the items
            for j in line[1:]:
                RS[user][j.split(":")[0]] = float(j.split(":")[1])

            # check if the size of the recommendation is the same for all users.
            if len(line[1:]) < amount_n:
                window.msgError("Sorry, but your file \n" + recommendation_list +
                                " \nhave the number of recommendations lower than your amount of topN chosen")
                return False

        # if there is any problem with the recommdation file
        except:
            window.msgError('error in format of recommender file: %s' % recommendation_list)
            return False

    fin.close()

    if cont_lines == 0:
        window.msgError('error in format of recommender file: %s' % recommendation_list)
        return False

    # file is ok
    return True


def check_recommendation_mymedialite(recommendation_list, amount_n, window):
    # Get the recommender list
    if not os.path.isfile(recommendation_list):
        window.msgError('Sorry, but your file recommender ' + recommendation_list +
                        ' not exist')
        return False

    # Load recommendation information
    cont_lines = 0
    fin = open(recommendation_list, "r")
    RS = {}
    for i in fin:

        cont_lines += 1

        # check if the recommendation file is ok
        try:
            # reading
            i = i.rstrip()
            line = i.split("\t")
            user = line[0]
            items = line[1][1:]
            items = items[:-1].split(",")

            # checking user
            if not RS.get(user, False):
                RS[user] = dict()

            # inserting all the items
            for j in items:
                RS[user][j.split(":")[0]] = float(j.split(":")[1])

            # check if the size of the recommendation is the same for all users.
            if len(items) < amount_n:
                window.msgError("Sorry, but your file \n" + recommendation_list +
                                " \nhave the number of recommendations lower than your amount of topN chosen")
                return False

        # if there is any problem with the recommdation file
        except:
            window.msgError('error in format of recommender file: %s' % recommendation_list)
            return False

    fin.close()

    if cont_lines == 0:
        window.msgError('error in format of recommender file: %s' % recommendation_list)
        return False

    # file is ok
    return True
