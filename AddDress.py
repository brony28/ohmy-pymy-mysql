from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def DressRegister():
    DRESS_CODE = dressInfo1.get()
    TYPE = dressInfo2.get()
    CATEGORY = dressInfo3.get()
    SIZE = dressInfo4.get()
    PRICE = dressInfo5.get()
    insertDress = "insert into dressTable values('"+DRESS_CODE+"','"+TYPE+"','"+CATEGORY+"','"+SIZE+"','"+PRICE+"')"
    # 'dressTable' is the name of the TABLE present in 'mydatabase' DATABASE.
    try:
        cur.execute(insertDress)
        con.commit()
        messagebox.showinfo('Success',"Dress added successfully")
    except:        
        messagebox.showinfo("Error","Can't add data into Database")
        print(DRESS_CODE)
        print(TYPE)
        print(CATEGORY)
        print(SIZE)
        print(PRICE)
    root.destroy()

def AddDress():         
    global dressInfo1,dressInfo2,dressInfo3,dressInfo4,dressInfo5,Canvas1,con,cur,root

    root = Tk()
    root.title("LUSH BERRY")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    # Add your own database name and password here to reflect in the code
    con = pymysql.connect(host="localhost",user="root",password='<password>',database='mydatabase')
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Dress to Collection", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Dress ID    
    lb1 = Label(labelFrame,text="Dress ID : ", bg='black', fg='white')    
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)            
    dressInfo1 = Entry(labelFrame)    
    dressInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # TYPE
    lb2 = Label(labelFrame,text="TYPE : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
    dressInfo2 = Entry(labelFrame)
    dressInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Dress CATEGORY
    lb3 = Label(labelFrame,text="CATEGORY : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    dressInfo3 = Entry(labelFrame)
    dressInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Dress Size
    lb4 = Label(labelFrame,text="SIZE : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    dressInfo4 = Entry(labelFrame)
    dressInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Dress Price
    lb5 = Label(labelFrame,text="PRICE : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
    dressInfo5 = Entry(labelFrame)
    dressInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=DressRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()