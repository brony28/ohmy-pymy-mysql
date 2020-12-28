from tkinter import *

from PIL import ImageTk,Image

from tkinter import messagebox

import pymysql



from menu import *



# Add your own database name and password here to reflect in the code


con = pymysql.connect(host="localhost",user="root",password='<password>',database=mydatabase)
cur = con.cursor()







def checkLogin():

    uname = userName.get()
    pwd = password.get()

    
    loginSql = "select username,password from "+loginTable+" where username = '"+uname+"' and password = '"+pwd+"';"

    cur.execute(loginSql)
    count=cur.rowcount

    if count>0:
        messagebox.showinfo('Success',"You have logged in Successfully")
        root.destroy()
        library()
    else:
        messagebox.showinfo('Failure',"Please check User Name and Password")

       

root = Tk()
root.title("Login")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25


# Adding a background image

background_image =Image.open("closet.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size


newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)


Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

        

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        
headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

# Enter User Name
lb1 = Label(labelFrame,text="User Name : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.08)

userName = Entry(labelFrame)
userName.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.35, relheight=0.08)

password = Entry(labelFrame)
password.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)


#Submit Button
SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=checkLogin)
SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

root.mainloop()



