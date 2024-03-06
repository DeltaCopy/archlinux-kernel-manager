import gi
import libs.functions as fn

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GLib, GdkPixbuf, GObject, Gdk

base_dir = fn.os.path.abspath(fn.os.path.join(fn.os.path.dirname(__file__), ".."))


class SplashScreen(Gtk.Window):
    def __init__(self, **kwargs):
        # Gtk.Window.__init__(self, Gtk.WindowType.POPUP, title="")
        super().__init__(**kwargs)
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_modal(True)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        self.set_child(child=main_vbox)

        tux_icon = Gtk.Picture.new_for_file(
            file=Gio.File.new_for_path(
                fn.os.path.join(base_dir, "images/364x408/akm-tux-splash.png")
            )
        )

        tux_icon.set_opacity(0.5)
        tux_icon.set_content_fit(content_fit=Gtk.ContentFit.FILL)

        main_vbox.append(tux_icon)

        self.present()
