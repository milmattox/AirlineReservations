#Python Airline Reservation Program
#Michelle Mattox - July 10, 2022
'''Program will take in a list of passengers and assign
them into seats based on seating preference designation'''

#source https://pythonguides.com/python-tkinter-listbox/
import tkinter as tk
from tkinter import *

ws = Tk()
ws. title("E=mc2 Airlines")
ws.geometry('800x600')
ws.config(bg='#EEEEEE')
titleLabel = tk.Label(text = "Airline Reservations")
titleLabel.grid(row=0,column=0)
person=''

passengers = ["Ardeen, Blount","Crystal,Ballantyne","Cristina,Slany","Nicole,Pauling","Doy,Liddington","Lincoln,Moultrie","Binny,Lockney","Pris,Clitsome","Redd,Jekyll","Homerus,Braycotton","Judah,Willman","Helenelizabeth,Mallabone","Kirstyn,Kassman","Iolanthe,Melendez","Debbie,Dignon","Rosalyn,Aylott","Georgine,Nealon","Hatti,Durban","Sapphira,Lassells","Wini,Kuhnert","Ken,Benoit","Lindy,Woolard","Sonia,Spinola","Emmie,Ewers","Glenden,Fehner"]
assigned=[]
assignedSeats=[]

def clickSeat(k):
    print(k)
    assigned.append(person)
    passengers.remove(person)
    assignedSeats.append(k)
    print(assigned)
    print(assignedSeats)
    update_noAssignList()
    update_AssignedList()
    print(passengers)

#create gui seat grid
seats = []
rowNum = 1
for r in range(1,21):
    colNum = 4
    for c in range(7):
        name = str(r) + chr(65 + c)
        seats.append(name)
        if c % 2 == 0:
            seatButton = tk.Button(text = name, width=3,bg="lightgreen", command=lambda k=name:clickSeat(k))
        else:
            seatButton = tk.Button(text = name, width=3,bg="red", state = DISABLED)
        seatButton.grid(row = rowNum,column = colNum)
        #seats.append(seatButton)
        colNum = colNum + 1
    rowNum = rowNum + 1
    #print(seats)


#----------unassigned listbox
def showSelected():
    global person
    show.config(text=noAssignedSeatlb.get(ANCHOR))
    person = noAssignedSeatlb.get(ANCHOR)
    print(person)

def update_noAssignList():
    noAssignedSeatlb.delete(0,noAssignedSeatlb.size())
    for i in range(len(passengers)):
        noAssignedSeatlb.insert(i,passengers[i])

noAssignedSeatlb=Listbox(ws)
noAssignedSeatlb.grid(row = 1, column = 1, rowspan = 8)
for i in range(len(passengers)):
    noAssignedSeatlb.insert(i,passengers[i])

Button(ws, text = 'Select Passenger', command=showSelected).grid(row=9,column=0)
show = Label(ws)
show.grid(row = 9, column = 1)
#------------unassigned listbox end
def showSelectedAs():
    global person
    person = AssignedSeatlb.get(ANCHOR)
    #showAs.config(text=AssignedSeatlb.get(ANCHOR))
    
    showAs.config(text=assignedSeats[assigned.index(person)])

def update_AssignedList():
    AssignedSeatlb.delete(0,AssignedSeatlb.size())
    for i in range(len(assigned)):
        AssignedSeatlb.insert(i, assigned[i])

AssignedSeatlb=Listbox(ws)
AssignedSeatlb.grid(row = 1, column = 12, rowspan = 8)
for i in range(len(assigned)):
    AssignedSeatlb.insert(i, assigned[i])

Button(ws, text = 'Show Seat Assignment', command=showSelectedAs).grid(row=9,column=12)
showAs = Label(ws)
showAs.grid(row = 9, column = 13)

ws.mainloop()
