import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import subprocess, sys
import os
import pickle


class feature_window(Gtk.Window):
    def __init__(self, window, parameters):
        Gtk.Window.__init__(self, title="Data Feature Extraction")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_homogeneous(False)
        vbox.set_margin_top(30)
        vbox.set_margin_right(30)
        vbox.set_margin_bottom(30)
        vbox.set_margin_left(30)

        label = Gtk.Label("Data output from feature extraction")
        vbox.pack_start(label, True, True, 0)

        if parameters['feature_items']:
            # popularity of items
            label_popularity = Gtk.Label("Popularity")
            label_popularity.set_justify(Gtk.Justification.LEFT)
            label_popularity.set_size_request(200, 0)
            label_popularity.set_xalign(0)
            hbox_popularity = Gtk.Box(spacing=10)
            hbox_popularity.pack_start(label_popularity, True, True, 0)

            btn_popularity_g = Gtk.Button(label="View Graph")
            btn_popularity_g.set_size_request(100, 0)
            btn_popularity_g.connect("clicked", self.open_object,
                                     parameters['folder_output'] + '/featureExtraction/popularity.eps')
            hbox_popularity.pack_start(btn_popularity_g, True, True, 0)

            btn_popularity_t = Gtk.Button(label="View Text")
            btn_popularity_t.set_size_request(100, 0)
            btn_popularity_t.connect("clicked", self.open_object,
                                     parameters['folder_output'] + '/featureExtraction/popularity.txt')
            hbox_popularity.pack_start(btn_popularity_t, True, True, 0)
            vbox.pack_start(hbox_popularity, True, True, 0)

            # average note of items
            label_ani = Gtk.Label("Average note of items")
            label_ani.set_justify(Gtk.Justification.LEFT)
            label_ani.set_size_request(200, 0)
            label_ani.set_xalign(0)
            hbox_ani = Gtk.Box(spacing=10)
            hbox_ani.pack_start(label_ani, True, True, 0)

            button_ani_g = Gtk.Button(label="View Graph")
            button_ani_g.set_size_request(100, 0)
            button_ani_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/averageNote-items.eps')
            hbox_ani.pack_start(button_ani_g, True, True, 0)

            button_ani_t = Gtk.Button(label="View Text")
            button_ani_t.set_size_request(100, 0)
            button_ani_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/averageNote-items.txt')
            hbox_ani.pack_start(button_ani_t, True, True, 0)
            vbox.pack_start(hbox_ani, True, True, 0)

            # variance of item note
            label_vin = Gtk.Label("Variance of item note")
            label_vin.set_justify(Gtk.Justification.LEFT)
            label_vin.set_size_request(200, 0)
            label_vin.set_xalign(0)
            hbox_vin = Gtk.Box(spacing=10)
            hbox_vin.pack_start(label_vin, True, True, 0)

            button_vin_g = Gtk.Button(label="View Graph")
            button_vin_g.set_size_request(100, 0)
            button_vin_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/variance-items.eps')
            hbox_vin.pack_start(button_vin_g, True, True, 0)

            button_vin_t = Gtk.Button(label="View Text")
            button_vin_t.set_size_request(100, 0)
            button_vin_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/variance-items.txt')
            hbox_vin.pack_start(button_vin_t, True, True, 0)
            vbox.pack_start(hbox_vin, True, True, 0)

        if parameters['feature_users']:
            # Historic
            label_historic = Gtk.Label("Historic")
            label_historic.set_justify(Gtk.Justification.LEFT)
            label_historic.set_size_request(200, 0)
            label_historic.set_xalign(0)
            hbox_historic = Gtk.Box(spacing=10)
            hbox_historic.pack_start(label_historic, True, True, 0)

            button_historic_g = Gtk.Button(label="View Graph")
            button_historic_g.set_size_request(100, 0)
            button_historic_g.connect("clicked", self.open_object,
                                      parameters['folder_output'] + '/featureExtraction/historic.eps')
            hbox_historic.pack_start(button_historic_g, True, True, 0)

            button_historic_t = Gtk.Button(label="View Text")
            button_historic_t.set_size_request(100, 0)
            button_historic_t.connect("clicked", self.open_object,
                                      parameters['folder_output'] + '/featureExtraction/historic.txt')
            hbox_historic.pack_start(button_historic_t, True, True, 0)
            vbox.pack_start(hbox_historic, True, True, 0)

            # average note of users
            label_anu = Gtk.Label("Average note of users")
            label_anu.set_justify(Gtk.Justification.LEFT)
            label_anu.set_size_request(200, 0)
            label_anu.set_xalign(0)
            hbox_anu = Gtk.Box(spacing=10)
            hbox_anu.pack_start(label_anu, True, True, 0)

            button_anu_g = Gtk.Button(label="View Graph")
            button_anu_g.set_size_request(100, 0)
            button_anu_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/averageNote-users.eps')
            hbox_anu.pack_start(button_anu_g, True, True, 0)

            button_anu_t = Gtk.Button(label="View Text")
            button_anu_t.set_size_request(100, 0)
            button_anu_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/averageNote-users.txt')
            hbox_anu.pack_start(button_anu_t, True, True, 0)
            vbox.pack_start(hbox_anu, True, True, 0)

            # variance of user note
            label_vun = Gtk.Label("Variance of user note")
            label_vun.set_justify(Gtk.Justification.LEFT)
            label_vun.set_size_request(200, 0)
            label_vun.set_xalign(0)
            hbox_vun = Gtk.Box(spacing=10)
            hbox_vun.pack_start(label_vun, True, True, 0)

            button_vun_g = Gtk.Button(label="View Graph")
            button_vun_g.set_size_request(100, 0)
            button_vun_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/variance-users.eps')
            hbox_vun.pack_start(button_vun_g, True, True, 0)

            button_vun_t = Gtk.Button(label="View Text")
            button_vun_t.set_size_request(100, 0)
            button_vun_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + '/featureExtraction/variance-users.txt')
            hbox_vun.pack_start(button_vun_t, True, True, 0)
            vbox.pack_start(hbox_vun, True, True, 0)

            # probability of ratings
            label_pr = Gtk.Label("Probability of ratings")
            label_pr.set_justify(Gtk.Justification.LEFT)
            label_pr.set_size_request(200, 0)
            label_pr.set_xalign(0)
            hbox_pr = Gtk.Box(spacing=10)
            hbox_pr.pack_start(label_pr, True, True, 0)

            button_pr_g = Gtk.Button(label="View Graph")
            button_pr_g.set_size_request(100, 0)
            button_pr_g.connect("clicked", self.open_object,
                                parameters['folder_output'] + '/featureExtraction/probability_ratings.eps')
            hbox_pr.pack_start(button_pr_g, True, True, 0)

            button_pr_t = Gtk.Button(label="View Text")
            button_pr_t.set_size_request(100, 0)
            button_pr_t.connect("clicked", self.open_object,
                                parameters['folder_output'] + '/featureExtraction/probability_ratings.txt')
            hbox_pr.pack_start(button_pr_t, True, True, 0)
            vbox.pack_start(hbox_pr, True, True, 0)

        self.add(vbox)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def open_object(self, widget, object_path):
        try:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, object_path])
        except Exception:
            print('error in open: ' + object_path)


