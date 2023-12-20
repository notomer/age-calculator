#Omer Code Prod
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time

# window Geometry
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#18171B")
window.resizable(width=False,height=False)
window.title('Age Calculator')

window.eval("tk::PlaceWindow . center")

#label
age_calc = Label(window, text = "Age Calculator!", font= ("helvetica", 24),)
age_calc.pack(pady=10)

enter_age = Label(window, text = "Enter Age", font= ("helvetica", 24),)
enter_age.pack(pady=20)

age_entry = Entry(window, font=("arial", 20))
age_entry.pack(pady=20) 


#Algorithim
def age():
    if age_entry.get():
        #"calculating"
        time.sleep(10)
        messagebox.showinfo(window, f"Your age is {int(age_entry.get())}!", )
    else: 
        messagebox.showwarning("Input Numerical Value",("You didn't input a value!"))


#Buttons

age_button = Button(window, text = "Calculate Age", font=("arial", 20), command=age)
age_button.pack(pady=20)

window.mainloop()