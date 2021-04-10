import tkinter as tk
from tkinter import *
import HillClimb_GestureRecog

window = Tk()
# creating the Box
window.title("Gesture Control App")
# Adjust size  

window.geometry("1540x850")



# Add image file 

bg = PhotoImage( file = "features-2.png") 
# Show image using label 

label1 = Label( window, image = bg) 

label1.place(x = 0,y = 0) 

link1 = Label(window, text="Start Hill Climb Racing", fg="blue",bg="white", cursor="hand2",font="Arial")
link1.pack()
link1.bind("<Button-1>", lambda e: HillClimb_GestureRecog.oncamerafeed(window) )
link1.config(width=20)

link1.place(relx = 0.73, rely = 0.5, anchor = 'center')


window.resizable(0,0)
window.mainloop()
window.update()