class quality_window(Gtk.Window):
    def __init__(self, window, parameters, name_recommender):
        Gtk.Window.__init__(self, title="Data Quality Analisys")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_homogeneous(False)
        vbox.set_margin_top(30)
        vbox.set_margin_right(30)
        vbox.set_margin_bottom(30)
        vbox.set_margin_left(30)

        label = Gtk.Label(name_recommender + " : Data output from quality analisys")
        vbox.pack_start(label, True, True, 0)

        if parameters['mae_mse_accuracy']:
            # mean absolute error
            label_mae = Gtk.Label("Mean absolute error")
            label_mae.set_justify(Gtk.Justification.LEFT)
            label_mae.set_size_request(260, 0)
            label_mae.set_xalign(0)
            hbox_mae = Gtk.Box(spacing=10)
            hbox_mae.pack_start(label_mae, True, True, 0)

            btn_mae_g = Gtk.Button(label="View Graph")
            btn_mae_g.set_size_request(100, 0)
            btn_mae_g.connect("clicked", self.open_object,
                              parameters['folder_output'] + "/" + name_recommender
                              + '/qualityAnalysis/mean-absolute-error.eps')
            hbox_mae.pack_start(btn_mae_g, True, True, 0)

            btn_mae_t = Gtk.Button(label="View Text")
            btn_mae_t.set_size_request(100, 0)
            btn_mae_t.connect("clicked", self.open_object,
                              parameters['folder_output'] + "/" + name_recommender
                              + '/qualityAnalysis/mean-absolute-error.txt')
            hbox_mae.pack_start(btn_mae_t, True, True, 0)
            vbox.pack_start(hbox_mae, True, True, 0)

            # root mean squared error
            label_rmse = Gtk.Label("Average note of items")
            label_rmse.set_justify(Gtk.Justification.LEFT)
            label_rmse.set_size_request(260, 0)
            label_rmse.set_xalign(0)
            hbox_rmse = Gtk.Box(spacing=10)
            hbox_rmse.pack_start(label_rmse, True, True, 0)

            button_rmse_g = Gtk.Button(label="View Graph")
            button_rmse_g.set_size_request(100, 0)
            button_rmse_g.connect("clicked", self.open_object,
                                  parameters['folder_output'] + "/" + name_recommender
                                  + '/qualityAnalysis/root-mean-squared-error.eps')
            hbox_rmse.pack_start(button_rmse_g, True, True, 0)

            button_rmse_t = Gtk.Button(label="View Text")
            button_rmse_t.set_size_request(100, 0)
            button_rmse_t.connect("clicked", self.open_object,
                                  parameters['folder_output'] + "/" + name_recommender
                                  + '/qualityAnalysis/root-mean-squared-error.txt')
            hbox_rmse.pack_start(button_rmse_t, True, True, 0)
            vbox.pack_start(hbox_rmse, True, True, 0)

            # accuracy
            label_accuracy = Gtk.Label("Accuracy")
            label_accuracy.set_justify(Gtk.Justification.LEFT)
            label_accuracy.set_size_request(260, 0)
            label_accuracy.set_xalign(0)
            hbox_accuracy = Gtk.Box(spacing=10)
            hbox_accuracy.pack_start(label_accuracy, True, True, 0)

            button_accuracy_g = Gtk.Button(label="View Graph")
            button_accuracy_g.set_size_request(100, 0)
            button_accuracy_g.connect("clicked", self.open_object,
                                      parameters['folder_output'] + "/" + name_recommender
                                      + '/qualityAnalysis/accuracy.eps')
            hbox_accuracy.pack_start(button_accuracy_g, True, True, 0)

            button_accuracy_t = Gtk.Button(label="View Text")
            button_accuracy_t.set_size_request(100, 0)
            button_accuracy_t.connect("clicked", self.open_object,
                                      parameters['folder_output'] + "/" + name_recommender
                                      + '/qualityAnalysis/accuracy.txt')
            hbox_accuracy.pack_start(button_accuracy_t, True, True, 0)
            vbox.pack_start(hbox_accuracy, True, True, 0)

        if parameters['precision_recall']:
            # Distribution Precision
            label_dp = Gtk.Label("Distribution precision")
            label_dp.set_justify(Gtk.Justification.LEFT)
            label_dp.set_size_request(260, 0)
            label_dp.set_xalign(0)
            hbox_dp = Gtk.Box(spacing=10)
            hbox_dp.pack_start(label_dp, True, True, 0)

            button_dp_g = Gtk.Button(label="View Graph")
            button_dp_g.set_size_request(100, 0)
            button_dp_g.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/distributionPrecision.eps')
            hbox_dp.pack_start(button_dp_g, True, True, 0)

            button_dp_t = Gtk.Button(label="View Text")
            button_dp_t.set_size_request(100, 0)
            button_dp_t.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/distributionPrecision.txt')
            hbox_dp.pack_start(button_dp_t, True, True, 0)
            vbox.pack_start(hbox_dp, True, True, 0)

            # Distribution Recall
            label_dr = Gtk.Label("Distribution recall")
            label_dr.set_justify(Gtk.Justification.LEFT)
            label_dr.set_size_request(260, 0)
            label_dr.set_xalign(0)
            hbox_dr = Gtk.Box(spacing=10)
            hbox_dr.pack_start(label_dr, True, True, 0)

            button_dr_g = Gtk.Button(label="View Graph")
            button_dr_g.set_size_request(100, 0)
            button_dr_g.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/distributionRecall.eps')
            hbox_dr.pack_start(button_dr_g, True, True, 0)

            button_dr_t = Gtk.Button(label="View Text")
            button_dr_t.set_size_request(100, 0)
            button_dr_t.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/distributionRecall.txt')
            hbox_dr.pack_start(button_dr_t, True, True, 0)
            vbox.pack_start(hbox_dr, True, True, 0)

            # Distribution Cumulative Precision
            label_dcp = Gtk.Label("Distribution cumulative precision")
            label_dcp.set_justify(Gtk.Justification.LEFT)
            label_dcp.set_size_request(260, 0)
            label_dcp.set_xalign(0)
            hbox_dcp = Gtk.Box(spacing=10)
            hbox_dcp.pack_start(label_dcp, True, True, 0)

            button_dcp_g = Gtk.Button(label="View Graph")
            button_dcp_g.set_size_request(100, 0)
            button_dcp_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + "/" + name_recommender
                                 + '/qualityAnalysis/distributionPrecisionCumulative.eps')
            hbox_dcp.pack_start(button_dcp_g, True, True, 0)

            button_dcp_t = Gtk.Button(label="View Text")
            button_dcp_t.set_size_request(100, 0)
            button_dcp_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + "/" + name_recommender
                                 + '/qualityAnalysis/distributionPrecisionCumulative.txt')
            hbox_dcp.pack_start(button_dcp_t, True, True, 0)
            vbox.pack_start(hbox_dcp, True, True, 0)

            # Distribution Recall
            label_dcr = Gtk.Label("Distribution cumulative recall")
            label_dcr.set_justify(Gtk.Justification.LEFT)
            label_dcr.set_size_request(260, 0)
            label_dcr.set_xalign(0)
            hbox_dcr = Gtk.Box(spacing=10)
            hbox_dcr.pack_start(label_dcr, True, True, 0)

            button_dcr_g = Gtk.Button(label="View Graph")
            button_dcr_g.set_size_request(100, 0)
            button_dcr_g.connect("clicked", self.open_object,
                                 parameters['folder_output'] + "/" + name_recommender
                                 + '/qualityAnalysis/distributionRecallCumulative.eps')
            hbox_dcr.pack_start(button_dcr_g, True, True, 0)

            button_dcr_t = Gtk.Button(label="View Text")
            button_dcr_t.set_size_request(100, 0)
            button_dcr_t.connect("clicked", self.open_object,
                                 parameters['folder_output'] + "/" + name_recommender
                                 + '/qualityAnalysis/distributionRecallCumulative.txt')
            hbox_dcr.pack_start(button_dcr_t, True, True, 0)
            vbox.pack_start(hbox_dcr, True, True, 0)

            # harmonic mean of precision and recall
            label_hmpr = Gtk.Label("Harmonic mean of precision and recall")
            label_hmpr.set_justify(Gtk.Justification.LEFT)
            label_hmpr.set_size_request(260, 0)
            label_hmpr.set_xalign(0)
            hbox_hmpr = Gtk.Box(spacing=10)
            hbox_hmpr.pack_start(label_hmpr, True, True, 0)

            button_hmpr_g = Gtk.Button(label="View Graph")
            button_hmpr_g.set_size_request(100, 0)
            button_hmpr_g.connect("clicked", self.open_object,
                                  parameters['folder_output'] + "/" + name_recommender
                                  + '/qualityAnalysis/harmonic-mean-precision-recall.eps')
            hbox_hmpr.pack_start(button_hmpr_g, True, True, 0)

            button_hmpr_t = Gtk.Button(label="View Text")
            button_hmpr_t.set_size_request(100, 0)
            button_hmpr_t.connect("clicked", self.open_object,
                                  parameters['folder_output'] + "/" + name_recommender
                                  + '/qualityAnalysis/harmonic-mean-precision-recall.txt')
            hbox_hmpr.pack_start(button_hmpr_t, True, True, 0)
            vbox.pack_start(hbox_hmpr, True, True, 0)

            # Average Precision
            label_ap = Gtk.Label("Average Precision")
            label_ap.set_justify(Gtk.Justification.LEFT)
            label_ap.set_size_request(260, 0)
            label_ap.set_xalign(0)
            hbox_ap = Gtk.Box(spacing=10)
            hbox_ap.pack_start(label_ap, True, True, 0)

            button_ap_g = Gtk.Button(label="View Graph")
            button_ap_g.set_size_request(100, 0)
            button_ap_g.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/average-precision.eps')
            hbox_ap.pack_start(button_ap_g, True, True, 0)

            button_ap_t = Gtk.Button(label="View Text")
            button_ap_t.set_size_request(100, 0)
            button_ap_t.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/qualityAnalysis/average-precision.txt')
            hbox_ap.pack_start(button_ap_t, True, True, 0)
            vbox.pack_start(hbox_ap, True, True, 0)

            # Mean average Precision
            label_map = Gtk.Label("Mean average Precision")
            label_map.set_justify(Gtk.Justification.LEFT)
            label_map.set_size_request(260, 0)
            label_map.set_xalign(0)
            hbox_map = Gtk.Box(spacing=10)
            hbox_map.pack_start(label_map, True, True, 0)

            try:
                file = open(parameters['folder_output'] + "/" + name_recommender
                            + '/qualityAnalysis/mean-average-precision.txt', 'r')
                value = file.readline()
            except Exception:
                value = 'open error'

            label_map_v = Gtk.Label(value)
            label_map_v.set_justify(Gtk.Justification.LEFT)
            label_map_v.set_size_request(260, 0)
            label_map_v.set_xalign(0.1)
            hbox_map.pack_start(label_map_v, True, True, 0)
            vbox.pack_start(hbox_map, True, True, 0)

        self.add(vbox)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def open_object(self, widget, object_path):
        try:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, object_path])
        except Exception:
            print('error in open: ' + object_path)


