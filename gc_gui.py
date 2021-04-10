import tkinter as tk
from tkinter import *
import webbrowser

window = Tk()
# creating the Box
window.title("Gesture Control App")
# Adjust size  

window.geometry("980x680")
window.configure(bg='white')

# Add image file 

bg = PhotoImage( file = "features-1.png") 
# Show image using label 

label1 = Label( window, image = bg) 

label1.place(x = 350,y = 250) 


def callback(url):
    webbrowser.open_new(url)


link1 = Label(window, text="Google Hyperlink", fg="blue",bg="white", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(window, text="Ecosia Hyperlink", fg="Black",bg="white", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

label2 = Label( window, text = "Welcome to GesCon!",bg="white", font=("Arial", 25)).pack()
label2.pack(pady = 50)

label3 = Label( window, text = "We are a platform that provide Gesture Controlled Actions for your Faviourite Games!",bg="white", font=("Arial", 20)).pack()
label3.pack(pady = 50)



window.mainloop()
