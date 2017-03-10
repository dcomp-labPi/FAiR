# -*- coding: utf-8 -*-
from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk

import os
from windows import DialogEntry
from checkRecommendation import check_recommendation


class FileChooserWindow(Gtk.Window):
    def on_file_clicked(self, widget, label, window, file):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if Gtk.Buildable.get_name(widget) == 'btnRecommenderFile':
                dialog_entry = DialogEntry(self, "Input Name", "Write name of recommender metric")
                response = dialog_entry.run()
                if response == Gtk.ResponseType.OK:
                    dialog_amount = DialogEntry(self, 'Input amount topN', 'Write the amount of topN recommendations')
                    response_amount = dialog_amount.run()
                    if response_amount == Gtk.ResponseType.OK:
                        window.setValuesTable(dialog_entry.entry.get_text(), dialog.get_filename(), int(dialog_amount.entry.get_text()))
                    dialog_amount.destroy()
                dialog_entry.destroy()
            elif Gtk.Buildable.get_name(widget) == 'btnDataFile':
                label.set_text(os.path.basename(dialog.get_filename()))
                window.params[file] = dialog.get_filename()
            else:
                label.set_text(os.path.basename(dialog.get_filename()))
                window.parameters.dic[file] = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            # print("Cancel clicked")
            pass

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget, label, parameters, file):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            label.set_text(os.path.basename(dialog.get_filename()))
            if Gtk.Buildable.get_name(widget) == 'btnFolderOutput':
                parameters[file] = dialog.get_filename()
            else:
                parameters.dic[file] = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            # print("Cancel clicked")
            pass

        dialog.destroy()