class business_window(Gtk.Window):
    def __init__(self, window, parameters, name_recommender):
        Gtk.Window.__init__(self, title="Data Business Metrics")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_homogeneous(False)
        vbox.set_margin_top(30)
        vbox.set_margin_right(30)
        vbox.set_margin_bottom(30)
        vbox.set_margin_left(30)

        label = Gtk.Label("REC" + " : Data output from business metrics")
        vbox.pack_start(label, True, True, 0)

        if parameters['diversity_novelty']:
            # Diversity
            label_diversity = Gtk.Label("Diversity")
            label_diversity.set_justify(Gtk.Justification.LEFT)
            label_diversity.set_size_request(200, 0)
            label_diversity.set_xalign(0)
            hbox_diversity = Gtk.Box(spacing=10)
            hbox_diversity.pack_start(label_diversity, True, True, 0)

            btn_diversity_g = Gtk.Button(label="View Graph")
            btn_diversity_g.set_size_request(100, 0)
            btn_diversity_g.connect("clicked", self.open_object,
                                    parameters['folder_output'] + "/" + name_recommender
                                    + '/businessMetrics/diversityNovelty/diversity.eps')
            hbox_diversity.pack_start(btn_diversity_g, True, True, 0)

            btn_diversity_t = Gtk.Button(label="View Text")
            btn_diversity_t.set_size_request(100, 0)
            btn_diversity_t.connect("clicked", self.open_object,
                                    parameters['folder_output'] + "/" + name_recommender
                                    + '/businessMetrics/diversityNovelty/diversity.txt')
            hbox_diversity.pack_start(btn_diversity_t, True, True, 0)
            vbox.pack_start(hbox_diversity, True, True, 0)

            # Novelty
            label_novelty = Gtk.Label("Novelty")
            label_novelty.set_justify(Gtk.Justification.LEFT)
            label_novelty.set_size_request(200, 0)
            label_novelty.set_xalign(0)
            hbox_novelty = Gtk.Box(spacing=10)
            hbox_novelty.pack_start(label_novelty, True, True, 0)

            button_novelty_g = Gtk.Button(label="View Graph")
            button_novelty_g.set_size_request(100, 0)
            button_novelty_g.connect("clicked", self.open_object,
                                     parameters['folder_output'] + "/" + name_recommender
                                     + '/businessMetrics/diversityNovelty/novelty.eps')
            hbox_novelty.pack_start(button_novelty_g, True, True, 0)

            button_novelty_t = Gtk.Button(label="View Text")
            button_novelty_t.set_size_request(100, 0)
            button_novelty_t.connect("clicked", self.open_object,
                                     parameters['folder_output'] + "/" + name_recommender
                                     + '/businessMetrics/diversityNovelty/novelty.txt')
            hbox_novelty.pack_start(button_novelty_t, True, True, 0)
            vbox.pack_start(hbox_novelty, True, True, 0)

        if parameters['serendipity']:
            # Serendipity
            label_serendipity = Gtk.Label("Serendipity")
            label_serendipity.set_justify(Gtk.Justification.LEFT)
            label_serendipity.set_size_request(200, 0)
            label_serendipity.set_xalign(0)
            hbox_serendipity = Gtk.Box(spacing=10)
            hbox_serendipity.pack_start(label_serendipity, True, True, 0)

            button_serendipity_g = Gtk.Button(label="View Graph")
            button_serendipity_g.set_size_request(100, 0)
            button_serendipity_g.connect("clicked", self.open_object,
                                         parameters['folder_output'] + "/" + name_recommender
                                         + '/businessMetrics/serendipity/serendipity.eps')
            hbox_serendipity.pack_start(button_serendipity_g, True, True, 0)

            button_serendipity_t = Gtk.Button(label="View Text")
            button_serendipity_t.set_size_request(100, 0)
            button_serendipity_t.connect("clicked", self.open_object,
                                         parameters['folder_output'] + "/" + name_recommender
                                         + '/businessMetrics/serendipity/serendipity.txt')
            hbox_serendipity.pack_start(button_serendipity_t, True, True, 0)
            vbox.pack_start(hbox_serendipity, True, True, 0)

        if parameters['catalog_coverage']:
            # Catalog coverage
            label_cc = Gtk.Label("Catalog coverage")
            label_cc.set_justify(Gtk.Justification.LEFT)
            label_cc.set_size_request(265, 0)
            label_cc.set_xalign(0)
            hbox_cc = Gtk.Box(spacing=10)
            hbox_cc.pack_start(label_cc, True, True, 0)

            try:
                file = open(parameters['folder_output'] + "/" + name_recommender
                            + '/businessMetrics/catalog-coverage.txt', 'r')
                value = file.readline()
            except Exception:
                value = 'open error'

            label_cc_v = Gtk.Label(value)
            label_cc_v.set_justify(Gtk.Justification.LEFT)
            label_cc_v.set_size_request(370, 0)
            label_cc_v.set_xalign(0.1)
            hbox_cc.pack_start(label_cc_v, True, True, 0)
            vbox.pack_start(hbox_cc, True, True, 0)

        if parameters['genre_coverage']:
            # Genre coverage
            label_gc = Gtk.Label("Genre coverage")
            label_gc.set_justify(Gtk.Justification.LEFT)
            label_gc.set_size_request(200, 0)
            label_gc.set_xalign(0)
            hbox_gc = Gtk.Box(spacing=10)
            hbox_gc.pack_start(label_gc, True, True, 0)

            try:
                file = open(parameters['folder_output'] + "/" + name_recommender
                            + '/businessMetrics/genreCoverage/genre-coverage-unique-value.txt', 'r')
                value = file.readline()
            except Exception:
                value = 'open error'

            label_gc_v = Gtk.Label(value)
            label_gc_v.set_justify(Gtk.Justification.LEFT)
            # label_gc_v.set_size_request(260, 0)
            label_gc_v.set_xalign(0.1)
            hbox_gc.pack_start(label_gc_v, True, True, 0)

            button_gc_g = Gtk.Button(label="View Graph")
            button_gc_g.set_size_request(100, 0)
            button_gc_g.connect("clicked", self.open_object,
                                parameters['folder_output'] + "/" + name_recommender
                                + '/businessMetrics/genreCoverage/genre-coverage-users.eps')
            hbox_gc.pack_start(button_gc_g, True, True, 0)
            vbox.pack_start(hbox_gc, True, True, 0)

        self.add(vbox)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def open_object(self, widget, object_path):
        try:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, object_path])
        except Exception:
            print('error in open: ' + object_path)


