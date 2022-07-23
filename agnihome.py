import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image as image
from tkinter import filedialog
import files_and_folder as filefold
import warnings
warnings.filterwarnings('ignore')

# import  faf_scan as fsc

window = Tk()
window.title('AGNI AntiVirus')

# global Widgets
asset_path = Label()
scan_button = Button()
path = ''
correct = Label()
wrong = Label()
progressbar = ttk.Progressbar()
file_name_holder = Label()
border = Frame()
frame1 = Label()
frame2 = Label()
frame3 = Button()


# progress = 0


# File Browser
def browseFiles():
    global border
    global correct
    global wrong
    border.place_forget()
    correct.place_forget()
    wrong.place_forget()
    global path
    global progressbar
    global file_name_holder
    file_location = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                               filetypes=(("Text files", "*.*"), ("all files", "*.*")))
    path = file_location
    asset_path.configure(text=path)
    scan_button['state'] = NORMAL
    progressbar.place(x=49, y=240)
    file_name_holder['text'] = path


# Folder Browser
def browseFolder():
    global path
    global border
    global correct
    global wrong
    border.place_forget()
    correct.place_forget()
    wrong.place_forget()
    filename = filedialog.askdirectory()
    print(filename)
    path = filename
    asset_path.configure(text=path)
    scan_button['state'] = NORMAL
    progressbar.place(x=49, y=240)


def folder_scan():
    row = 0
    global path
    global progressbar
    global correct
    global wrong
    global asset_path
    global file_name_holder
    global border
    global frame1
    global frame2
    global frame3

    files = os.listdir(path)
    border.place(x=49, y=290)
    file_name_holder.place(x=55, y=264)
    for file in files:
        progressbar['value'] = 0
        realpath = path + '\\' + file
        file_name_holder['text'] = realpath
        filefold.scan_sha1(realpath)
        if filefold.proceed == 0:
            progressbar['value'] = 30
            progressbar.update()

            filefold.scan_md5(realpath)
            if filefold.proceed == 1:
                progressbar['value'] = 50
                progressbar.update()

                filefold.scan_sha256(realpath)
                if filefold.proceed == 2:
                    progressbar['value'] = 100
                    progressbar.update()

                    frame1 = Label(border, text=realpath, width=65, background='#ffffff')
                    frame1.grid(row=row, column=0, sticky='WENS')
                    frame2 = Label(border, text='File is safe', width=35, background='#ffffff')
                    frame2.grid(row=row, column=1, sticky='WENS')
                    # frame3 = Button(border, text='virus found', width=20, bd=0, highlightthickness=0, background='#DB3D4D', fg='white')
                    # frame3.grid(row=row, column=2, sticky='WENS')

                    row = row + 1

                    print('File is safe')
                else:
                    # wrong.place(x=314, y=311)
                    print('FIle is Unsafe')
                    frame1 = Label(border, text=realpath, width=65, background='#ffffff')
                    frame1.grid(row=row, column=0, sticky='WENS')
                    frame2 = Label(border, text='Virus found', width=35, background='#ffffff')
                    frame2.grid(row=row, column=1, sticky='WENS')
                    frame3 = Button(border, text='DELETE', width=20, bd=0, highlightthickness=0, background='#DB3D4D',
                                    fg='white')
                    frame3.grid(row=row, column=2, sticky='WENS')
            else:
                # wrong.place(x=314, y=311)
                print('FIle is Unsafe')
                frame1 = Label(border, text=realpath, width=65, background='#ffffff')
                frame1.grid(row=row, column=0, sticky='WENS')
                frame2 = Label(border, text='Virus found', width=35, background='#ffffff')
                frame2.grid(row=row, column=1, sticky='WENS')
                frame3 = Button(border, text='DELETE', width=20, bd=0, highlightthickness=0, background='#DB3D4D',
                                fg='white')
                frame3.grid(row=row, column=2, sticky='WENS')
        else:
            # wrong.place(x=314, y=311)
            print('FIle is Unsafe')
            frame1 = Label(border, text=realpath, width=65, background='#ffffff')
            frame1.grid(row=row, column=0, sticky='WENS')
            frame2 = Label(border, text='Virus found', width=35, background='#ffffff')
            frame2.grid(row=row, column=1, sticky='WENS')
            frame3 = Button(border, text='DELETE', width=20, bd=0, highlightthickness=0, background='#DB3D4D',
                            fg='white')
            frame3.grid(row=row, column=2, sticky='WENS')
    asset_path['text'] = ''
    progressbar.place_forget()
    file_name_holder.place_forget()
    scan_button['state'] = DISABLED


