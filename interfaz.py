from tkinter import *
import datarev
import serial
import csv
import  threading
from plots import  grafpos
from datarev import datataker
from datarev import  vec
def btn_clicked():
   for i in range(5):
       print("Monda")



window = Tk()

window.geometry("800x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    202.0, 303.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 461, y = 468,
    width = 282,
    height = 88)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : vec('pos.txt'),
    relief = "flat")

b1.place(
    x = 461, y = 325,
    width = 282,
    height = 88)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command =datataker,
    relief = "flat")

b2.place(
    x = 461, y = 39,
    width = 282,
    height = 88)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : grafpos('pos.txt'),
    relief = "flat")

b3.place(
    x = 461, y = 182,
    width = 282,
    height = 88)

window.resizable(False, False)
window.title("Proyecto Geo-expofisica")
window.mainloop()
