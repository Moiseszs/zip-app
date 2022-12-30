from tkinter import filedialog,Tk
from zipfile import *
import os
import shutil
import time

source = ''
dest = ''


def ask_folder():
    folder = filedialog.askdirectory()
    return folder

def ask_path():
    path = filedialog.askdirectory()
    return path

def move(file, dest):

    filename = file + '.zip'  

    print(filename)
    print(dest)

    shutil.move(filename, dest)

def name_it(source):

    base_name = os.path.basename(source)

    return base_name
    

def archive(source, filename):
    shutil.make_archive(filename, 'zip', root_dir=source)
    
def operate():
    window = Tk()
    window.geometry("500x200")
    source = ask_folder()
    dest = ask_folder()
     

    filename = name_it(source)

    time.sleep(2)

    archive(source, filename)
    

    move(filename, dest)