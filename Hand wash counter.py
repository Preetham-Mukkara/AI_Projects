
import tkinter as tk
import random
from PIL import ImageTk,Image


dataset = ["Diseases can make anyone sick regardless of their race or ethnicity.","the immediate risk of becoming seriously ill from COVID-19 is thought to be low.",
           "Someone who has completed quarantine does not pose a risk of infection to other people."
           , "Wash your hands often with soap and water for at least 20 seconds","in public, wear a cloth face covering that covers your mouth and nose." ,"Avoid touching your eyes, nose, and mouth with unwashed hands."
           ,"Stay home when you are sick.","Cover your cough/sneeze with a tissue and throw the tissue in the trash."]
window = tk.Tk()

window.title("COVID-19 Safety Measures")


window.geometry('1000x250')

my_img = ImageTk.PhotoImage(Image.open("C.jpg"))
background_label = tk.Label(window, image = my_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.LabelFrame(window, text = "Hand-Washing Helps!",padx = 10,pady = 10)

frame.pack(padx = 25,pady = 12.5)

frame.configure(background = "orange")

lbl = tk.Label(frame, text="Hello, hope you're doing well!")

lbl.grid(column=0, row=0)

lbl.configure(background = "yellow")

label4 = tk.Label(frame, text="Wash hands for 20 seconds to be safe!")

label4.grid(column=1, row=1)
label4.configure(background = "yellow")
counter = 0
label = tk.Label(frame)
factLabel = tk.Label(frame)
lbl3 = tk.Label(frame) 

def count():
            global counter
            global label 
            if counter < 20:
                label = tk.Label(frame)
                label.config(text = "Time left washing hands:" + str(20 - counter))
                label.configure(background = "red")
                label.grid(column = 0, row = 1)
                label.after(1000,count)
                counter = counter + 1                
def popup():
    global factLabel
    global counter
    global lbl3
    lbl3.destroy()
    global label
    label.destroy()
    factLabel.destroy()
    counter = 0
    response = tk.messagebox.askquestion(title = "Hello :)", message = "Did you wash your hands after coming back?")
    if response == 'no':
        factLabel = tk.Label(frame)
        factLabel.config(text = str(random.choice(dataset)))
        factLabel.grid(column = 0, row = 2)
        factLabel.configure(background = "red")
        count()
    if response == 'yes':
            label.destroy()
            lbl3 = tk.Label(frame, text="Good job!")
            lbl3.configure(background = "green")
            lbl3.grid(column=0, row=1)

    
btn2 = tk.Button(frame, text = "Have you washed your hands? " ,fg = 'red',command = popup)
btn2.grid(column = 1, row = 0)   

def lol():
    window.destroy()
buttonEnd = tk.Button(window,text = "close application", command = lol)
buttonEnd.pack()
window.mainloop()