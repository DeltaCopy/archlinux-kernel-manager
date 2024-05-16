import gi
import os
import libs.functions as fn
from ui.ProgressWindow import ProgressWindow
from ui.MessageWindow import MessageWindow

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GLib

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class FlowBox(Gtk.FlowBox):
    def __init__(
        self,
        kernel,
        active_kernel,
        manager_gui,
        source,
    ):
        super(FlowBox, self).__init__()

        self.manager_gui = manager_gui

        # self.set_row_spacing(5)
        # self.set_activate_on_single_click(True)
        # self.connect("child-activated", self.on_child_activated)

        self.set_selection_mode(Gtk.SelectionMode.NONE)

        # self.set_homogeneous(True)
        self.set_max_children_per_line(2)
        self.set_min_children_per_line(2)
        self.kernel_count = 0

        self.active_kernel_found = False
        self.kernels = []

        self.kernel = kernel
        self.source = source

        if self.source == "official":
            self.flowbox_official()

        if self.source == "community":
            self.flowbox_community()

    def flowbox_community(self):
        for community_kernel in self.kernel:
            self.kernels.append(community_kernel)

            self.kernel_count += 1

        if len(self.kernels) > 0:
            installed = False

            for cache in self.kernels:
                fb_child = Gtk.FlowBoxChild()
                fb_child.set_name(
                    "%s %s %s" % (cache.name, cache.version, cache.repository)
                )

                tux_icon = Gtk.Picture.new_for_file(
                    file=Gio.File.new_for_path(
                        os.path.join(base_dir, "images/48x48/akm-tux.png")
                    )
                )

                tux_icon.set_content_fit(content_fit=Gtk.ContentFit.SCALE_DOWN)
                tux_icon.set_halign(Gtk.Align.START)

                # hbox_tux_icon = Gtk.Box(
                #     orientation=Gtk.Orientation.HORIZONTAL, spacing=0
                # )
                # hbox_tux_icon.set_homogeneous(True)
                #
                # hbox_tux_icon.append(tux_icon)

                vbox_kernel_widgets = Gtk.Box(
                    orientation=Gtk.Orientation.VERTICAL, spacing=0
                )
                vbox_kernel_widgets.set_name("vbox_kernel_widgets")
                vbox_kernel_widgets.set_homogeneous(True)

                switch_kernel = Gtk.Switch()
                switch_kernel.set_halign(Gtk.Align.START)

                hbox_kernel_switch = Gtk.Box(
                    orientation=Gtk.Orientation.HORIZONTAL, spacing=0
                )

                hbox_kernel_switch.append(switch_kernel)

                label_active_kernel_info = Gtk.Label(xalign=0, yalign=0)
                label_kernel_version = Gtk.Label(xalign=0, yalign=0)
                label_kernel_version.set_name("label_kernel_version")

                label_kernel_size = Gtk.Label(xalign=0, yalign=0)
                label_kernel_size.set_name("label_kernel_flowbox")

                for installed_kernel in self.manager_gui.installed_kernels:
                    if "{}-{}".format(
                        installed_kernel.name, installed_kernel.version
                    ) == "{}-{}".format(cache.name, cache.version):
                        installed = True

                if installed is True:
                    switch_kernel.set_state(True)
                    switch_kernel.set_active(True)

                else:
                    switch_kernel.set_state(False)
                    switch_kernel.set_active(False)

                installed = False
                switch_kernel.connect("state-set", self.kernel_toggle_state, cache)
                # switch_kernel.connect(
                #     "notify::active", self.kernel_toggle_active, cache
                # )

                hbox_kernel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                hbox_kernel.set_name("hbox_kernel")

                label_kernel_name = Gtk.Label(xalign=0, yalign=0)
                label_kernel_name.set_name("label_kernel_version")
                label_kernel_name.set_text(
                    "%s-%s /%s" % (cache.name, cache.version, cache.repository)
                )

                vbox_kernel_widgets.append(label_kernel_name)

                label_kernel_size.set_text("%sM" % str(cache.install_size))

                vbox_kernel_widgets.append(label_kernel_size)

                label_kernel_build_date = Gtk.Label(xalign=0, yalign=0)
                label_kernel_build_date.set_name("label_kernel_flowbox")
                label_kernel_build_date.set_text(cache.build_date)

                vbox_kernel_widgets.append(label_kernel_build_date)

                vbox_kernel_widgets.append(hbox_kernel_switch)

                hbox_kernel.append(tux_icon)
                hbox_kernel.append(vbox_kernel_widgets)

                fb_child.set_child(hbox_kernel)

                self.append(fb_child)

    def flowbox_official(self):
        for official_kernel in self.manager_gui.official_kernels:
            if official_kernel.name == self.kernel:
                self.kernels.append(official_kernel)
                self.kernel_count += 1

        if len(self.kernels) > 0:
            installed = False

            latest = sorted(self.kernels)[:-1][0]

            for cache in sorted(self.kernels):
                fb_child = Gtk.FlowBoxChild()
                fb_child.set_name("%s %s" % (cache.name, cache.version))
                if cache == latest:
                    tux_icon = Gtk.Picture.new_for_file(
                        file=Gio.File.new_for_path(
                            os.path.join(base_dir, "images/48x48/akm-new.png")
                        )
                    )

                else:
                    tux_icon = Gtk.Picture.new_for_file(
                        file=Gio.File.new_for_path(
                            os.path.join(base_dir, "images/48x48/akm-tux.png")
                        )
                    )

                tux_icon.set_content_fit(content_fit=Gtk.ContentFit.SCALE_DOWN)
                tux_icon.set_halign(Gtk.Align.START)

                vbox_kernel_widgets = Gtk.Box(
                    orientation=Gtk.Orientation.VERTICAL, spacing=0
                )
                vbox_kernel_widgets.set_homogeneous(True)

                hbox_kernel_switch = Gtk.Box(
                    orientation=Gtk.Orientation.HORIZONTAL, spacing=0
                )

                switch_kernel = Gtk.Switch()
                switch_kernel.set_halign(Gtk.Align.START)

                hbox_kernel_switch.append(switch_kernel)

                label_kernel_version = Gtk.Label(xalign=0, yalign=0)
                label_kernel_version.set_name("label_kernel_version")
                label_kernel_version.set_selectable(True)

                label_kernel_size = Gtk.Label(xalign=0, yalign=0)
                label_kernel_size.set_name("label_kernel_flowbox")

                if self.manager_gui.installed_kernels is None:
                    self.manager_gui.installed_kernels = fn.get_installed_kernels()

                for installed_kernel in self.manager_gui.installed_kernels:
                    if (
                        "{}-{}".format(installed_kernel.name, installed_kernel.version)
                        == cache.version
                    ):
                        installed = True

                if installed is True:
                    switch_kernel.set_state(True)
                    switch_kernel.set_active(True)

                else:
                    switch_kernel.set_state(False)
                    switch_kernel.set_active(False)

                installed = False
                switch_kernel.connect("state-set", self.kernel_toggle_state, cache)

                # switch_kernel.connect(
                #     "notify::active", self.kernel_toggle_active, cache
                # )

                label_kernel_version.set_text(cache.version)

                hbox_kernel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                hbox_kernel.set_name("hbox_kernel")

                label_kernel_size.set_text(cache.size)

                vbox_kernel_widgets.append(label_kernel_version)
                vbox_kernel_widgets.append(label_kernel_size)

                label_kernel_modified = Gtk.Label(xalign=0, yalign=0)
                label_kernel_modified.set_name("label_kernel_flowbox")
                label_kernel_modified.set_text(cache.last_modified)

                vbox_kernel_widgets.append(label_kernel_modified)

                vbox_kernel_widgets.append(hbox_kernel_switch)

                hbox_kernel.append(tux_icon)
                hbox_kernel.append(vbox_kernel_widgets)

                fb_child.set_child(hbox_kernel)

                self.append(fb_child)

        else:
            fn.logger.error("Failed to read in kernels.")

    # def kernel_toggle_active(self, switch, data, kernel):
    #     print("kernel_toggle_active")
    #     if switch.get_state() is False:
    #         switch.set_active(True)
    #     else:
    #         switch.set_active(False)
    #     # return True

    def kernel_toggle_state(self, switch, data, kernel):
        fn.logger.debug(
            "Switch toggled, kernel selected = %s %s" % (kernel.name, kernel.version)
        )

        if fn.check_pacman_lockfile() is False:
            # switch widget is currently toggled off
            if switch.get_state() is False:  # and switch.get_active() is True:
                # self.fn.download_kernel_package(kernel)
                message_window = FlowBoxMessageWindow(
                    title="Install kernel ?",
                    message="Install <b>%s-%s</b>" % (kernel.name, kernel.version),
                    action="install",
                    kernel=kernel,
                    transient_for=self.manager_gui,
                    textview=self.manager_gui.textview,
                    textbuffer=self.manager_gui.textbuffer,
                    switch=switch,
                    source=self.source,
                    manager_gui=self.manager_gui,
                    image_path="images/48x48/akm-install.png",
                )
                message_window.present()
                return True

            # switch widget is currently toggled on
            # if widget.get_state() == True and widget.get_active() == False:
            if switch.get_state() is True:
                # and switch.get_active() is False:
                installed_kernels = fn.get_installed_kernels()

                if len(installed_kernels) > 1:
                    message_window = FlowBoxMessageWindow(
                        title="Remove kernel ?",
                        message="Remove <b>%s-%s</b>" % (kernel.name, kernel.version),
                        action="uninstall",
                        kernel=kernel,
                        transient_for=self.manager_gui,
                        textview=self.manager_gui.textview,
                        textbuffer=self.manager_gui.textbuffer,
                        switch=switch,
                        source=self.source,
                        manager_gui=self.manager_gui,
                        image_path="images/48x48/akm-remove.png",
                    )
                    message_window.present()
                    return True
                else:
                    switch.set_state(True)
                    # switch.set_active(False)
                    fn.logger.warn(
                        "You only have 1 kernel installed %s-%s, uninstall aborted."
                        % (kernel.name, kernel.version)
                    )
                    msg_win = MessageWindow(
                        title="Warning: Uninstall aborted",
                        message=f"You only have 1 kernel installed.\n"
                        f"{kernel.name} {kernel.version}\n",
                        image_path="images/48x48/akm-remove.png",
                        transient_for=self.manager_gui,
                    )
                    msg_win.present()
                    return True

        else:
            fn.logger.error(
                "Pacman lockfile found, is another pacman process running ?"
            )

            msg_win = MessageWindow(
                title="Warning",
                message="Pacman lockfile found, which indicates another pacman process is running",
                transient_for=self.manager_gui,
            )
            msg_win.present()
            return True

        # while self.manager_gui.default_context.pending():
        #     self.manager_gui.default_context.iteration(True)


