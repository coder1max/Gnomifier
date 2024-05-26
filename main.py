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
