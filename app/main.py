from tkinter import *
from tkinter import filedialog
import extract as e
import zip as z
from tkinter.tix import *
from tkinter.ttk import *
import dialog as d
from threading import Thread
import time
from tkinter import ttk

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

#extract_button = Button(window, image=ext_icon, command=e.extract, compound=CENTER)

#extract_button.pack(side = LEFT, padx=200)

#zip_button = Button(window, image = zip_icon, compound=CENTER, command=open_window)

#zip_button.pack(side = LEFT, padx = 150)

#extract_tip.bind_widget(extract_button, balloonmsg="Extract icon")

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)

editmenu = Menu(menubar, tearoff=0)

compmenu = Menu(menubar, tearoff=0)

extmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Compress", menu=compmenu)
menubar.add_cascade(label="Extract", menu=extmenu)
extmenu.add_command(label="Extract a file to...")
window.config(menu=menubar)

left_tree = ttk.Treeview(window)

left_tree.insert('', END, text='/', iid='root', open=True)
left_tree.insert('',  END, text='/usr', iid='usr', open=True)

CONTENTS = ["Folder 1", "Folder 2", "Folder 3", "Folder 4", "Folder 5", "Folder 6"]

for CONTENT in CONTENTS[0:3]:
    left_tree.insert('root', END, text=CONTENT)
    
for CONTENTPLUS in CONTENTS[3:]:
    left_tree.insert('usr', END, text=CONTENTPLUS)



left_tree.pack(side=LEFT, fill=BOTH)


FILES = []

for i in range(20):
    FILES.append((f"File #{i}", f'{i}kB'))

main_tree = ttk.Treeview(window, columns=('Name', 'Size'), show='headings')

main_tree.heading('Name', text='Name')
main_tree.heading('Size', text='Size')

for FILE in FILES:
    main_tree.insert('', END, values=FILE, text=FILE)

main_tree.pack(side=RIGHT, fill=BOTH, expand=True)

vsb = ttk.Scrollbar(window, orient="vertical", command=left_tree.yview)
vsb.pack(side= RIGHT, fill= Y)

left_tree.configure(yscrollcommand=vsb.set)

window.mainloop()