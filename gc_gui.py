import tkinter as tk
from tkinter import *
import webbrowser

window = Tk()
# creating the Box
window.title("Gesture Control App")
# Adjust size  

window.geometry("980x680")


# Add image file 

bg = PhotoImage( file = "features-1.png") 
# Show image using label 

label1 = Label( window, image = bg) 

label1.place(x = 0,y = 0) 


def callback(url):
    webbrowser.open_new(url)


link1 = Label(window, text="Click Here to Begin!", fg="blue",bg="white", cursor="hand2",font="Arial")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
link1.config(width=20)

link1.place(relx = 0.73,
                   rely = 0.5,
                   anchor = 'center')



window.mainloop()
