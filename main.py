
from PIL import Image, ImageTk
import PIL
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
import mysql.connector as pymysql
from tkinter import *

con = pymysql.connect(host="localhost", user="root", password='root', database='a12',
                      auth_plugin='mysql_native_password')
cur = con.cursor()
qry = "CREATE DATABASE IF NOT EXISTS a12"
cur.execute(qry)
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
# root.maxsize(width=654, height=500)
root.geometry("600x500")

# use this if the above given PIL lib won't work as it doesn't work sometimes depending on versions
# Take n greater than 0.25 and less than 5
# same = True
# n = 0.25
# Adding a background image
# background_image = Image.open("lib.jpg")

'''newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
print(newImageSizeWidth)
print(newImageSizeHeight)'''
# background_image = background_image.resize((imageSizeWidth, imageSizeHeight), Image.Resampling.LANCZOS)
imgb = PIL.Image.open("lib.jpg")
img = ImageTk.PhotoImage(imgb)

Canvas1 = Canvas(root)

Canvas1.create_image(350, 250, image=img)
Canvas1.config(bg="black", width=1770, height=10)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n DC Library", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

menubar = Menu(root, background='blue', fg='white')

credits = Menu(menubar, tearoff=False, background='#f45c43')
menubar.add_cascade(label="Credits", menu=credits)
credits.add_command(label='Savitender Singh', background='yellow', command=None)
credits.add_command(label='Sarthak Gomber', background='#ef629f', command=None)

credits.add_separator()
credits.add_command(label='Exit', command=root.destroy)

root.config(menu=menubar)
root.mainloop()
