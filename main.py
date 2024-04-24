import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tarfile
import os

start = "/"
root = Tk()

root.title("Linux icons pack changer")
root.geometry("400x300")

basic_icons_path = str(os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read())


def fileImport():
    """
    function that imports the icons from file manager
    :return: None
    """
    file = filedialog.askopenfilename()
    if file.endswith(".tar.xz"):
        error.grid_forget()
        print("File can be extracted. Extracting...")
        extractFile(file)
    else:
        error.grid(column=1, row=0)


def extractFile(file):
    """
    function that exctracts the icons file into the icons folder
    :return: None
    """
    file = tarfile.open(file)
    # The variable folder will be used to find the folder in the icons folders
    folder = str(os.path.commonprefix(file.getnames()))
    file.extractall("/usr/share/icons/")
    print("Extraction done")
    file.close()
    iconChange(folder)


def iconChange(folder):
    """
    function that changes the default icons
    :param folder: folder where the icons are stored
    :return: None
    """
    change_icons_path = str(os.popen('sudo find /usr -name plasma-changeicons').read())
    os.system(change_icons_path.strip() + ' ' + str(folder))


def restoreIcons():
    """
    function that restores the default icons
    :return: None
    """
    change_icons_path = str(os.popen('sudo find /usr -name plasma-changeicons').read())
    os.system(change_icons_path.strip() + ' ' + str(basic_icons_path))


def changingValue(event):
    change_icons_path = str(os.popen('sudo find /usr -name plasma-changeicons').read())
    os.system(change_icons_path.strip() + ' /usr/share/icons/' + str(selectedIcons.get()))


error = Label(root, text="The fittkle isn't a .tar.xz file", fg="red")

buttons = ttk.Frame(root)
buttons.pack(pady=100)
importButton = Button(buttons, text="Import file", fg="green", command=fileImport)
importButton.pack(side=TOP)
button2 = Button(buttons, text="Restore to default icons", fg="red", command=restoreIcons)
button2.pack()
foldersList = [name for name in os.listdir("/usr/share/icons/")]
selectedIcons = tk.StringVar()
liste = ttk.Combobox(root, values=foldersList, textvariable=selectedIcons)
liste.pack()
liste.bind('<<ComboboxSelected>>', changingValue)

root.mainloop()
