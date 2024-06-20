# Gnomifier (Gnome required) -- BETA (V-0.1)

<br>

<div align="center">
  <img src="gnomifier-0.1/icons/gnomifier.png" width="200px"><br>
</div>

<br>

### __*GNOME DE needs to be installed on your pc for this program to work. It will work even if there are multiple DE on your OS, you need at least GNOME DE.*__
A simple program written in Python (PyGObject) to switch between icons packs on Linux.

*Linux icons modifier* is a simple python program that uses both the OS, tarfile, and PyGObject module from Python. [PyGobject](https://pygobject.gnome.org/), so GTK3, is used for the GUI, while [tarfile](https://docs.python.org/3/library/tarfile.html) is used to untar icons packs files, and [OS](https://docs.python.org/3/library/os.html) is used to use terminal commands in order to change the icons.

## How to use this program?
### 1) Make sure everything is installed
Install GNOME : `sudo apt-get install task-gnome-desktop && sudo reboot`

### 2) Run the app
Download the *gnomifier-X.X.deb* file from the package section, or if you are not on a Debian based distro, simply download the *main.py* file from this repository and execute it from a terminal with `cd path/to/the/python/file && python3 main.py`

Then the app should run fine.

## How to add an icons pack?
In order to add a new icon pack, you just need to download one from internet in the *.tar.xz* format, then click on the *Import icon pack* button, choose your file and it will change your DE icons. When you click 'open', the window may seem frozen for a few seconds or more, this is totaly normal, give it the time to untar the file.

## Other
* You can change the icons with the dropdown list.
* I am planning on adding a feature to remove some icon packs, and to make the app prettier.
* If you encounter any bug, report it in this repo I'll do my best to solve it
* I am not responsible for any damage caused to your OS, this program shouldn't harm your pc but it's a beta right now, just try it if you want to contribute or have fun.
