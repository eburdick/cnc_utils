#!/usr/bin/python3

import os
from os import path

from tkinter import filedialog
from tkinter import *
from tkinter import ttk

input_dir_base = "/"
in_path_state_file_name = "/infile_path"
#
# State_dir is the directory where the program saves its state between runs.
# Currently it is the directory where the program lives.
#
state_dir = os.path.dirname(os.path.realpath(__file__))
#
# The in path state file saves the default directory for the input file, initially
# at the system root directory. If the user chooses another directory, that will
# be saved in the path state file, so the next time the program is run, it will
# still be set to that location.
#
in_path_state_path = state_dir + in_path_state_file_name
print(in_path_state_path)

if not path.exists(in_path_state_path):
    #
    #
    #
    in_path_file = open(in_path_state_path, "w")
    in_path_file.write(input_dir_base)
    in_path_file.close()
    print("input path default created")
else:
    in_path_file = open(in_path_state_path, "r")
    input_dir_base = in_path_file.readline();
    in_path_file.close()
    print("input path default already exists" + input_dir_base)

def get_infile_clicked():
    #
    # Temporary button to pop up file dialog
    #
    window.in_file_name = filedialog.askopenfilename(initialdir=window.input_dir_base, title="Select gcode file",
                                                     filetypes=(("nc files", "*.nc"), ("all files", "*.*")))
    (head,tail)=os.path.split(window.in_file_name)
    print(head)
    print(tail)
    return

def show_contents_clicked():
    in_file = open(window.in_file_name, "r")

    content = in_file.readlines()

    in_file.close()

    for line in content:
        print(line, end='')

    return

def get_input_directory_clicked():
    window.input_dir_base = filedialog.askdirectory(initialdir = in_path_state_path, title="Select Default Input Folder")
    in_path_file = open(in_path_state_path, "w")
    in_path_file.write(window.input_dir_base)
    in_path_file.close()
    print(window.input_dir_base)
    return

window = Tk()

window.input_dir_base = input_dir_base

get_infile_button = Button(window, text='In File', command=get_infile_clicked)

show_content_button = Button(window, text='Show Contents', command=show_contents_clicked)

get_input_directory = Button(window, text='Set Input Folder', command=get_input_directory_clicked)

get_input_directory.pack()
get_infile_button.pack()
show_content_button.pack()


window.mainloop()



