from tkinter import filedialog
from tkinter import messagebox
from zipfile import *
import shutil
import os

def ask_zip():
    folder = filedialog.askopenfilename()
    return folder

def ask_path():
    path = filedialog.askdirectory()
    return path

def success():
    messagebox.showinfo(title="status", message="sucess")

def extract():
    file = ask_zip()
    path_root = ask_path()
    filename = os.path.basename(file)
    path  = os.path.join(path_root, filename)
    path = (os.path.splitext(path)[0])

    os.mkdir(path)
    shutil.unpack_archive(file, path)

    success()
