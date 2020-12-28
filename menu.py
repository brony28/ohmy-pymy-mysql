from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

from AddDress import *
from DeleteDress import *
from ViewDress import *
from SellDress import *
from ViewSoldDress import *

def library():   
    root = Tk()   
    root.title("LUSH BERRY")  
    root.minsize(width=400,height=400)  
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code  

    con = pymysql.connect(host="localhost",user="root",password='<password>',database='mydatabase')  
    cur = con.cursor() 

    # Take n greater than 0.25 and less than 5    
    same=True
    n=0.25

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n LUSH bury CLOSET", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Dress Details",bg='black', fg='white', command=AddDress)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Dress",bg='black', fg='white', command=DeleteDress)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Dresses",bg='black', fg='white', command=ViewDress)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Sell Dress",bg='black', fg='white', command = SellDress)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Return Dress",bg='black', fg='white', command = ViewSoldDress)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    
    root.mainloop()
