# Title: Airline Reservation SystemError
# Author: Sharan S
# Created on: 07.02.2023
# Last Modified Data: 19.02.2023
# Reviewed by - Silpa
# Reviewed on -

from login_Signup import Login_SignUp
filename='login.csv'


print("*********************************************************")
print("HELLO!! Welcome to Airline Reservation System")
print("*********************************************************")
acc=input("DO YOU HAVE AN ACCOUNT?")

if acc=="yes":
    l=Login_SignUp()
    l.Login()
else:
    s=Login_SignUp()
    s.SignUp()
        

            
        

        

        




