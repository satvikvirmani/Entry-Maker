
#Import Packages

from tkinter import ttk
from tkinter import *
from random import randint
import tkinter as tk
from tkinter import messagebox
import webbrowser

#Initialise dictionary

database = dict()

#Function to raise frame

def raise_frame(frame):
    frame.tkraise()

#Write details Function
    
def update_frame(frame):
    name = enter_name.get()
    age = enter_age.get()
    if var_gender.get() == 1:
        gender = "Male"
    elif var_gender.get() == 2:
        gender = "Female"
    else :
        gender = "Other"
    if var_stream.get() == 1:
        stream = "B-Tech"
    elif var_stream.get() == 2:
        stream = "B-Arc."
    else:
        stream = "Other"
    email = enter_mail.get()
    studentdetaillist = [name, age, gender]
    password = randint(10000000,99999999)
    if name != "" and age != "" and gender != "" and email != "":
        with open("Record.txt","r") as pass_check:
            for password in pass_check.read():
                password = randint(10000000,99999999)
        with open("Record.txt", "a") as storage:
            storage.write("Name["+str(password)+"] : "+name+"\n")
            storage.write("Age["+str(password)+"] : "+age+"\n")
            storage.write("Gender["+str(password)+"] : "+gender+"\n")
            storage.write("Stream["+str(password)+"] : "+stream+"\n")
            storage.write("E-Mail["+str(password)+"] : "+email+"\n")
            storage.close()
        label_show = Label(show_frame, text='Student Added', font=("Verdana", 12))
        label_show.place(x=185,y=0)
        pass_show = "Your password : "+ str(password)
        label_show_pass = Label(frame, text=pass_show, font=("Tahoma", 12))
        label_show_pass.place(x=150, y=50)
        label_show_note = Label(frame, text='(Please remember your password)', fg='red')
        label_show_note.place(x=155, y=75)
        database[password] = studentdetaillist
    if name == "" or age == "" or gender == "" or email == "":
        lab = Label(frame, text='          Invalid details           \n     \n                                            \n                                     \n                                     ', font=("Tahoma", 12))
        lab.place(x=150,y=0)
    back_btnr = ttk.Button(frame, text="Back",  width=10, image=photo_back, compound=LEFT, command=lambda: raise_frame(Home))
    back_btnr.place(x=383,y=216)
    enter_name.delete(first=0, last=200)
    enter_age.delete(first=0, last=200)
    frame.tkraise()

#Check Details Function
    
def check_show(frame):
    read_detail = open("Record.txt", "r")
    check = False
    count = 25
    if enter_pass.get() != "" and len(enter_pass.get())==8:
        for line in read_detail:
            if enter_pass.get() in line:
                replacement = "[" + enter_pass.get() + "]"
                replaced_text = line.replace(replacement, "")
                rep2= replaced_text + "                                                                               "
                l2 = Label(frame, text=rep2, font=("Tahoma", 12))
                l2.place(x=40, y=0+count)
                count = count+25
                check = True
    if enter_pass.get() == "":
        l23 = Label(frame, text='                              Enter a valid roll no.!               \n                                                                                       \n                                                                                       \n                                                                                       \n                                                                                       \n                                                                                       ', font=("Tahoma", 12))
        l23.place(x=0,y=20)
    elif check == False:
        l1 = Label(frame, text='                   No student with specified rollnumber found!               \n                                                                                       \n                                                                                       \n                                                                                       \n                                                                                       \n                                                                                                           ', font=("Tahoma", 12))
        l1.place(x=0,y=20)
    back_btn5 = ttk.Button(frame, text="Back",  width=10, image=photo_back, compound=LEFT, command=lambda: raise_frame(Home))
    back_btn5.place(x=383,y=216)
    read_detail.close()
    enter_pass.delete(first=0, last=200)
    frame.tkraise()

#Exit Function

def verify_dialog():
        msg = tk.messagebox.askquestion('WE Databases', 'Are you sure you want to exit?',icon='warning')
        if msg == 'yes':
            root.destroy()
        
def open_about():
	webbrowser.open('https://www.python.org')
#Declare Window

root = Tk()
root.geometry('500x270')
root.resizable(0, 0)
root.title('WE Databases')
root.iconphoto(False, tk.PhotoImage(file = r"book.png"))

#Declare Frame

Home = Frame(root)
entry_frame = Frame(root)
check_frame = Frame(root)
show_frame = Frame(root)
check_frame = Frame(root)
check_frame_display = Frame(root)
forgot_pass = Frame(root)

#Set frame grid

for F in (Home, entry_frame, check_frame, show_frame, check_frame_display, forgot_pass):
    F.grid(row=0, column=0, sticky='news')

#Set icon in buttons

