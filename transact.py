import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'bank')
mycursor = mydb.cursor()

class trans:
    def __init__(self):
        self.act()
    def act(self):
        x = 0
        while x >= 3:
            q = input("Enter your Bank id >>> ")
            t = input("Enter your pin >>> ")
            if q and t:
                myquery = 'SELECT * FROM Bank WHERE Bank_id=%s AND Bank_pin=%s'
                val = (q, t)
                mycursor.execute(myquery, val)
                myreg = mycursor.fetchone()
                mydb.commit()
                print('Welcome User'+ q)
                fy = int(input('''
                Choose option:
                 1.  Cash Withdrawal 2. Balance Inquiry 3. Transfer 
                 4. Bill Payment 5. Recent Transactions 6. Contact Us
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
                elif fy == 6:      
                    self.six()
                else:
                    print('Wrong input')
                    quit()
                break           
            else:
                print('Wrong input. Try again, %d tries left' %(3-x)) 
                x += 1    
        else:
            print('Your account has been blocked, contact our customer service center for help')  



trans.act(1)
    # def one(self):