class FlowBoxInstalled(Gtk.FlowBox):
    def __init__(self, installed_kernels, manager_gui, **kwargs):
        super().__init__(**kwargs)

        self.set_row_spacing(5)

        self.set_selection_mode(Gtk.SelectionMode.NONE)

        self.set_homogeneous(True)
        self.set_max_children_per_line(2)
        self.set_min_children_per_line(2)

        self.manager_gui = manager_gui

        for installed_kernel in installed_kernels:
            tux_icon = Gtk.Picture.new_for_file(
                file=Gio.File.new_for_path(
                    os.path.join(base_dir, "images/48x48/akm-tux.png")
                )
            )

            fb_child = Gtk.FlowBoxChild()
            fb_child.set_name(
                "%s %s" % (installed_kernel.name, installed_kernel.version)
            )

            tux_icon.set_content_fit(content_fit=Gtk.ContentFit.SCALE_DOWN)
            tux_icon.set_halign(Gtk.Align.START)

            # vbox_tux_icon = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

            # vbox_tux_icon.append(tux_icon)

            label_installed_kernel_version = Gtk.Label(xalign=0, yalign=0)
            label_installed_kernel_version.set_name("label_kernel_version")
            label_installed_kernel_version.set_text(installed_kernel.version)

            label_installed_kernel_name = Gtk.Label(xalign=0, yalign=0)
            label_installed_kernel_name.set_name("label_kernel_version")
            label_installed_kernel_name.set_text(installed_kernel.name)

            hbox_installed_version = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL, spacing=0
            )

            hbox_installed_version.append(label_installed_kernel_name)
            hbox_installed_version.append(label_installed_kernel_version)

            label_installed_kernel_size = Gtk.Label(xalign=0, yalign=0)
            label_installed_kernel_size.set_name("label_kernel_flowbox")
            label_installed_kernel_size.set_text("%s" % installed_kernel.size)

            label_installed_kernel_date = Gtk.Label(xalign=0, yalign=0)
            label_installed_kernel_date.set_name("label_kernel_flowbox")
            label_installed_kernel_date.set_text("%s" % installed_kernel.date)

            image_uninstall = Gtk.Picture.new_for_file(
                file=Gio.File.new_for_path("%s/images/48x48/akm-remove.png" % base_dir)
            )
            image_uninstall.set_content_fit(content_fit=Gtk.ContentFit.COVER)
            image_uninstall.set_halign(Gtk.Align.START)

            button_uninstall_kernel = Gtk.Button.new_with_label("Remove")

            # vbox_tux_icon.append(button_uninstall_kernel)

            button_uninstall_kernel.set_size_request(100, 30)
            button_uninstall_kernel.set_halign(Gtk.Align.START)
            # button_uninstall_kernel.set_name("button_uninstall_kernel")

            button_uninstall_kernel.connect(
                "clicked", self.button_uninstall_kernel, installed_kernel
            )

            vbox_kernel_widgets = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL, spacing=0
            )
            vbox_kernel_widgets.set_homogeneous(True)

            # vbox_kernel_widgets.append(label_installed_kernel_name)
            # vbox_kernel_widgets.append(label_installed_kernel_version)
            vbox_kernel_widgets.append(hbox_installed_version)
            vbox_kernel_widgets.append(label_installed_kernel_size)
            vbox_kernel_widgets.append(label_installed_kernel_date)
            vbox_kernel_widgets.append(button_uninstall_kernel)

            hbox_kernel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            hbox_kernel.set_name("hbox_kernel")

            hbox_kernel.append(tux_icon)
            hbox_kernel.append(vbox_kernel_widgets)

            fb_child.set_child(hbox_kernel)

            self.append(fb_child)

    def button_uninstall_kernel(self, button, installed_kernel):
        installed_kernels = fn.get_installed_kernels()

        if len(installed_kernels) > 1:
            fn.logger.info(
                "Selected kernel to remove = %s %s"
                % (installed_kernel.name, installed_kernel.version)
            )

            message_window = FlowBoxMessageWindow(
                title="Remove kernel ?",
                message="Remove <b>%s-%s</b>"
                % (installed_kernel.name, installed_kernel.version),
                action="uninstall",
                kernel=installed_kernel,
                transient_for=self.manager_gui,
                textview=self.manager_gui.textview,
                textbuffer=self.manager_gui.textbuffer,
                switch=None,
                source=None,
                manager_gui=self.manager_gui,
                image_path="images/48x48/akm-remove.png",
            )
            message_window.present()
        else:
            fn.logger.warn(
                "You only have 1 kernel installed, %s %s uninstall aborted."
                % (installed_kernel.name, installed_kernel.version)
            )
            msg_win = MessageWindow(
                title="Warning: Uninstall aborted",
                message=f"You only have 1 kernel installed, {installed_kernel.name} {installed_kernel.version}\n",
                image_path="images/48x48/akm-remove.png",
                transient_for=self.manager_gui,
            )
            msg_win.present()


