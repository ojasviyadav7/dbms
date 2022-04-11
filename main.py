from tkinter import *
import sqlite3
from tkinter import messagebox as msgbox

window = Tk()

window.title("Login")
window.geometry("1280x960")
window.config(bg="#faf3e0")


def con(a):
    a.config(bg="#faf3e0")


def b(j):
    j.config(bg="pink")


user = Label(window, text="Username", font=(5))
user.place(x=560, y=220, width=120)
con(user)

pw = Label(window, text="Passcode", font=(2))
pw.place(x=560, y=250, width=120)
con(pw)

u = Entry(window, width=50)
u.place(x=670, y=230, width=120, height=30)
b(u)
p = Entry(window, show="*", width=50)
p.place(x=670, y=255, width=120, height=30)
b(p)


def logintodb():
    if u.get() == "admin" and p.get() == "kekw":
        print("Access Granted!")
        root = Tk()
        root.geometry('659x659')
        e = Label(root, text="Enter Name").grid(row=0, column=0)
        pla = Label(root, text="Enter place").grid(row=1, column=0)
        kla = Label(root, text="Enter mobile").grid(row=2, column=0)
        fla = Label(root, text="Enter email address").grid(row=3, column=0)
        gla = Label(root, text="Enter AADHAAR").grid(row=4, column=0)
        jla = Label(root, text="Enter PAN CARD").grid(row=5, column=0)
        ola = Label(root, text="Enter Gender").grid(row=6, column=0)
        h = Entry(root, width=20)
        h.grid(row=0, column=1)
        e2 = Entry(root, width=20)
        e2.grid(row=1, column=1)
        e3 = Entry(root, width=20)
        e3.grid(row=2, column=1)
        e4 = Entry(root, width=20)
        e4.grid(row=3, column=1)
        e5 = Entry(root, width=20)
        e5.grid(row=4, column=1)
        e6 = Entry(root, width=20)
        e6.grid(row=5, column=1)
        e7 = Entry(root, width=20)
        e7.grid(row=6, column=1)

        def database():
            a = h.get()
            b = e2.get()
            c = e3.get()
            d = e4.get()
            e = e5.get()
            f = e6.get()
            o = e7.get()
            db = sqlite3.connect("miniproject.db")
            conn = db.cursor()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS HOTEL(NAME TEXT NOT NULL,PLACE TEXT NOT NULL,MOBILE TEXT NOT NULL,EMAILADDRESS TEXT NOT NULL,AADHAAR TEXT NOT NULL,PANCARD TEXT NOT NULL,GENDER TEXT NOT NULL)")
            conn.execute(
                "INSERT INTO HOTEL(NAME,PLACE,MOBILE,EMAILADDRESS,AADHAAR,PANCARD,GENDER) VALUES(?,?,?,?,?,?,?)",
                (a, b, c, d, e, f, o))

            msg = msgbox.showinfo("Status", " successfully added to database")
            cur = conn.execute("SELECT * FROM HOTEL")
            for row in cur:
                print(row)
            db.commit()
            db.close()

        s = Button(root, text="Add data", command=database).grid(row=8, column=1)
        root.mainloop()










    else:
        msg = msgbox.showinfo("status", "wrong credentials")


log = Button(text="Login", font=(0.5), command=logintodb)
log.place(x=650, y=290, width=80, height=25)
log.config(bg="#f4d160")

window.mainloop()