from tkinter import *
from tkinter import messagebox
import mysql.connector as pymysql

# Add your own database name and password here to reflect in the code

con = pymysql.connect(host="localhost", user="root", password='root', database='a12', auth_plugin='mysql_native_password')
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

# List To store all Book IDs
allBid = []


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status, check

    bid = int(inf1.get())
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from " + bookTable
    try:
        cur.execute(extractBid)
        result = cur.fetchall()
        for i in result:
            allBid.append(i[0])
            print(allBid)

        if bid in allBid:
            print(bid)
            checkAvail = f"select status from {bookTable}  where bid = {bid}"
            cur.execute(checkAvail)
            result = cur.fetchall()
            print(result)
            check = result[0][0]
            print(check)

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = f"INSERT INTO {issueTable} VALUES ({bid}, '{issueto}')"

    updateStatus = f"update {bookTable} set status = 'issued' where bid = {bid}"
    get_issued_to = f"select bi.IssuedTo" \
                    f" from {issueTable} bi,{bookTable} b " \
                    f"where bi.BookID=b.BID and status = 'issued' and BID ={bid}"
    try:
        if status:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            cur.execute(get_issued_to)
            issue_to = cur.fetchone()
            messagebox.showinfo('Success', f"Book Issued Successfully to {issue_to[0].upper()}")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(bid)
    print(issueto)

    allBid.clear()


def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name 
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
