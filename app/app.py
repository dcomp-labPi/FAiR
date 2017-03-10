# -*- coding: utf-8 -*-
from gi import require_version

require_version('Gtk', '3.0')
from gi.repository import Gtk

import signal
import sys
import os
import threading

import fileChooser
import windows
import parameters
from checkRecommendation import *

sys.path.insert(0, 'src')
from framework import runFramework
from loadData import *
from calcLoader import CalcLoader


class App(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("app.glade")

        self.win = builder.get_object("window")
        self.loader_window = None

        # builders
        self.fChooser = fileChooser.FileChooserWindow()
        self.parameters = parameters.parameters()

        # set action Next
        self.notebook = builder.get_object("notebook")
        btnNext = builder.get_object("btnNext")
        btnNext.connect("clicked", self.setCurrentPage)

        ############################################################################
        ### CHOOSER FILE
        ############################################################################

        # set action checkbox mymedialite format
        self.chkMymedialite = builder.get_object("chkMymedialite")

        # set action Train File Chooser
        self.lbTrainFile = builder.get_object("lbTrainFile")
        btnTrainFile = builder.get_object("btnTrainFile")
        btnTrainFile.connect("clicked", self.fChooser.on_file_clicked, self.lbTrainFile, self, 'file_train')

        # set action Test File Chooser
        self.lbTestFile = builder.get_object("lbTestFile")
        btnTestFile = builder.get_object("btnTestFile")
        btnTestFile.connect("clicked", self.fChooser.on_file_clicked, self.lbTestFile, self, 'file_test')

        # set action Feature File Chooser
        self.lbFeatureFile = builder.get_object("lbFeatureFile")
        btnFeatureFile = builder.get_object("btnFeatureFile")
        btnFeatureFile.connect("clicked", self.fChooser.on_file_clicked, self.lbFeatureFile, self, 'file_feature')

        # set action Recommender File Chooser
        self.lbRecommenderFile = None
        btnRecommenderFile = builder.get_object("btnRecommenderFile")
        btnRecommenderFile.connect("clicked", self.fChooser.on_file_clicked, self.lbRecommenderFile, self,
                                   'file_recommender')

        # set action Output Foder Chooser
        self.lbOutputFolder = builder.get_object("lbOutputFolder")
        btnOutputFolder = builder.get_object("btnOutputFolder")
        btnOutputFolder.connect("clicked", self.fChooser.on_folder_clicked, self.lbOutputFolder, self.parameters,
                                'folder_output')

        ############################################################################
        ### WINDOW CHOICE METRICS
        ############################################################################
        # set action checkbox Feature Extraction
        # self.chkFeatureExtraction = builder.get_object("chkFeatureExtraction")
        self.chkEnableFeatureExtraction = builder.get_object("chkEnableFeatureExtraction")
        self.chkFeatureUsers = builder.get_object("chkFeatureUsers")
        self.chkFeatureItems = builder.get_object("chkFeatureItems")

        self.enableFeatureExtraction_toggled(self.chkEnableFeatureExtraction)
        # set action of checkbox
        self.chkEnableFeatureExtraction.connect("toggled", self.enableFeatureExtraction_toggled)

        # set config initial of checkboxes Quality Analysis
        self.chkEnableQualityAnalysis = builder.get_object("chkEnableQualityAnalysis")
        self.chkMaeAccuracy = builder.get_object("chkMaeAccuracy")
        self.chkPrecisionRecall = builder.get_object("chkPrecisionRecall")

        self.enableQualityAnalysis_toggled(self.chkEnableQualityAnalysis)
        # set action of checkbox
        self.chkEnableQualityAnalysis.connect("toggled", self.enableQualityAnalysis_toggled)

        # set config initial of checkboxes Business Metrics
        self.chkEnableBusinessMetrics = builder.get_object("chkEnableBusinessMetrics")
        self.chkDiversityNovelty = builder.get_object("chkDiversityNovelty")
        self.chkGenreCoverage = builder.get_object("chkGenreCoverage")
        self.chkCatalogCoverage = builder.get_object("chkCatalogCoverage")
        self.chkSerendipity = builder.get_object("chkSerendipity")

        self.enableBusinessMetrics_toggled(self.chkEnableBusinessMetrics)
        # set action of checkbox
        self.chkEnableBusinessMetrics.connect("toggled", self.enableBusinessMetrics_toggled)

        # set action Run button
        btnRun = builder.get_object("btnRun")
        btnRun.connect("clicked", self.callRun)

        ############################################################################
        ### WINDOW INFO
        ############################################################################
        btnInfo = builder.get_object("btnInfo")
        btnInfo.connect("clicked", self.callWindow)

        ############################################################################
        ### WINDOW GENERATE TRAIN TEST
        ############################################################################
        btnGenerateTrainTest = builder.get_object("btnGenerateTrainTest")
        btnGenerateTrainTest.connect("clicked", self.callWindow)

        ############################################################################
        ### WINDOW FEATURE TEST
        ############################################################################
        btnGenerateFeature = builder.get_object("btnGenerateFeature")
        btnGenerateFeature.connect("clicked", self.callWindow)

        ############################################################################
        # TABLE THE RECOMMENDER FILES
        ############################################################################
        self.liststore = builder.get_object("liststore")
        self.editText = builder.get_object("cellrenderertextedit")
        self.editText.set_property("editable", True)
        self.editText.connect("edited", self.text_edited)

        self.editTextTopN = builder.get_object("cellrendertopn")
        self.editTextTopN.set_property("editable", True)
        self.editTextTopN.connect("edited", self.text_edited_topN)

        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()
        Gtk.main()

    def setValuesTable(self, name, path, amount_n):
        self.liststore.append([name, path, amount_n])

    def getValuesTable(self):
        values = []
        value = self.liststore.get_iter_first()
        while value is not None:
            aux = [self.liststore.get_value(value, 0), self.liststore.get_value(value, 1),
                   self.liststore.get_value(value, 2)]
            values.append(aux)
            value = self.liststore.iter_next(value)
        return values

    def text_edited(self, widget, path, text):
        self.liststore[path][0] = text

    def text_edited_topN(self, widget, path, text):
        self.liststore[path][2] = int(text)

    def setCurrentPage(self, widget):
        self.notebook.set_current_page(1)

    def enableBusinessMetrics_toggled(self, checkbox):
        if checkbox.get_active():
            self.chkDiversityNovelty.set_sensitive(True)
            self.chkGenreCoverage.set_sensitive(True)
            self.chkCatalogCoverage.set_sensitive(True)
            self.chkSerendipity.set_sensitive(True)
        else:
            self.chkDiversityNovelty.set_sensitive(False)
            self.chkGenreCoverage.set_sensitive(False)
            self.chkCatalogCoverage.set_sensitive(False)
            self.chkSerendipity.set_sensitive(False)

    def enableFeatureExtraction_toggled(self, checkbox):
        if checkbox.get_active():
            self.chkFeatureUsers.set_sensitive(True)
            self.chkFeatureItems.set_sensitive(True)
        else:
            self.chkFeatureUsers.set_sensitive(False)
            self.chkFeatureItems.set_sensitive(False)

    def enableQualityAnalysis_toggled(self, checkbox):
        if checkbox.get_active():
            self.chkMaeAccuracy.set_sensitive(True)
            self.chkPrecisionRecall.set_sensitive(True)
        else:
            self.chkMaeAccuracy.set_sensitive(False)
            self.chkPrecisionRecall.set_sensitive(False)

    def callWindow(self, widget):
        if Gtk.Buildable.get_name(widget) == "btnInfo":
            window = windows.infoWindow(self)
        elif Gtk.Buildable.get_name(widget) == "btnGenerateTrainTest":
            window = windows.generateTrainTestWindow(self)
        elif Gtk.Buildable.get_name(widget) == "btnGenerateFeature":
            window = windows.generateFeatureWindow(self)
        else:
            print(Gtk.Buildable.get_name(widget) + " button does not exist")

    def callRun(self, widget):
        # get parameters
        self.parameters.dic['mymedialite'] = self.chkMymedialite.get_active()
        self.parameters.dic['feature_extraction'] = (self.chkFeatureUsers.get_active()
                                                     or self.chkFeatureItems.get_active())
        self.parameters.dic['feature_users'] = self.chkFeatureUsers.get_active()
        self.parameters.dic['feature_items'] = self.chkFeatureItems.get_active()
        self.parameters.dic['quality_analysis'] = (self.chkMaeAccuracy.get_active()
                                                   or self.chkPrecisionRecall.get_active())
        self.parameters.dic['mae_mse_accuracy'] = self.chkMaeAccuracy.get_active()
        self.parameters.dic['precision_recall'] = self.chkPrecisionRecall.get_active()
        self.parameters.dic['diversity_novelty'] = self.chkDiversityNovelty.get_active()
        self.parameters.dic['genre_coverage'] = self.chkGenreCoverage.get_active()
        self.parameters.dic['catalog_coverage'] = self.chkCatalogCoverage.get_active()
        self.parameters.dic['serendipity'] = self.chkSerendipity.get_active()

        # check data
        if not (self.parameters.dic['feature_extraction'] or self.parameters.dic['quality_analysis']
                or self.parameters.dic['diversity_novelty'] or self.parameters.dic['genre_coverage']
                or self.parameters.dic['catalog_coverage'] or self.parameters.dic['serendipity']):
            self.msgError('Please select one metric in tab Choice Metrics')
            return None

        if self.checkFileNone('file_train', "Select the Training File") or self.checkFileNone('folder_output',
                                                                                              "Select the Output Folder"):
            return None
        else:
            if self.checkFileExists('file_train', "Error! file " + self.parameters.dic['file_train'] + " not exist"):
                return None

        # recommender file
        if self.parameters.dic['quality_analysis'] or self.parameters.dic['diversity_novelty']\
                or self.parameters.dic['genre_coverage'] or self.parameters.dic['catalog_coverage']\
                or self.parameters.dic['serendipity']:
            self.parameters.dic['file_recommender'] = self.getValuesTable()
            if len(self.parameters.dic['file_recommender']) == 0:
                self.msgError("Select the Recommender File")
                return None
            else:
                for j in range(len(self.parameters.dic['file_recommender'])):
                    if not os.path.isfile(self.parameters.dic['file_recommender'][j][1]):
                        self.msgError("Error! file " + self.parameters.dic['file_recommender'][j][1] + " not exist")
                        return None

        if self.parameters.dic['quality_analysis'] or self.parameters.dic['diversity_novelty'] \
                or self.parameters.dic['catalog_coverage']:
            if self.checkFileNone('file_test', "Select the Testing File"):
                return None
            else:
                if self.checkFileExists('file_test', "Error! file " + self.parameters.dic['file_test'] + " not exist"):
                    return None

        if self.parameters.dic['genre_coverage'] or self.parameters.dic['serendipity']:
            if self.checkFileNone('file_feature', "Select the Features File"):
                return None
            else:
                if self.checkFileExists('file_feature',
                                        "Error! file " + self.parameters.dic['file_feature'] + " not exist"):
                    return None

        self.loader_window = windows.loaderWindow(self)
        loader_window = CalcLoader(self)

        config = {}
        config['dic_u_training'] = None
        config['dic_i_training'] = None
        config['amount_ratings'] = None
        config['dic_u_test'] = None
        config['dic_i_test'] = None
        config['loader_value'] = loader_window.value
        config['loader_weight'] = 0

        file_test = self.parameters.dic['file_test']
        file_train = self.parameters.dic['file_train']

        ############################################################################
        # LOAD TRAIN DATA
        ############################################################################
        # function from loadData where returns the data matrices
        loader_window.set_process(1, 'Read Data Training')
        config['loader_weight'] += 1
        try:
            config['dic_u_training'], config['dic_i_training'], config['amount_ratings'] = \
                load_data_training(file_train, self)
        except:
            return

        ############################################################################
        # LOAD TEST
        ############################################################################
        # function from loadData where returns the data matrices
        if self.parameters.dic['quality_analysis'] or self.parameters.dic['catalog_coverage']:
            loader_window.set_process(1, 'Read Data Test')
            config['loader_weight'] += 1
            try:
                config['dic_u_test'], config['dic_i_test'] = load_data_test(file_test, self)
            except:
                return

        ############################################################################
        # CHECK  RATINGS DATA
        ############################################################################
        if self.parameters.dic['quality_analysis'] or self.parameters.dic['catalog_coverage'] \
                or self.parameters.dic['serendipity'] or self.parameters.dic['genre_coverage']:
            for j in range(len(self.parameters.dic['file_recommender'])):
                file_top_n = self.parameters.dic['file_recommender'][j][1]
                amount_n = int(self.parameters.dic['file_recommender'][j][2])

                if self.parameters.dic['mymedialite']:
                    if not check_recommendation_mymedialite(file_top_n, amount_n, self):
                        sys.exit(2)
                else:
                    if not check_recommendation(file_top_n, amount_n, self):
                        sys.exit(2)

        th = threading.Thread(target=runFramework, args=(self, config), daemon=True)
        th.start()
        # self.out_window.show()
        # th.join()
        # self.loader_window.closeCallback()
        # out_window = outWindow.out_window()

    def msgError(self, msg):
        dialog = Gtk.MessageDialog(self.win, 0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK, msg)
        dialog.run()

        dialog.destroy()

    def checkFileExists(self, file, msg):
        if not os.path.isfile(self.parameters.dic[file]):
            self.msgError(msg)
            return True
        return False

    def checkFileNone(self, file, msg):
        if self.parameters[file] is None:
            self.msgError(msg)
            return True
        return False


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    App()
