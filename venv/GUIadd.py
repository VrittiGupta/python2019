from tkinter import *
from tkinter import Radiobutton

import mysql.connector


def onClick():

    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()
    print(name, phone, email)


    sql = "insert into customer values(null, '{}', '{}', '{}')".format(name,phone,email)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="vripy")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(name," Saved in DataBase")

def click1():
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()


    cid=entrycid.get()


    sql = "delete from customer where cid = {}".format(cid)

    print(sql)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="vripy")

    cursor = con.cursor()
    cursor.execute(sql)

    con.commit()
    print(">> ", cid, "Deleted !!")
def click2():
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()


    sql = "select * from customer "

    print(sql)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="vripy")

    cursor = con.cursor()
    cursor.execute(sql)

    row = cursor.fetchall()
    print(row)
def click3():
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()
    cid=entrycid.get()

    sql="Update customer set name='{}',phone='{}',email='{}' where cid ='{}'".format(name,phone,email,cid)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="vripy")

    cursor = con.cursor()
    cursor.execute(sql)
    print(name," updated in database")

def r1():
    entryname.config(state=NORMAL)
    entryemail.config(state=NORMAL)
    entryphone.config(state=NORMAL)

    radio2.config(state=DISABLED)
    radio3.config(state=DISABLED)
    radio4.config(state=DISABLED)
def r2():

    entrycid.configure(state="normal")
    entryname.configure(state="disabled")
    entryemail.configure(state="disabled")
    entryphone.configure(state="disabled")
    radio1.config(state=DISABLED)
    radio3.config(state=DISABLED)
    radio4.config(state=DISABLED)

def r3():
    entrycid.configure(state="disabled")
    entryname.configure(state="disabled")
    entryemail.configure(state="disabled")
    entryphone.configure(state="disabled")
    radio2.config(state=DISABLED)
    radio1.config(state=DISABLED)
    radio4.config(state=DISABLED)

def r4():
    entrycid.configure(state="normal")
    entryname.configure(state="normal")
    entryphone.configure(state="normal")
    entryemail.configure(state="normal")
    radio2.config(state=DISABLED)
    radio3.config(state=DISABLED)
    radio1.config(state=DISABLED)


global window
window= Tk()
global entryemail
global entryphone
global entryemail
global entrycid


global radio1
global radio2
global radio3
global radio4



radio1=Radiobutton(window,text="Save",command =r1)
radio1.pack()
radio2=Radiobutton(window,text="Delete",command=r2)
radio2.pack()
radio3=Radiobutton(window,text="View",command=r3)
radio3.pack()
radio4=Radiobutton(window,text="Update",command=r4)
radio4.pack()

lbltitle=Label(window,text="Customer Record")
lbltitle.pack()
lblname=Label(window,text="Enter the Name")
lblname.pack()
entryname=Entry(window,state=DISABLED)
entryname.pack()
lblphone=Label(window,text="Enter the Phone")
lblphone.pack()
entryphone=Entry(window,state=DISABLED)
entryphone.pack()
lblemail=Label(window,text="Enter the Email")
lblemail.pack()
entryemail=Entry(window,state=DISABLED)
entryemail.pack()
lblcid=Label(window,text="Enter the Customer ID")
lblcid.pack()
entrycid=Entry(window,state=DISABLED)
entrycid.pack()





btnSave = Button(window, text="Save Customer", command=onClick)
btnSave.pack()
btnDelete = Button(window, text="Delete Customer", command=click1)
btnDelete.pack()
btnView = Button(window, text="View Customer", command=click2)
btnView.pack()
btnUpdate= Button(window, text="Update Customer", command=click3)
btnUpdate.pack()


window.mainloop()