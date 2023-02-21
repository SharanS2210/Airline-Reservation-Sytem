import random
import csv
import sys
class booking:
    def menu(self):
        print("\t ------------------------------ \n")
        print("\t ------------------------------ \n")
        print("\t        Online Booking")
        print("\t ------------------------------ \n")
        print("\t ------------------------------ \n")
        print()
        print("Press 1 for booking: ")
        option=int(input())
        self.reservation(option)

    def flightBooking(self,flightname,NoOfPassengers,From,To,Date):
        filename='passenger.csv'
        while NoOfPassengers!=0:
            FirstName=input("First Name - ")
            LastName=input("LastName - ")
            Age=int(input("Age - "))
            NoOfPassengers-=1
            print("Select ur Seat: \n  [1] [2]  [3]  [4]  [5] \n  [6] [7]  [8]  [9]  [10] \n [11] [12] [13] [14] [15] \n [16] [17] [18] [19] [20] \n [21] [22] [23] [24] [25] \n [26] [27] [28] [29] [30] \n [31] [32] [33] [34] [35] \n [36] [37] [38] [39] [40] \n [41] [42] [43] [44] [45] \n [46] [47] [48] [49] [50]")
            SelectedSeat=int(input())
            flightname[SelectedSeat-1]=1
            pnr=random.randint(1111111111,9999999999)
            try:
                with open(filename, 'a', newline="") as f:
                    writer=csv.writer(f, delimiter=",")
                    writer.writerow([FirstName,LastName,From,To,Date,Age,SelectedSeat,pnr])
            except FileNotFoundError:
                print("Sorry, the file "+ filename +"does not exist.")
        print("*********************************************************")
        print("*********************************************************")
        print("               YOUR SEAT IS BOOKED!!!")
        print("*********************************************************")
        print("*********************************************************")
        sys.exit()
    
    def reservation(self,choice):
        PNR=0
        Vistara=[0]*50
        Indigo=[0]*50
        goAir=[0]*50
        Airasia=[0]*50
        AirIndia=[0]*50
        if choice==1:
            From=input("From - ")
            To=input("To - ")
            Date=input("Date - ")
            NoOfPassengers=int(input("Number of passengers - "))
            print("*********************************************************")
            print("                       FLIGHTS")
            print("*********************************************************")
            flights={"Vistara":["5.30am","2.30pm","4.30pm"],"Indigo":["9.00am","12.30pm","1.10pm"],"goAir ":["10.00am","2.35pm"],"Air Asia":["10.45am"],"Air India":["2.15pm"]}
            i=0
                
            for k,v in flights.items():
                for j in v:
                    i+=1
                    print(i,"\t",k,"\t",j)
            print("*********************************************************")
            flight=input("Select ur Flight - ")
            if flight=="Vistara":
                self.flightBooking(Vistara,NoOfPassengers,From,To,Date)
            elif flight=="Indigo":
                self.flightBooking(Indigo,NoOfPassengers,From,To,Date)
            elif flight=="goAir":
                self.flightBooking(goAir,NoOfPassengers,From,To,Date)
            elif flight=="Air Asia":
                self.flightBooking(Airasia,NoOfPassengers,From,To,Date)
            elif flight=="Air India":
                self.flightBooking(AirIndia,NoOfPassengers,From,To,Date)
    
    
