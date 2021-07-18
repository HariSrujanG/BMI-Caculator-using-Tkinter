from tkinter import*
import math

def calculate():
    a = h.get()
    ht = float(a)
    b = w.get()
    wt = float(b)
    bmi = wt/pow(ht,2)
    r.set(math.floor(bmi*10000))

bmi = Tk()
bmi.title('BMI calculator')
bmi.geometry('400x300')
bmi.configure(bg='sky blue')

h = StringVar()
w = StringVar()
r = StringVar()

#header
lbl = Label(bmi, text="BMI Calculator",font=("Timesnew roman",16), bg="sky blue")
lbl.grid(row=1, column=1, pady=10, padx=10)

#Hieght
lbl = Label(bmi, text="Enter your hieght in meters", font=("Timesnew roman", 12), bg="sky blue")
lbl.grid(row=3, column=1, pady=10, padx=10)
txt = Entry(bmi, textvariable=h, width=10,font=("Unispace", 12) ) 
txt.grid(row=3, column=2)

#weight
lbl = Label(bmi, text="Enter your weight in Kgs", font=("Timesnew roman", 12), bg="sky blue" )
lbl.grid(row=4, column=1, pady=10, padx=10)
txt = Entry(bmi, textvariable=w, width=10,font=("Unispace", 12) ) 
txt.grid(row=4, column=2)

#Calc Button
btn = Button(bmi, text="Check BMI", bg= 'gray', fg= 'sky blue', command=calculate) 
btn.grid(row=6, column=1) 

#Result
lbl = Label(bmi, text="Your BMI is", font=("Timesnew roman", 12), bg="sky blue")
lbl.grid(row=8, column=1, pady=10, padx=10)
txt = Entry(bmi, textvariable=r,width=10,font=("Unispace", 12) ) 
txt.grid(row=8, column=2)

bmi.mainloop()
