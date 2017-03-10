# -*- coding: utf-8 -*-
from gi import require_version

require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import sys

import fileChooser


class infoWindow(Gtk.Window):
    def __init__(self, window):
        builder = Gtk.Builder()
        builder.add_from_file("info.glade")

        self.values = window

        self.windowApp = builder.get_object("window")

        # Buttons
        btnClose = builder.get_object("btnClose")

        # Buttons Event Handler
        btnClose.connect("clicked", self.closeCallback)

        self.windowApp.set_transient_for(window.win)

        self.windowApp.connect("delete-event", Gtk.main_quit)
        self.windowApp.show_all()
        Gtk.main()

    def closeCallback(self, widget):
        Gtk.main_quit()
        self.windowApp.destroy()


class generateTrainTestWindow(Gtk.Window):
    def __init__(self, window):
        builder = Gtk.Builder()
        builder.add_from_file("generateTrainTest.glade")

        self.values = window

        self.windowApp = builder.get_object("window")

        # build file chooser
        self.fChooser = fileChooser.FileChooserWindow()

        # set file
        self.params = {}
        self.params['file'] = None
        self.params['folder_out'] = None

        # set action Data File Chooser
        self.lbDataFile = builder.get_object("lbDataFile")
        btnDataFile = builder.get_object("btnDataFile")
        btnDataFile.connect("clicked", self.fChooser.on_file_clicked, self.lbDataFile, self, 'file')

        # set action Output Folder Chooser
        self.lbFolderOutput = builder.get_object("lbFolderOutput")
        btnFolderOutput = builder.get_object("btnFolderOutput")
        btnFolderOutput.connect("clicked", self.fChooser.on_folder_clicked, self.lbFolderOutput, self,
                                'folder_out')

        # set action Run
        self.btnRun = builder.get_object("btnRun")
        self.spinner = builder.get_object("spinner")
        self.btnRun.connect("clicked", self.runCallback)

        self.windowApp.set_transient_for(window.win)

        self.windowApp.connect("delete-event", Gtk.main_quit)
        self.windowApp.show_all()
        Gtk.main()

    def runCallback(self, widget):
        if (self.btnRun.get_label() == "Run"):
            self.spinner.start()
            self.btnRun.set_sensitive(False)
        # self.btnRun.set_label("Close")
        # self.spinner.stop()
        # self.btnRun.set_sensitive(True)
        else:
            Gtk.main_quit()
            self.windowApp.destroy()


class generateFeatureWindow(Gtk.Window):
    def __init__(self, window):
        builder = Gtk.Builder()
        builder.add_from_file("generateFeature.glade")

        self.values = window

        self.windowApp = builder.get_object("window")

        # build file chooser
        self.fChooser = fileChooser.FileChooserWindow()

        # set file
        self.params = {}
        self.params['file'] = None
        self.params['folder_out'] = None

        # set action Data File Chooser
        self.lbDataFile = builder.get_object("lbDataFile")
        btnDataFile = builder.get_object("btnDataFile")
        btnDataFile.connect("clicked", self.fChooser.on_file_clicked, self.lbDataFile, self, 'file')

        # set action Output Folder Chooser
        self.lbFolderOutput = builder.get_object("lbFolderOutput")
        btnFolderOutput = builder.get_object("btnFolderOutput")
        btnFolderOutput.connect("clicked", self.fChooser.on_folder_clicked, self.lbFolderOutput, self,
                                'folder_out')

        # set action Run
        self.btnRun = builder.get_object("btnRun")
        self.spinner = builder.get_object("spinner")
        self.btnRun.connect("clicked", self.runCallback)

        self.windowApp.set_transient_for(window.win)

        self.windowApp.connect("delete-event", Gtk.main_quit)
        self.windowApp.show_all()
        Gtk.main()

    def runCallback(self, widget):
        if (self.btnRun.get_label() == "Run"):
            self.spinner.start()
            self.btnRun.set_sensitive(False)
            # self.btnRun.set_label("Close")
            # self.spinner.stop()
            # self.btnRun.set_sensitive(True)
        else:
            Gtk.main_quit()
            self.windowApp.destroy()


class loaderWindow(Gtk.Window):
    def __init__(self, window):
        builder = Gtk.Builder()
        builder.add_from_file("loader.glade")

        self.values = window

        self.thread = None

        self.exit = False

        self.windowApp = builder.get_object("window")

        # Buttons
        # self.btnClose = builder.get_object("btnClose")
        # self.btnClose.set_sensitive(False)
        # Buttons Event Handler
        # self.btnClose.connect("clicked", self.closeCallback)

        self.progressbar = builder.get_object("progressbar")
        self.progressFinish = False
        self.lbLoader = builder.get_object("lbLoader")
        # self.timeout_id = GObject.timeout_add(50, self.on_timeout)

        self.windowApp.set_transient_for(window.win)

        self.windowApp.connect("delete-event", self.alertExit)
        window.loader_window = self
        self.windowApp.show_all()

    def closeCallback(self):
        self.windowApp.destroy()
        if self.exit:
            self.exit = False
            self.windowApp.destroy()
            Gtk.main_quit()

    def setStatus(self, value):
        if 0.25 < value <= 1:
            value -= 0.05
        if value == 1.1:
            self.progressbar.set_fraction(1)
            self.progressFinish = True
            # self.btnClose.set_sensitive(True)
        else:
            self.progressbar.set_fraction(value)

    def setText(self, text):
        self.lbLoader.set_text(text)

    def getStatus(self):
        return float(self.progressbar.get_fraction())

    def alertExit(self, widget, data):
        if self.progressFinish:
            self.windowApp.destroy()
            Gtk.main_quit()
        else:
            dialog = Gtk.MessageDialog(self.windowApp, 0, Gtk.MessageType.WARNING,
                                       Gtk.ButtonsType.OK_CANCEL, "CONFIRM EXIT")
            dialog.format_secondary_text(
                "You confirm exit to software?")
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                dialog.destroy()
                if self.exit:
                    self.exit = False
                    self.windowApp.destroy()
                    Gtk.main_quit()
                sys.exit(1)
            elif response == Gtk.ResponseType.CANCEL:
                print('CANCEl')
                dialog.destroy()
                self.exit = True
                Gtk.main()

    def on_timeout(self):
        """
        Update value on the progress bar
        """
        value = self.progressbar.get_fraction() + 0.01

        if value > 1:
            self.progressFinish = True
            self.btnClose.set_sensitive(True)

        self.progressbar.set_fraction(value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True

    def msg_error(self, msg):
        dialog = Gtk.MessageDialog(self.windowApp, 0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK, msg)
        dialog.run()

        dialog.destroy()


class DialogEntry(Gtk.Dialog):

    def __init__(self, parent, title, labelText):
        Gtk.Dialog.__init__(self, title, parent, 0,
            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(200, 100)

        label = Gtk.Label(labelText)

        box = self.get_content_area()
        box.add(label)

        self.entry = Gtk.Entry()
        self.entry.set_text(title)
        box.pack_start(self.entry, True, True, 0)

        self.show_all()
