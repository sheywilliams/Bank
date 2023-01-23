# atm 
# i still want to write this atm loop bigger, using php and inserting and selecting from table(new acct)etc 
# class seun:
#     def __init__(self):
#         # self.pin = '3456'
#         self.start()
#     def start(self):
#         x = 0
#         pin = 3456
#         while x <= 3:
#             fx = int(input('Welcome,\n Enter your PIN >>>\n'))
#             if fx == pin: 
#                 fy = int(input('''
#                 Choose option:
#                 1.  Cash Withdrawal 2. Balance Inquiry 3. Transfer 
#                 4. Bill Payment 5. Recent Transactions 6. Contact Us
#                 '''))
#                 if fy == 1: 
#                     self.one()
#                 elif fy == 2:
#                     self.two()
#                 elif fy == 3:
#                     self.thr() 
#                 elif fy == 4:
#                     self.four()
#                 elif fy == 5:
#                     self.five()
#                 elif fy == 6:      
#                     self.six()
#                 else:
#                     print('Wrong input')
#                     quit()
#                 break                                   
#             else:
#                 print('Try again, %d tries left' %(3-x)) 
#                 x += 1     
#         else:
#             print('Your account has been blocked')                  
            
#     def one(self):
#         fz = int(input('1. 1000\n 2. 5000\n 3. 10000\n 4. 20000\n 5. Amounts greater than 20000\n Enter 0 to go back to main menu\n'))
#         if fz == 1 or 2 or 3 or 4 or 5:
#             print('kkk\n Thank you for banking with us')
#         else:
#             self.start()   
#     def two(self):
#         fa = int(input('Your balance is xyz naira\n Enter 1 to Go back to main menu or 0 to Quit\n'))
#         if fa == 1:
#             self.start()
#         else:
#             quit()
#     def thr(self):
#         fb1 = int(input('Enter recipient account number: '))
#         fb2 = input('Enter recipient bank: ')
#         fb3 = int(input('Amount: '))
#         if fb3 > 100000:
#             print('Amount must be less than 100,000')
#             self.thr()
#         else:
#             print('Transaction successful') 
#             qw = int(input('Enter 1 to Go back to main menu and 0 to Quit\n'))
#             if qw == 1:
#                 self.start()
#             else:
#                 quit()     
#     def four(self):
#         fc = int(input('1. PHCN\n 2. Water bill\n 3. DSTV/GOTV\n 4. Cancel\n')) 
#         if fc == 1 or 2 or 3:
#             fc1 = input('Enter Meter number >>>')
#             fc2 = input('Enter Amount >>>') 
#             print('Transaction successful')
#             qw = int(input('Enter 1 to Go back to main menu and 0 to Quit \n'))
#             if qw == 1:
#                 self.start()
#             else:
#                 quit() 
#         else:
#             quit()
#     def five(self):
#         fd = int(input('day 1 : food 3k\n day 2: bills 100k\n NOW SAPA DON CATCH YOU\n enter 1 to Go back to main menu or 0 to Quit'))
#         if fd == 1:
#             self.start()
#         else:
#             quit()    
#     def six(self):
#         fe = int(input('phone no: 080xxxx\n email: xyz@gmail.com\n enter 1 to Go back to main menu or 0 to Quit \n'))
#         if fe == 1:
#             self.start()
#         else:
#             quit()    
# seun()    
