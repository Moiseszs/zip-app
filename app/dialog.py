from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from zip import operate
import time
from threading import Thread

opThread = Thread(target=operate)

def startt():
    opThread.start()

def stop():
    opThread.join()

def init():
    pass




