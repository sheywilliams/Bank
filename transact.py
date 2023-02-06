import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'bank')
mycursor = mydb.cursor()
from home import page


class trans:
    def __init__(self):
        self.act()
        
    def act(self): 
        Bankid = input("Enter your Bank id >>> ") 
        Bankpin = input("Enter your pin >>> ") 
        if Bankpin:
            myquery = 'SELECT * FROM User WHERE Bank_id=%s AND Bank_pin=%s'
            val = (Bankid, Bankpin)
            mycursor.execute(myquery, val)
            myreg = mycursor.fetchone()
            mydb.commit()
            print('Welcome User '+ Bankid)
            fy = int(input('''
            Choose option:
                1. Deposit 2. Cash Withdrawal 3. Transfer 
                4. Balance Inquiry 5. Recent Transactions 6. Go to main menu  
                '''))
            if fy == 1: 
                trans.one(0)
                # dep = int(input('How much will you like to deposit into your account? >>>'))
                # # sql = 'SELECT @id := id FROM customers WHERE id="Bank_id" '
                # # mycursor.execute(sql)
                # myquery = "INSERT INTO User(Deposits) VALUES (%s) WHERE Bank_id= 180092  AND Bank_pin= 1234 "
                # val1 = (dep)
                # mycursor.execute(myquery, [val1,])
                # # mycursor.executemany(myquery, vals)
                # mydb.commit()
                # print('Deposit made successfully') 
                # qw = input('Enter 1 to go back to main menu or 2 to quit')
                # if qw == '1':
                #     self.act()
                # else:
                #     quit()  
            elif fy == 2:
                trans.two(0)
            elif fy == 3:
                self.thr() 
            elif fy == 4:
                self.four()
            elif fy == 5:
                self.five()
            elif fy == 6:
                page.start()    
            else:
                print('Wrong input')
                quit()          
        else: 
            print('Wrong login details, Try again')
            
    def one(self):
        # dep = int(input('How much will you like to deposit into your account? >>>'))
        dep = 1000
        myquery = "UPDATE User SET User.Deposits=%s WHERE User.Bank_Id= %s"
        val1 = (dep)
        mycursor.execute(myquery, [val1,])
        # mycursor.execute(myquery, {'dep':dep})
        mydb.commit()
        print('Deposit made successfully') 
        qw = input('Enter 1 to go back to main menu or 2 to quit')
        if qw == '1':
            trans.act()
        else:
            quit()    

#     def two(self):
#         withd = int(input('How much will you like to withdraw?'))
#         myquery1 = 'INSERT INTO User (Withdrawals) VALUES (%s)'
#         val1 = (withd)
#         mycursor.execute(myquery1, (val1,))
#         mydb.commit()
#         print('Take your cash...')

#         myquery2 = 'INSERT INTO User (Balance) VALUES (%s) WHERE (Deposits = %s - Withdrawals = %s)'
#         mycursor.execute(myquery2)
#         mydb.commit()
trans.act(0)