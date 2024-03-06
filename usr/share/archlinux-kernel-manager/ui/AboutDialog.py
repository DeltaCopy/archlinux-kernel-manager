# This class stores static information about the app, and is displayed in the about window
import os
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class AboutDialog(Gtk.AboutDialog):
    def __init__(self, manager_gui, **kwargs):
        super().__init__(**kwargs)

        website = "<website-placeholder>"
        authors = ["fennec (DeltaCopy)"]
        program_name = "Arch Linux Kernel Manager"
        comments = (
            f"Add/Remove Officially supported Linux kernels on Arch based systems\n"
            f"Community based Linux kernels are also supported\n"
            f"This application matches your system theme !\n"
            f"Developed in Python with GTK 4\n"
        )

        icon_name = "akm-tux"

        self.set_transient_for(manager_gui)
        self.set_modal(True)
        self.set_authors(authors)
        self.set_program_name(program_name)
        self.set_comments(comments)
        self.set_website(website)
        self.set_website_label(website)
        self.set_logo_icon_name(icon_name)
        self.set_version(manager_gui.app_version)

        tux_icon = Gdk.Texture.new_from_file(
            file=Gio.File.new_for_path(
                os.path.join(base_dir, "images/96x96/akm-tux.png")
            )
        )

        self.set_logo(tux_icon)
