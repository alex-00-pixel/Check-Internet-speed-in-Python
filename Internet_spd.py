#import math -> math module is imported
#from math import*-> a method from math imported as a variable
from tkinter import *

import speedtest
def speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    dwn = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.download()/(10**6),3))+"Mbps"
    lab_down.config(text=dwn)
    lab_up.config(text=up)
    
#calling tkinter class by a variable sp
sp = Tk()

sp.title("Internet Speed Test")
sp.geometry("500x400")
sp.config(bg = "green")

lab = Label(sp, text="Internet Speed Test", font =("Time New Roman", 30, "bold"), bg = "pink")
lab.place(x =465, y = 20)

lab = Label(sp, text="Download Speed", font =("Time New Roman", 15, "bold"))
lab.place(x =165, y = 420)

lab_down = Label(sp, text="00", font =("Time New Roman", 15, "bold"), bg = "light blue")
lab_down.place(x =200, y = 370)

lab = Label(sp, text="Upload Speed", font =("Time New Roman", 15, "bold"))
lab.place(x =885, y = 420)

lab_up = Label(sp, text="00", font =("Time New Roman", 15, "bold"), bg = "light blue")
lab_up.place(x =900, y = 370)

button = Button(sp, text ="CHECK", font=("Time New Roman",12,"bold"), bg="red",relief=RAISED, command=speed)
button.place(x = 555, y = 500)

# To show new wndow

sp.mainloop()