import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'bank')
mycursor = mydb.cursor()
# from transact import trans
# mycursor.execute("CREATE DATABASE bank")
# mycursor.execute("SHOW DATABASES")
# for database in mycursor:
#     print(database)
import numpy as np
# mycursor.execute('CREATE TABLE User (Full_name VARCHAR(50), Gender VARCHAR(1), Phone_No VARCHAR(11), Bank_Id INT(6), Bank_pin INT(10), Deposits INT(30), Withdrawals INT(30), Balance INT(30))')
# sql = 'DROP TABLE User'
# mycursor.execute(sql)


class page:
    def __init__(self):
        self.start()
    def start(self):
        print('Welcome to Star Bank Online Services')
        q = int(input('Click on preferred option\n 1. Open bank account\n 2. Online Transactions\n 3. Contact Customer Services >>>'))
        if q == 1:
            x = input("Enter full name >>>")
            y = input("Enter Gender(M/F) >>>")
            z = input("Enter phone number >>>")
            print("Your Bank id is ...")
            t = np.random.randint(100000, 200000)
            print(t)
            p = int(input('Enter your desired four-digit pin >>>'))
            myquery ='INSERT INTO User(Full_name, Gender, Phone_No, Bank_id, Bank_pin ) VALUES (%s, %s, %s, %s, %s)'
            val = (x, y, z, t, p)
            mycursor.execute(myquery, val)
            mydb.commit()
            print('Account added successfully') 
page.start(0)

