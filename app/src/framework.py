# -*- coding: utf-8 -*


import os
import sys
import pickle

from loadData import *
from featureExtraction import *
from qualityAnalysis import quality_analysis
from businessMetrics import *
from threading import Thread


def send_message(loader_window, status, text):
    loader_window.setStatus(status)
    loader_window.setText(text)


def run_send(loader_window, status, text):
    thread = Thread(target=send_message, args=(loader_window, status, text), daemon=True)
    thread.start()
    return thread


def runFramework(window, config):
    window.parameters = window.parameters.dic
    loader_window = window.loader_window

    # create output directory if it does not exist
    # noinspection PyBroadException
    output_directory = window.parameters['folder_output']
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    except:
        print(str(sys.exc_info()[0]))
        sys.exit(2)

    # setting output file
    output_file = output_directory + '/'
    output_root = output_file

    file_test = window.parameters['file_test']
    file_train = window.parameters['file_train']
    file_feature = window.parameters['file_feature']
    """file_test = 'src/input/ML-10M/ratings_test.txt'
    file_train = 'src/input/ML-10M/ratings_train.txt'
    file_top_n = 'src/recommendations/UserKNN/output/ML-10M/k=80/out.txt'
    file_feature = 'src/input/ML-10M/featuresItems.txt'
    amount_n = 100"""

    ############################################################################
    # LOAD TRAIN DATA
    ############################################################################
    dic_u_training = config['dic_u_training']
    dic_i_training = config['dic_i_training']
    amount_ratings = config['amount_ratings']
    del config['dic_u_training']
    del config['dic_i_training']
    del config['amount_ratings']

    # get the amount of users
    users = len(dic_u_training)
    items = len(dic_i_training)
    print("usuarios: %d" % users)
    print("itens: %d" % items)

    ############################################################################
    # FEATURES EXTRACTION
    ############################################################################
    if window.parameters['feature_extraction']:
        print("Domain Profiling")
        config['loader_weight'] += 2
        value = config['loader_weight'] * config['loader_value']
        text = 'Executing Domain Profiling'
        send_message(loader_window, value, text)
        average_note_user = feature_extraction(dic_u_training, dic_i_training, users, items, amount_ratings,
                                               output_file, window.parameters)
    else:
        if window.parameters['quality_analysis'] or window.parameters['catalog_coverage'] \
                or window.parameters['genre_coverage']:
            config['loader_weight'] += 2
            value = config['loader_weight'] * config['loader_value']
            text = 'Calculating Average Note User'
            send_message(loader_window, value, text)
            average_note_user = average_note_users(dic_u_training, users)

    ############################################################################
    # LOAD TEST
    ############################################################################
    # function from loadData where returns the data matrices
    if window.parameters['quality_analysis'] or window.parameters['catalog_coverage']:
        dic_u_test = config['dic_u_test']
        dic_i_test = config['dic_i_test']
        del config['dic_u_test']
        del config['dic_i_test']

    ############################################################################
    # LOAD  RATINGS DATA
    ############################################################################
    if window.parameters['quality_analysis'] or window.parameters['catalog_coverage'] \
            or window.parameters['serendipity'] or window.parameters['genre_coverage']:

        output_root = output_file
        for j in range(len(window.parameters['file_recommender'])):
            name_recommender = window.parameters['file_recommender'][j][0]
            file_top_n = window.parameters['file_recommender'][j][1]
            amount_n = int(window.parameters['file_recommender'][j][2])
            # settings output Directory
            output_directory = output_root + name_recommender

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

            # loader_window.set_process(1, name_recommender + ': Read Data Recommender')
            config['loader_weight'] += 1
            value = config['loader_weight'] * config['loader_value']
            text = name_recommender + ': Read Data Recommender'
            send_message(loader_window, value, text)
            if window.parameters['mymedialite']:
                dic_u_top, matrix_top_n, matrix_ratings = load_data_mymedialite(file_top_n)
            else:
                dic_u_top, matrix_top_n, matrix_ratings = load_data_topN(file_top_n)

            ############################################################################
            # QUALITY ANALYSIS
            ############################################################################
            if window.parameters['quality_analysis']:
                print(name_recommender + ": Effectiveness-based")
                config['loader_weight'] += 3
                value = config['loader_weight'] * config['loader_value']
                text = name_recommender + ': Executing Effectiveness-based'
                send_message(loader_window, value, text)
                quality_analysis(dic_u_test, dic_u_top, matrix_top_n,
                                 matrix_ratings, average_note_user, users, amount_n, output_file, window.parameters)

            ############################################################################
            # BUSINESS METRICS
            ############################################################################
            if window.parameters['diversity_novelty'] or window.parameters['catalog_coverage'] \
                    or window.parameters['serendipity'] or window.parameters['genre_coverage']:
                # settings output Directory
                output_directory = output_file + 'Complementary_Dimensions_of_Quality'

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

            if window.parameters['catalog_coverage']:
                print(name_recommender + ': catalog_coverage')
                config['loader_weight'] += 2
                value = config['loader_weight'] * config['loader_value']
                text = name_recommender + ': Executing Catalog Coverage'
                send_message(loader_window, value, text)
                catalog_coverage(dic_u_test, dic_u_top, matrix_top_n, average_note_user, amount_n, users, items,
                                 output_file)

            if window.parameters['serendipity']:
                print(name_recommender + ': metric_serendipity')
                config['loader_weight'] += 3
                value = config['loader_weight'] * config['loader_value']
                text = name_recommender + ': Executing Serendipity'
                send_message(loader_window, value, text)
                metric_serendipity(dic_u_training, dic_u_top, matrix_top_n, amount_n, users, file_feature, output_file)

            if window.parameters['genre_coverage']:
                print(name_recommender + ': genre_coverage')
                config['loader_weight'] += 2
                value = config['loader_weight'] * config['loader_value']
                text = name_recommender + ': Executing Genre Coverage'
                send_message(loader_window, value, text)
                genre_coverage(dic_u_training, matrix_top_n, average_note_user, users, amount_n, file_feature,
                               output_file)

    ############################################################################
    # FREE MEMORY
    ############################################################################
    del dic_u_training
    del dic_i_training
    if window.parameters['quality_analysis'] or window.parameters['catalog_coverage']:
        del dic_u_test
        del dic_i_test
    if window.parameters['quality_analysis'] or window.parameters['catalog_coverage'] \
            or window.parameters['serendipity'] or window.parameters['genre_coverage']:
        del dic_u_top
        del matrix_top_n
        del matrix_ratings

    if window.parameters['quality_analysis'] or window.parameters['catalog_coverage'] \
            or window.parameters['genre_coverage'] or window.parameters['feature_extraction']:
        del average_note_user

    ############################################################################
    # EXECUTING DIVERSITY AND NOVELTY FOR ALL RECOMMENDATIONS
    ############################################################################
    if window.parameters['diversity_novelty']:
        for j in range(len(window.parameters['file_recommender'])):
            name_recommender = window.parameters['file_recommender'][j][0]
            file_top_n = window.parameters['file_recommender'][j][1]
            amount_n = int(window.parameters['file_recommender'][j][2])

            # settings output Directory
            output_directory = output_root + name_recommender + '/Complementary_Dimensions_of_Quality'
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

            print(name_recommender + ': diversity_novelty_metrics')
            if window.parameters['mymedialite']:
                convert_file_mymedialite(file_top_n, output_file)
            config['loader_weight'] += 3
            value = config['loader_weight'] * config['loader_value']
            text = name_recommender + ': Executing Diversity and Novelty'
            send_message(loader_window, value, text)
            if window.parameters['mymedialite']:
                diversity_novelty_metrics(file_test,
                                          file_train,
                                          output_file + "file_mymedialite_topn.txt",
                                          users, amount_n, output_file)
                os.system("cd " + output_file + " && rm file_mymedialite_topn.txt")
            else:
                diversity_novelty_metrics(file_test,
                                          file_train,
                                          file_top_n,
                                          users, amount_n, output_file)

    # loader_window.finish_process()
    loader_window.setStatus(1.1)
    loader_window.setText('Finished')
    print('Finished')
    frame_path = os.popen("pwd").read().rstrip()

    with open(frame_path + '/list_file_recommender.txt', 'wb') as fp:
        pickle.dump(window.parameters['file_recommender'], fp)

    os.system("python3 %s %d %d %s %s %r %r %r %r %r %r %r %r" % (
        frame_path + "/src/outWindow.py",
        users,
        items,
        frame_path,
        window.parameters['folder_output'],
        window.parameters['feature_users'],
        window.parameters['feature_items'],
        window.parameters['mae_mse_accuracy'],
        window.parameters['precision_recall'],
        window.parameters['diversity_novelty'],
        window.parameters['genre_coverage'],
        window.parameters['catalog_coverage'],
        window.parameters['serendipity']
    ))
    window.loader_window.closeCallback()