def file_scan():
    global progressbar
    global correct
    global wrong
    global asset_path
    global file_name_holder
    progressbar['value'] = 0
    filefold.scan_sha1(path)
    if filefold.proceed == 0:
        progressbar['value'] = 30
        progressbar.update()

        filefold.scan_md5(path)
        if filefold.proceed == 1:
            progressbar['value'] = 50
            progressbar.update()

            filefold.scan_sha256(path)
            if filefold.proceed == 2:
                progressbar['value'] = 100
                progressbar.update()
                correct.place(x=314, y=311)
                asset_path['text'] = ''
                progressbar.place_forget()
                file_name_holder.place_forget()
                print('File is safe')
            else:
                progressbar.place_forget()
                wrong.place(x=314, y=311)
                print('FIle is Unsafe')
        else:
            progressbar.place_forget()
            wrong.place(x=314, y=311)
            print('FIle is Unsafe')
    else:
        progressbar.place_forget()
        wrong.place(x=314, y=311)
        print('FIle is Unsafe')


def scan():
    global path
    if os.path.isdir(path):
        folder_scan()
    else:
        file_scan()


# Image for File and Folder Scan
bg_image_faf = ImageTk.PhotoImage(image.open('Images\\FAF\\faf.png').resize((940, 650), image.ANTIALIAS))
scan_button_image = ImageTk.PhotoImage(image.open('Images\\FAF\\sacnButton.png').resize((219, 63), image.ANTIALIAS))
correct_image = ImageTk.PhotoImage(image.open('Images\\FAF\\correct.png').resize((308, 205), image.ANTIALIAS))
wrong_image = ImageTk.PhotoImage(image.open('Images\\FAF\\wrong.png').resize((308, 225), image.ANTIALIAS))
browse_files_image = ImageTk.PhotoImage(image.open('Images\\FAF\\browse file.png').resize((190, 44), image.ANTIALIAS))
browse_folder_image = ImageTk.PhotoImage(
    image.open('Images\\FAF\\browse folder.png').resize((220, 44), image.ANTIALIAS))


# Files and Folder -> The code for Files and Folder
def start_faf():
    file_folder = Toplevel()
    file_folder.title("AGNI Antivirus")
    width_faf = 940
    height_faf = 650
    screen_height_faf = file_folder.winfo_screenheight()
    screen_width_faf = file_folder.winfo_screenwidth()
    center_x_faf = int((screen_width_faf / 2) - width_faf / 2)
    center_y_faf = int((screen_height_faf / 2) - height_faf / 2)

    file_folder.geometry(f'{width_faf}x{height_faf}+{center_x_faf}+{center_y_faf}')
    bg_label_faf = Label(file_folder, image=bg_image_faf)
    bg_label_faf.place(x=0, y=0, relwidth=1, relheight=1)
    global asset_path
    asset_path = Label(file_folder, background='#ffffff', bd=0, highlightthickness=0, width=87, height=3)
    asset_path.place(x=49, y=100)
    global scan_button
    scan_button = Button(file_folder, image=scan_button_image, bd=0, highlightthickness=0, command=scan)
    scan_button.place(x=692, y=100)
    scan_button['state'] = DISABLED
    browse_file = Button(file_folder, image=browse_files_image, bd=0, highlightthickness=0, command=browseFiles)
    browse_file.place(x=49, y=154)

    browse_folder = Button(file_folder, image=browse_folder_image, bd=0, highlightthickness=0, command=browseFolder)
    browse_folder.place(x=250, y=154)

    global progressbar
    progressbar = ttk.Progressbar(file_folder, orient=HORIZONTAL, length=862)
    # progressbar.place(x=49, y=240)
    global file_name_holder
    file_name_holder = Label(file_folder, background='#ffffff')
    # file_name_holder.place(x=55, y=264)

    global correct
    correct = Label(file_folder, image=correct_image, bd=0, highlightthickness=0)
    # correct.place(x=314, y=311)
    global wrong
    wrong = Label(file_folder, image=wrong_image, bd=0, highlightthickness=0)
    # wrong.place(x=314, y=311)
    global border
    border = Frame(file_folder, height=282, width=862, background='#ffffff')
    # border.place(x=49, y=280)
    # frame1 = Label(border, text='hello world', width=65, background='#ffffff')
    # frame1.grid(row=0, column=0, sticky='WENS')
    # frame2 = Label(border, text='virus found', width=35, background='#ffffff')
    # frame2.grid(row=0, column=1, sticky='WENS')
    # frame3 = Button(border, text='virus found', width=20, bd=0, highlightthickness=0, background='#DB3D4D', fg='white')
    # frame3.grid(row=0, column=2, sticky='WENS')

    file_folder.resizable(False, False)


