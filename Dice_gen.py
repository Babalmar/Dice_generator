import random
from tkinter import * 

#main settings
window = Tk()
window.geometry("480x480")
window.wm_title("Dice generator")
window.iconbitmap("Iconsmind-Outline-Dice.ico")


frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()

label = Label(frame1, text='')
#frame1.grid_propagate(0)
label_poly = Label(frame2, text="Polyhedrals dices")
#label_poly.pack()
label_non_poly = Label(frame3, text="Non-polyhedrals dices")
#label_non_poly.pack()


#dice mechanics
def dice4():
    d4 = random.randint(1,4)
    label.configure(text="Dice throw (d4): " + str(d4))

def dice6():
    d6 = random.randint(1,6)
    label.configure(text="Dice throw (d6): " + str(d6))
    
def dice8():
    d8 = random.randint(1,8)
    label.configure(text="Dice throw (d8): " + str(d8))

def dice10():
    d10 = random.randint(1,10)
    label.configure(text="Dice throw (d10): " + str(d10))

def dice12():
    d12 = random.randint(1,12)
    label.configure(text="Dice throw (d12): " + str(d12))

def dice20():
    d20 = random.randint(1,20)
    label.configure(text="Dice throw (d20): " + str(d20))
    
def dice100():
    d100 = random.randint(1,100)
    label.configure(text="Dice throw (d100): " + str(d100))

def dice3():
    d3 = random.randint(1,3)
    label.configure(text="Dice throw (d3): " + str(d3))
    
def dice5():
    d5 = random.randint(1,85)
    label.configure(text="Dice throw (d5): " + str(d5))

def dice7():
    d7 = random.randint(1,7)
    label.configure(text="Dice throw (d7): " + str(d7))

def dice14():
    d14 = random.randint(1,14)
    label.configure(text="Dice throw (d14): " + str(d14))

def dice16():
    d16 = random.randint(1,16)
    label.configure(text="Dice throw (d16): " + str(d16))

def dice24():
    d24 = random.randint(1,24)
    label.configure(text="Dice throw (d24): " + str(d24))

def dice30():
    d30 = random.randint(1,30)
    label.configure(text="Dice throw (d30): " + str(d30))
   
d4_button = Button(frame2, text='D4', command=dice4)
d6_button = Button(frame2, text='D6', command=dice6)
d8_button = Button(frame2, text='D8', command=dice8)
d10_button = Button(frame2, text='D10', command=dice10)
d12_button = Button(frame2, text='D12', command=dice12)
d20_button = Button(frame2, text='D20', command=dice20)
d100_button = Button(frame2, text='D100', command=dice100)

d3_button = Button(frame3, text='D3', command=dice3)
d5_button = Button(frame3, text='D5', command=dice5)
d7_button = Button(frame3, text='D7', command=dice7)
d14_button = Button(frame3, text='D14', command=dice14)
d16_button = Button(frame3, text='D16', command=dice16)
d24_button = Button(frame3, text='D24', command=dice24)
d30_button = Button(frame3, text='D30', command=dice30)

'''
label.pack()
d4_button.pack(padx = 3, pady = 3)
d6_button.pack(padx = 3, pady = 3)
d8_button.pack(padx = 3, pady = 3)
d10_button.pack(padx = 3, pady = 3)
d12_button.pack(padx = 3, pady = 3)
d20_button.pack(padx = 3, pady = 3)
d100_button.pack(padx = 3, pady = 3)

d3_button.pack(padx = 3, pady = 3)
d5_button.pack(padx = 3, pady = 3)
d7_button.pack(padx = 3, pady = 3)
d14_button.pack(padx = 3, pady = 3)
d16_button.pack(padx = 3, pady = 3)
d24_button.pack(padx = 3, pady = 3)
d30_button.pack(padx = 3, pady = 3)
'''

label = Label(frame1, text='')
label_poly = Label(frame2, text="Polyhedrals dices")
label_non_poly = Label(frame3, text="Non-polyhedrals dices")

label.grid(row=0, column=2, columnspan=3)
label_poly.grid(row=2, column=3, columnspan=3)
label_non_poly.grid(row=5, column=3, columnspan=3)

d4_button.grid(row=3, column=1)
d6_button.grid(row=3, column=2)
d8_button.grid(row=3, column=3)
d10_button.grid(row=3, column=4)
d12_button.grid(row=3, column=5)
d20_button.grid(row=3, column=6)
d100_button.grid(row=3, column=7)

d3_button.grid(row=6, column=1)
d5_button.grid(row=6, column=2)
d7_button.grid(row=6, column=3)
d14_button.grid(row=6, column=4)
d16_button.grid(row=6, column=5)
d24_button.grid(row=6, column=6)
d30_button.grid(row=6, column=7)


window.mainloop()
