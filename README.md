# Linux-icons-modifier (KDE required) -- BETA (V-0.1)

<br>

<div align="center">
  <img src="icons/linux_icons_modifier.png" width="200px"><br>
</div>

<br>

### __*KDE Plasma needs to be installed on your pc for this program to work. It will work even if there are multiple DE on your OS, you need at least KDE Plasma.*__
A simple program written in Python (Tkinter) to switch between icons packs on Linux. I know this is already included in KDE Plasma but I will soon add an option to change icons directly on GNOME.

*Linux icons modifier* is a simple python program that uses both the OS, tarfile, and Tkinter module from Python. [Tkinter](https://docs.python.org/3/library/tkinter.html) is used for the GUI (not the best I agree but for the moment I don't know how to make python app "prettier"), while [tarfile](https://docs.python.org/3/library/tarfile.html) is used to untar icons packs files, and [OS](https://docs.python.org/3/library/os.html) is used to use terminal commands in order to change the icons.

## How to use this program?
### 1) Make sure every module is installed
Install Tkinter with PIP : `pip install tk`

Install Tkinter with apt : `sudo apt install python3-tk`

### 2) Run the python file in your terminal
For the moment the only way to get this program to work without root privilegies problems is to open your terminal (Konsole), head to the directory where the *main.py* file is located with `cd path_to_the_directory` and run the file with `python3 main.py`.

Then the app should run fine. Make sure the terminal is still opened since it may ask you root privilegies to modify icons, in the terminal.

## How to add an icons pack?
In order to add a new icon pack, you just need to download one from internet in the *.tar.xz* format, then click on the *Import icon pack* button, choose your file and it will change your DE icons.

## Other
* You can change the icons with the dropdown list.
* The dropdown list may contain file names, I'm going to solve this too but it should'nt hurt your pc if you choose an icon since it will simply not work.

* Some icons may not change immediatly, I don't know how to solve this problem but I'm working on it, but it's normal if some don't seem to change, just restart your pc or click on them it must work.

* If you encounter any other bug, report it in this repo I'll do my best to solve it
* I am not responsible for any damage caused to your OS, this program shouldn't harm your pc but it's a beta right now, just try it if you want to contribute or have fun.
