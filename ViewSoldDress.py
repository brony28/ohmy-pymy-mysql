from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code

con = pymysql.connect(host="localhost",user="root",password='<password>',database='mydatabase')
cur = con.cursor()


def ViewSoldDress(): 

    root = Tk()
    root.title("LUSH BERRY")
    root.minsize(width=400,height=400)
    root.geometry("700x600")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Sold Dress", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)

    y = 0.25

    # Label(labelFrame, text="%-10s %-50s %-40s %-20s %-20s\n"%('Code','Type','Category','Size','Price'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="{0:<7}{1:<51}\n".format('ID','Sold To'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    getSoldDress = "select * from soldTable"

    try:
        cur.execute(getSoldDress)
        con.commit()

        for i in cur:
            # Label(labelFrame, text="%-10s %-50s %-40s %-20s %-20s\n"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white').place(relx=0.07,rely=y)
            Label(labelFrame, text="{0:<7}{1:<51}\n".format(i[0],i[1]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