class Window(Gtk.Window):
    def __init__(self, users, items, parameters):
        Gtk.Window.__init__(self, title="Data Output")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_homogeneous(False)
        vbox.set_margin_top(30)
        vbox.set_margin_right(30)
        vbox.set_margin_bottom(30)
        vbox.set_margin_left(30)

        label = Gtk.Label("Data output of framework")
        vbox.pack_start(label, True, True, 0)

        label = Gtk.Label("Users : " + users)
        label.set_margin_top(20)
        label.set_xalign(0)
        vbox.pack_start(label, True, True, 0)

        label = Gtk.Label("Items : " + items)
        label.set_xalign(0)
        vbox.pack_start(label, True, True, 0)

        if parameters['feature_users'] or parameters['feature_items']:
            label = Gtk.Label("Feature Extraction")
            label.set_margin_top(20)
            label.set_xalign(0)
            label.set_yalign(0.5)
            label.set_size_request(200, 0)
            hbox_f_extraction = Gtk.Box(spacing=10)
            hbox_f_extraction.pack_start(label, True, True, 0)

            button_f_extraction = Gtk.Button(label="View Data")
            button_f_extraction.set_size_request(100, 0)
            button_f_extraction.connect("clicked", self.call_window, 'button_f_extraction')
            hbox_f_extraction.pack_start(button_f_extraction, True, True, 0)
            vbox.pack_start(hbox_f_extraction, True, True, 0)

        if parameters['mae_mse_accuracy'] or parameters['precision_recall'] or parameters['diversity_novelty'] \
                or parameters['genre_coverage'] or parameters['catalog_coverage'] or parameters['serendipity']:
            for j in range(len(parameters['file_recommender'])):
                name_recommender = parameters['file_recommender'][j][0]
                # file_top_n = self.parameters.dic['file_recommender'][j][1]
                # amount_n = int(self.parameters.dic['file_recommender'][j][2])

                label = Gtk.Label(name_recommender)
                label.set_margin_top(20)
                label.set_xalign(0)
                vbox.pack_start(label, True, True, 0)

                if parameters['mae_mse_accuracy'] or parameters['precision_recall']:

                    label = Gtk.Label("Quality Analisys")
                    label.set_xalign(0.1)
                    label.set_size_request(200, 0)
                    hbox_q_analisys = Gtk.Box(spacing=10)
                    hbox_q_analisys.pack_start(label, True, True, 0)

                    button_q_analisys = Gtk.Button(label="View Data")
                    button_q_analisys.set_size_request(100, 0)
                    button_q_analisys.connect("clicked", self.call_window, 'button_q_analisys', name_recommender)
                    hbox_q_analisys.pack_start(button_q_analisys, True, True, 0)
                    vbox.pack_start(hbox_q_analisys, True, True, 0)

                if parameters['diversity_novelty'] or parameters['genre_coverage'] or parameters['catalog_coverage'] \
                        or parameters['serendipity']:

                    label = Gtk.Label("Business Metrics")
                    label.set_xalign(0.1)
                    label.set_size_request(200, 0)
                    hbox_b_metrics = Gtk.Box(spacing=10)
                    hbox_b_metrics.pack_start(label, True, True, 0)

                    button_b_metrics = Gtk.Button(label="View Data")
                    button_b_metrics.set_size_request(100, 0)
                    button_b_metrics.connect("clicked", self.call_window, 'button_b_metrics', name_recommender)
                    hbox_b_metrics.pack_start(button_b_metrics, True, True, 0)
                    vbox.pack_start(hbox_b_metrics, True, True, 0)

        label = Gtk.Label("PS: Your data were also saved on the output path")
        label.set_margin_top(20)
        vbox.pack_start(label, True, True, 0)

        self.add(vbox)
        self.set_position(Gtk.WindowPosition.CENTER)

    def call_window(self, widget, button, name_recommender=None):
        if button == "button_f_extraction":
            window = feature_window(self, parameters)
        elif button == "button_q_analisys":
            window = quality_window(self, parameters, name_recommender)
        elif button == "button_b_metrics":
            window = business_window(self, parameters, name_recommender)
        else:
            print(button + " button does not exist")


def cast_boolean(value):
    if value == "True":
        return True
    else:
        return False


users = sys.argv[1]
items = sys.argv[2]
parameters = {}
parameters['frame_path'] = sys.argv[3]

with open(parameters['frame_path'] + '/list_file_recommender.txt', 'rb') as fp:
    parameters['file_recommender'] = pickle.load(fp)
os.system("cd " + parameters['frame_path'] + " && rm list_file_recommender.txt")

parameters['folder_output'] = sys.argv[4]
parameters['feature_users'] = cast_boolean(sys.argv[5])
parameters['feature_items'] = cast_boolean(sys.argv[6])
parameters['mae_mse_accuracy'] = cast_boolean(sys.argv[7])
parameters['precision_recall'] = cast_boolean(sys.argv[8])
parameters['diversity_novelty'] = cast_boolean(sys.argv[9])
parameters['genre_coverage'] = cast_boolean(sys.argv[10])
parameters['catalog_coverage'] = cast_boolean(sys.argv[11])
parameters['serendipity'] = cast_boolean(sys.argv[12])

window = Window(users, items, parameters)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