# UPDATE -> The code for the Update Manger


def start_update():
    def delay():
        for i in range(1000):
            for j in range(1000):
                c = i + j

    def start():
        nonlocal label
        nonlocal button
        for i in range(0, 101, 4):
            bar['value'] = i
            bar.update()
            delay()
        label['text'] = 'No Updates available'
        button['text'] = 'Download'
        button['state'] = DISABLED

    win = Toplevel()
    win.title("AGNI Antivirus update manager")
    win.geometry('500x100')
    frame1 = Frame(win)
    frame1.grid(row=0, column=0, sticky='WENS')
    bar = ttk.Progressbar(frame1, orient=HORIZONTAL, length=400)
    bar.grid(row=0, column=0)
    label = Label(frame1, text='Checking for Updates')
    label.grid(row=1, column=0)
    frame1.rowconfigure(0, weight=2)
    frame1.rowconfigure(1, weight=1)
    frame1.columnconfigure(0, weight=1)
    frame2 = Frame(win)
    frame2.grid(row=1, column=0, sticky='WENS')
    button = Button(frame2, text='CHECK', command=start)
    button.grid(row=0, column=0)
    frame2.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=3)
    win.rowconfigure(1, weight=2)
    win.columnconfigure(0, weight=1)


width = 940
height = 650
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
center_x = int((screen_width / 2) - width / 2)
center_y = int((screen_height / 2) - height / 2)

window.geometry(f'{width}x{height}+{center_x}+{center_y}')
bg_image = ImageTk.PhotoImage(image.open('Images\\HOME\\Antivirus Home.jpg').resize((940, 650), image.ANTIALIAS))
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

tuner = ImageTk.PhotoImage(image.open('Images\\HOME\\Tuner.jpg').resize((189, 189), image.ANTIALIAS))
tuner_button = Button(window, image=tuner, bd=0, highlightthickness=0)
tuner_button.place(x=46, y=285)

faf = ImageTk.PhotoImage(image.open('Images\\HOME\\faf.jpg').resize((189, 189), image.ANTIALIAS))
faf_button = Button(window, image=faf, bd=0, highlightthickness=0, command=start_faf)
faf_button.place(x=265, y=285)

net = ImageTk.PhotoImage(image.open('Images\\HOME\\Net.jpg').resize((189, 189), image.ANTIALIAS))
net_button = Button(window, image=net, bd=0, highlightthickness=0)
net_button.place(x=487, y=285)

lock = ImageTk.PhotoImage(image.open('Images\\HOME\\Lock.jpg').resize((189, 189), image.ANTIALIAS))
lock_button = Button(window, image=lock, bd=0, highlightthickness=0)
lock_button.place(x=705, y=285)

update = ImageTk.PhotoImage(image.open('Images\\HOME\\update.jpg').resize((248, 68), image.ANTIALIAS))
update_button = Button(window, image=update, bd=0, highlightthickness=0, command=start_update)
update_button.place(x=649, y=517)

window.resizable(False, False)
window.mainloop()
