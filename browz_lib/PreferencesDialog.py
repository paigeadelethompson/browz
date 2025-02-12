# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# BEGIN LICENSE
# This file is in the public domain
# END LICENSE

"""this dialog adjusts values in gsettings
"""

from . helpers import get_builder, show_uri, get_help_uri
from gi.repository import Gtk  # pylint: disable=E0611
import logging
logger = logging.getLogger('browz_lib')


class PreferencesDialog(Gtk.Dialog):
    __gtype_name__ = "PreferencesDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when
        constructing a new instance of this class.

        Returns a fully instantiated PreferencesDialog object.
        """
        builder = get_builder('PreferencesBrowzDialog')
        new_object = builder.get_object("preferences_browz_dialog")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initalizing should be called after parsing the ui definition
        and creating a PreferencesDialog object with it in order to
        finish initializing the start of the new PerferencesBrowzDialog
        instance.

        Put your initialization code in here and leave __init__ undefined.
        """

        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self, True)

        # code for other initialization actions should be added here

    def on_btn_close_clicked(self, widget, data=None):
        self.destroy()

    def on_btn_help_clicked(self, widget, data=None):
        show_uri(self, "ghelp:%s" % get_help_uri('preferences'))
