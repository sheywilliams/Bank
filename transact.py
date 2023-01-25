import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'bank')
mycursor = mydb.cursor()

class trans:
    def __init__(self):
        self.act()
    def act(self):
        q = input("Enter your Bank id >>> ") 
        t = input("Enter your pin >>> ")
        if t :
            myquery = 'SELECT * FROM User WHERE Bank_id=%s AND Bank_pin=%s'
            val = (q, t)
            mycursor.execute(myquery, val)
            myreg = mycursor.fetchone()
            mydb.commit()
            print('Welcome User '+ q)
            fy = int(input('''
            Choose option:
                1.  Cash Withdrawal 2. Balance Inquiry 3. Transfer 
                4. Bill Payment 5. Recent Transactions 
                '''))
            if fy == 1: 
                self.one()
            elif fy == 2:
                self.two()
            elif fy == 3:
                self.thr() 
            elif fy == 4:
                self.four()
            elif fy == 5:
                self.five()
            else:
                print('Wrong input')
                quit()          
        else:
            print('Wrong login details, Try again')  
trans.act(1)
    # def one(self):