photo_add = PhotoImage(file = r"add.png") 
photoimage = photo_add.subsample(3, 3) 
photo_check = PhotoImage(file = r"check.png")
photoimage = photo_check.subsample(3, 3)
photo_next = PhotoImage(file = r"next.png")
photoimage = photo_next.subsample(3, 3)
photo_back = PhotoImage(file = r"back.png")
photoimage = photo_back.subsample(3, 3)
photo_exit = PhotoImage(file = r"exit.png")
photoimage = photo_back.subsample(3, 3)



#Declare labels

label_main = Label(Home, text='Student Record Entry', font=("Verdana", 12))
label_main.pack(side=TOP, padx=150)
label_entry = Label(entry_frame, text='Student Entry', font=("Baskerville Old Face", 22))
label_entry.place(x=185,y=0)
label_pgtwo = Label(check_frame, text='Check details', font=("Baskerville Old Face", 22))
label_pgtwo.place(x=185,y=0)

#entry_frame configuration

label_name = Label(entry_frame, text='Name : ', font=("Verdana", 11))
label_name.place(x=20,y=60)
label_age = Label(entry_frame, text='Age : ', font=("Verdana", 11))
label_age.place(x=20,y=85)
label_stream = Label(entry_frame, text='Stream : ', font=("Verdana", 11))
label_stream.place(x=20, y=135)
label_gender = Label(entry_frame, text='Gender : ', font=("Verdana", 11))
label_gender.place(x=20,y=110)
label_mail = Label(entry_frame, text='E-Mail : ', font=("Verdana", 11))
label_mail.place(x=20, y=162)

enter_name = ttk.Entry(entry_frame, width=35)
enter_name.place(x=100,y=62)
enter_age = ttk.Entry(entry_frame, width=35)
enter_age.place(x=100,y=87)
enter_mail = ttk.Entry(entry_frame, width=35)
enter_mail.place(x=100, y=162)
#Radiobuttons configuration

var_gender = IntVar()
male_btn = ttk.Radiobutton(entry_frame, text='Male', variable=var_gender, value=1)
female_btn = ttk.Radiobutton(entry_frame, text='Female', variable=var_gender, value=2)
other_btn = ttk.Radiobutton(entry_frame, text='Other', variable=var_gender, value=3)
male_btn.place(x=100, y=112)
female_btn.place(x=170, y=112)
other_btn.place(x=240, y=112)

var_stream = IntVar()
btech = ttk.Radiobutton(entry_frame, text='B-Tech.', variable=var_stream, value=1)
barc = ttk.Radiobutton(entry_frame, text='B-Arc.', variable=var_stream, value=2)
phd = ttk.Radiobutton(entry_frame, text='PHD.', variable=var_stream, value=3)
btech.place(x=100, y=137)
barc.place(x=170, y=137)
phd.place(x=240, y=137)

next_btn = ttk.Button(entry_frame, text="Next",  width=10, image=photo_next, compound=RIGHT, command=lambda: update_frame(show_frame))
next_btn.pack(side=RIGHT, pady=215)
back_btn = ttk.Button(entry_frame, text="Back",  width=10, image=photo_back, compound=LEFT, command=lambda: raise_frame(Home))
back_btn.pack(side=RIGHT, pady=215, padx=5)

#check_frame configuration

label_pass = ttk.Label(check_frame, text='Password : ', font=("Verdana", 11))
label_pass.place(x=20,y=60)
enter_pass = ttk.Entry(check_frame, width=35)
enter_pass.place(x=110,y=62)
next_btn1 = ttk.Button(check_frame, text="Next", width=10, image=photo_next, compound=RIGHT, command=lambda: check_show(check_frame_display))
next_btn1.pack(side=RIGHT)
back_btn1 = ttk.Button(check_frame, text="Back", width=10, image=photo_back, compound=LEFT, command=lambda: raise_frame(Home))
back_btn1.pack(side=RIGHT)

#Declare button

new_stu_btn = ttk.Button(Home, text='  Add a new student  ', width=20, image=photo_add, compound= RIGHT, command=lambda: raise_frame(entry_frame))
new_stu_btn.pack(pady=2)
check_stu_btn = ttk.Button(Home, text='Check student details',  width=20, image=photo_check, compound= RIGHT, command=lambda: raise_frame(check_frame))
check_stu_btn.pack(pady=2)
exit_btn = ttk.Button(Home, text='                Exit               ', width=20, image=photo_exit, compound=RIGHT, command=verify_dialog)
exit_btn.pack(pady=2)

#Declare Menu

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Actions', menu=filemenu)
filemenu.add_command(label='Add a Student', command=lambda: raise_frame(entry_frame))
filemenu.add_command(label='Check Details', command=lambda: raise_frame(check_frame))
filemenu.add_separator()
filemenu.add_command(label='Exit', command=verify_dialog)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=open_about)

root.protocol("WM_DELETE_WINDOW", verify_dialog)

#Raise Initial frame and window

Home.tkraise()
root.mainloop()
