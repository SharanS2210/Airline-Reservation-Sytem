import re
import random
import maskpass
import csv
import sys
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
        

            
        

        

        




