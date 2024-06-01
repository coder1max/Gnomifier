#!/usr/bin/python3


import gi
import tarfile
import os

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class ComboBoxWindow(Gtk.Window):

    def __init__(self):

        super().__init__(title="Gnomifier")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Create HeaderBar.
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Gnomifier"
        image = Gtk.Image(stock=Gtk.STOCK_HELP)
        help_button = Gtk.Button(label="Help", image=image)
        help_button.connect("clicked", self.on_help_clicked)
        hb.add(help_button)
        self.set_titlebar(hb)

        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        vbox.set_margin_start(20)
        vbox.set_margin_end(20)

        # IMPORT FILE
        button1 = Gtk.Button(label="Import icon pack")
        button1.connect("clicked", self.on_file_clicked)
        vbox.add(button1)

        # LABEL
        dropdown_label = Gtk.Label(label="Choose an icon pack :")
        vbox.add(dropdown_label)

        # DROPDOWN LIST
        home_path = os.getenv("HOME")
        foldersList = [name for name in os.listdir("/usr/share/icons/")] + [name for name in os.listdir(
            home_path + "/.local/share/icons")]

        folders_store = Gtk.ListStore(str)

        for e in foldersList:
            if e.endswith(".svg") or e.endswith(".png") == True:
                continue
            folders_store.append([e])

        folders_combo = Gtk.ComboBox.new_with_model(folders_store)
        folders_combo.connect("changed", self.on_folders_combo_changed)
        renderer_text = Gtk.CellRendererText()
        folders_combo.pack_start(renderer_text, True)
        folders_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(folders_combo, False, False, True)

        self.add(vbox)

    def on_help_clicked(self, widget):
        help_dialog = Gtk.Dialog(title="Help", transient_for=self, flags=0)
        help_dialog.set_default_size(200, 0)

        box = help_dialog.get_content_area()
        box.set_margin_start(20)
        box.set_margin_end(20)
        title_1 = Gtk.Label()
        title_1.set_markup("<b>What is Gnomifier ? </b>")
        title_1.set_margin_top(20)
        box.add(title_1)
        description_1 = Gtk.Label()
        description_1.set_markup("Gnomifier is a simple GTK app for Gnome DE to change the icon pack.")
        description_1.set_line_wrap(True)
        description_1.set_justify(Gtk.Justification.CENTER)
        box.add(description_1)
        title_2 = Gtk.Label()
        title_2.set_markup("<b>How do I use it ?</b>")
        title_2.set_margin_top(20)
        box.add(title_2)
        description_2 = Gtk.Label()
        description_2.set_markup("You can either add a compressed icon pack by clicking 'Import icon pack', or change "
                                 "the current icon pack applied to the system by clicking on the scrolldown menu.")
        description_2.set_line_wrap(True)
        description_2.set_justify(Gtk.Justification.CENTER)
        box.add(description_2)
        title_3 = Gtk.Label()
        title_3.set_markup("<b>Support the project</b>")
        title_3.set_margin_top(20)
        box.add(title_3)
        description_3 = Gtk.Label()
        description_3.set_markup("<a href='https://github.com/coder1max/Gnomifier'>Source code</a>")
        box.add(description_3)

        help_dialog.show_all()
        help_dialog.run()
        help_dialog.destroy()

    def on_file_clicked(self, widget):
        """
        display window to select a file
        :param widget:
        :return: None
        """
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )

        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            file = dialog.get_filename()
            if file.endswith(".tar.xz"):
                print("File can be extracted. Extracting...")
                self.extractFile(file)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def extractFile(self, file):
        """
            function that extracts the icons file into the icons folder
            :return: None
            """
        file = tarfile.open(file)
        # The variable folder will be used to find the folder in the icons folders
        folder = str(os.path.commonprefix(file.getnames()))
        home_path = os.getenv("HOME")
        print(home_path)
        file.extractall(home_path + "/.local/share/icons")
        print("Extraction done")
        file.close()
        self.iconChange(folder)

    def iconChange(self, folder):
        """
            function that changes the default icons with the extracted file
            :param folder: folder where the icons are stored
            :return: None
            """
        print(folder)
        os.system("gsettings set org.gnome.desktop.interface icon-theme" + " '" + folder + "'")

    def add_filters(self, dialog):

        filter_tar_xz = Gtk.FileFilter()
        filter_tar_xz.set_name(".tar.xz files")
        filter_tar_xz.add_pattern("*.tar.xz")
        dialog.add_filter(filter_tar_xz)

        filter_zip = Gtk.FileFilter()
        filter_zip.set_name("ZIP files")
        filter_zip.add_pattern("*.zip")
        dialog.add_filter(filter_zip)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folders_combo_changed(self, combo):

        tree_iter = combo.get_active_iter()

        if tree_iter is not None:
            model = combo.get_model()

            name = model[tree_iter][:1]
            print(name)

            print("Selected element " + str(name[0]))

            os.system("gsettings set org.gnome.desktop.interface icon-theme" + " '" + str(name[0]) + "'")


win = ComboBoxWindow()

win.connect("destroy", Gtk.main_quit)

win.show_all()

Gtk.main()
