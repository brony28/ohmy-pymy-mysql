# ohmy-pymy-mysql #
An easy-to-make Tkinter - MySQL interactive project edited and debugged for my friend...\
Simple version of ODBC in Python.

#### Small Guide.. ####

First, keep all program files and image in one folder.

Create a Database of name **mydatabase** using MySQL.\
Then create 3 tables in this database
1. login
2. dressTable
3. soldTable


The query for creating **login** Table:\
`CREATE TABLE login(userName varchar(20), password varchar(50));`

Now store a username and password to access the GUI.\
`INSERT INTO login VALUE('hello','world');`\
(you can give any values for this)


Once this is done create 2nd table, i.e. **dressTable** :\
`CREATE TABLE dressTable(DRESS_CODE int, TYPE varchar(30),CATEGORY varchar(30),SIZE varchar(25),PRICE int);`


Now Create 3rd Table, **soldTable** :\
`CREATE TABLE soldTable(ID int, Sold_To varchar(30));`
<br/>
The Database Configuration is done.


Now goto python files and replace the <password> in `pymysql.connect(host="localhost",user="root",password=' <password> ',database='mydatabase')` with your password
DO this in every python files.


Now you are good to go. Simple run the ___main.py___ file and explore.