class FlowBoxMessageWindow(Gtk.Window):
    def __init__(
        self,
        title,
        message,
        action,
        kernel,
        textview,
        textbuffer,
        switch,
        source,
        manager_gui,
        image_path,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.set_title(title=title)
        self.set_modal(modal=True)
        self.set_resizable(False)
        self.set_size_request(350, 100)

        self.textview = textview
        self.textbuffer = textbuffer
        self.manager_gui = manager_gui
        self.kernel = kernel
        self.action = action
        self.switch = switch
        self.source = source

        image = Gtk.Picture.new_for_filename(os.path.join(base_dir, image_path))

        image.set_content_fit(content_fit=Gtk.ContentFit.SCALE_DOWN)
        image.set_halign(Gtk.Align.START)

        hbox_image = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        hbox_image.append(image)

        vbox_flowbox_message = Gtk.Box.new(
            orientation=Gtk.Orientation.VERTICAL, spacing=10
        )
        vbox_flowbox_message.set_name("vbox_flowbox_message")

        self.set_child(child=vbox_flowbox_message)

        label_flowbox_message = Gtk.Label(xalign=0, yalign=0)
        label_flowbox_message.set_markup("%s" % message)
        label_flowbox_message.set_name("label_flowbox_message")

        hbox_image.append(label_flowbox_message)

        vbox_flowbox_message.append(hbox_image)
        vbox_flowbox_message.set_halign(Gtk.Align.CENTER)

        # Widgets.
        button_yes = Gtk.Button.new_with_label("Yes")
        button_yes.set_size_request(100, 30)
        button_yes.set_halign(Gtk.Align.END)
        button_yes_context = button_yes.get_style_context()
        button_yes_context.add_class("destructive-action")
        button_yes.connect("clicked", self.on_button_yes_clicked)

        button_no = Gtk.Button.new_with_label("No")
        button_no.set_size_request(100, 30)
        button_no.set_halign(Gtk.Align.END)
        button_no.connect("clicked", self.on_button_no_clicked)

        hbox_buttons = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox_buttons.set_halign(Gtk.Align.CENTER)
        hbox_buttons.append(button_yes)
        hbox_buttons.append(button_no)

        vbox_flowbox_message.append(hbox_buttons)

    def on_button_yes_clicked(self, button):
        self.hide()
        self.destroy()
        progress_window = None
        if fn.check_pacman_lockfile() is False:
            if self.action == "uninstall":
                progress_window = ProgressWindow(
                    title="Removing %s %s" % (self.kernel.name, self.kernel.version),
                    action="uninstall",
                    textview=self.textview,
                    textbuffer=self.textbuffer,
                    kernel=self.kernel,
                    switch=self.switch,
                    source=self.source,
                    manager_gui=self.manager_gui,
                    transient_for=self.manager_gui,
                )

            if self.action == "install":
                progress_window = ProgressWindow(
                    title="Installing %s %s" % (self.kernel.name, self.kernel.version),
                    action="install",
                    textview=self.textview,
                    textbuffer=self.textbuffer,
                    kernel=self.kernel,
                    switch=self.switch,
                    source=self.source,
                    manager_gui=self.manager_gui,
                    transient_for=self.manager_gui,
                )
        else:
            fn.logger.error(
                "Pacman lockfile found, is another pacman process running ?"
            )

    def on_button_no_clicked(self, button):
        if self.action == "uninstall":
            if self.switch is not None:
                self.switch.set_state(True)

        elif self.action == "install":
            if self.switch is not None:
                self.switch.set_state(False)

        self.hide()
        self.destroy()

        return True
