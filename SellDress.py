from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code


con = pymysql.connect(host="localhost",user="root",password='<password>',database='mydatabase')
cur = con.cursor()
  



def issue():

    bid = inf1.get()
    soldto = inf2.get()


    extractBid = "select * from dressTable where DRESS_CODE = '"+bid+"'"

    try:
        cur.execute(extractBid)
        con.commit()
        count=cur.rowcount


        if(count>0):
            sell = "delete from dressTable where DRESS_CODE = '"+bid+"'"
            cur.execute(sell)
            con.commit()

            issueSql = "insert into soldTable values ('"+bid+"','"+soldto+"')"
            # show = "select * from soldTable"

            cur.execute(issueSql)
            con.commit()
            # cur.execute(show)
            # con.commit()
            messagebox.showinfo('Success',"Dress Sold Successfully")

            root.destroy()

        else:
            messagebox.showinfo("Error","DressCode not present")

    except:
        messagebox.showinfo("Error","Can't fetch Dress Codes")
    
    print(bid)
    print(soldto)

    allBid.clear()

    
def SellDress(): 
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status

    root = Tk()
    root.title("LUSH BERRY")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Sell a Dress", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Dress Code
    lb1 = Label(labelFrame,text="Dress Code : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    # Sold To 
    lb2 = Label(labelFrame,text="Sold To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)


    #Sell Button
    issueBtn = Button(root,text="Sell",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

