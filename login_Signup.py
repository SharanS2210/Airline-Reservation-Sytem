import maskpass
import csv
import re
from Booking import booking

class Login_SignUp:
    def SignUp(self):
        while True:
            print("*********************************************************")
            print("SIGN UP")
            print("*********************************************************")
            filename='login.csv'
            NewEmail=input("Enter New Username - ")
            NewPassword=maskpass.askpass(prompt="New Password - ", mask="*")
            ConfirmPassword=maskpass.askpass(prompt="Confirm Password - ", mask="*")
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            pwd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            if re.match(pat,NewEmail) and re.match(pwd,NewPassword) and NewPassword==ConfirmPassword:
                print("Thank You for Signing In")
                try:
                    with open(filename, 'a', newline="") as f:
                        writer = csv.writer(f,delimiter=",")
                        writer.writerow([NewEmail, NewPassword])
                except FileNotFoundError:
                    print("Sorry, the file "+ filename +"does not exist.")
                if self.Login():    
                    m=booking()
                    m.menu()
                #return True
            else:
                print("Invalid Entry!! Please try again")

    def Login(self):
        print("*********************************************************")
        print("                       LOG IN")
        print("*********************************************************")
        while True:
            print("Email - ")
            email=input()
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(pat,email):
                password=maskpass.askpass(prompt="Password:", mask="*")
                pwd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
                try:
                    with open("login.csv","r") as f:
                        reader = csv.reader(f,delimiter=",")
                        for row in reader:
                            if re.match(pwd,password) and row == [email, password]:
                                print("Email and Password are valid")
                                m=booking()
                                m.menu()
                                # return True
                except FileNotFoundError:
                    print("Sorry, the file login.csv does not exist.")
            else:
                print("*********************************************************")
                print("               Wrong Username or Password")
                print("*********************************************************")
