from random import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector


def encrypt(text,key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        k = (2 * ord(key[i])) + i
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    for i in range(len(text)):
        if (char.isupper()):
            s = randrange(65,91)
        else :
            s=randrange(97,123)
        result += chr(s)
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='SEPM'
    )
    cursor = db.cursor()
    sql = "INSERT INTO encryptiondata(data, keydata, encrypt) VALUES (%s,%s,%s)"
    val = (text, key, result)
    cursor.execute(sql,val)
    db.commit()
    db.close()
    return result


def decrypt(a, key):
    result = ""

    # traverse text
    for i in range(len(a)-len(key)):
        char = a[i]
        k = (2*ord(key[i])) + i
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - k - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)

    return result

def encryptbutton():
    def encryptdo():
        a = str(entrye1.get())
        b = str(entrye2.get())
        e = encrypt(a, b)
        print(e)
        t = StringVar()
        t.set(e)
        messagebox.showinfo("DATA",t.get())
        r.destroy()
    r=Toplevel()
    r.title("ENCRYPTION")
    labele1 = Label(r, text="TEXT")
    entrye1 = Entry(r)
    labele1.grid(padx=10,pady=10, row=0, column=0)
    entrye1.grid(padx=10,pady=10, row=0, column=2)
    labele2 = Label(r, text="KEY")
    entrye2 = Entry(r)
    labele2.grid(padx=10, pady=10, row=1, column=0)
    entrye2.grid(padx=10, pady=10, row=1, column=2)
    buttone = Button(r, text="ENCRYPT",activebackground='green', width=25, command=encryptdo)
    buttone.grid(padx=10, pady=10, row=2, column=1)

def decryptbutton():
    def decryptdo():
        a = str(entryd1.get())
        b = str(entryd2.get())
        e = decrypt(a, b)

        t = StringVar()
        t.set(e)
        messagebox.showinfo("DATA", t.get())
        r1.destroy()
    r1=Toplevel()
    r1.title("DECRYPTION")
    labeld1 = Label(r1, text="TEXT")
    entryd1 = Entry(r1)
    labeld1.grid(padx=10, pady=10, row=0, column=0)
    entryd1.grid(padx=10, pady=10, row=0, column=2)
    labeld2 = Label(r1, text="KEY")
    entryd2 = Entry(r1)
    labeld2.grid(padx=10, pady=10, row=1, column=0)
    entryd2.grid(padx=10, pady=10, row=1, column=2)
    buttond = Button(r1, text="DECRYPT",activebackground='green', width=25, command=decryptdo)
    buttond.grid(padx=10, pady=10, row=2, column=1)

'''db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='SEPM'
)
cursor = db.cursor()
sql = "DROP TABLE encryptiondata"
cursor.execute(sql)'''
root = Tk()
root.title("SAC")
image1=ImageTk.PhotoImage(Image.open("D:\SEPM\logo.PNG"))
root.iconphoto(False,image1)
image=ImageTk.PhotoImage(Image.open("D:\SEPM\kali.png"))
button1 = Button(root,activebackground='green', text="ENCRYPTION", width=50, command=encryptbutton)
button2 = Button(root,activebackground='green', text="DECRYPTION", width=50, command=decryptbutton)
button3 = Button(root,activebackground='red', text="EXIT", width=25, command=root.destroy)
panel1 = Label(root, image=image)
button1.pack(padx=10, pady=10)
button2.pack(padx=10, pady=10)
panel1.pack(side='top', fill='both', expand='yes')
button3.pack(padx=10, pady=10)

panel1.image = image
root.mainloop()

