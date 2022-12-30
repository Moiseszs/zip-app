from tkinter import *
from tkinter import filedialog
import extract as e
import zip as z
from tkinter.tix import *
from tkinter.ttk import *
import dialog as d
from threading import Thread
import time

window = Tk()

window.minsize(300,300)

window.geometry("1000x600")

window.title("Zip-App")

window.configure(bg = '#f7f7f7')

ext_icon = PhotoImage(file = 'app/res/extract-icon.png')
zip_icon = PhotoImage(file = 'app/res/zip-icon.png')


def open_window():
    dialog = Toplevel(window)
    dialog.geometry("300x150")
    progressBar = Progressbar(dialog, length=200, mode='determinate')
    
    progressBar.pack(padx=10, pady=30)
    
    
    def progress():
        total = 200
        d.startt()
        time.sleep(5)
        progressBar['value'] = 10
        for i in range(total):    
            progressBar['value'] += 2
            dialog.update_idletasks()     
            time.sleep(0.600)

    def stop():
        d.stop()

    progressThread = Thread(target=progress)
    start = Button(dialog, text="Start", command = progressThread.start)
    stop = Button(dialog, text="Stop", command = stop)
    start.pack()
    stop.pack()
    dialog.wm_attributes('-topmost', -1)

extract_tip = Balloon(window)

extract_button = Button(window, image=ext_icon, command=e.extract, compound=CENTER)

extract_button.pack(side = LEFT, padx=200)

zip_button = Button(window, image = zip_icon, compound=CENTER, command=open_window)

zip_button.pack(side = LEFT, padx = 150)

extract_tip.bind_widget(extract_button, balloonmsg="Extract icon")

menubar = Menu(window)

filemenu = Menu(menubar)

editmenu = Menu(menubar)


menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)

window.config(menu=menubar)


window.mainloop()