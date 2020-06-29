
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

class GUI:
    def __init__(self, master):
        self.master = master
        master.geometry("1200x800")
        master.title("CARLA_GUI")


        #Home Page Title Text
        font_title = tkFont.Font(size=24)
        self.title_text = Label(master, text="Carla Driving Simulator", font = font_title)
        self.title_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Home Page Version Text
        font_version = tkFont.Font(size=14)
        self.version_text = Label(master, text="Version 0.00", font = font_version)
        self.version_text.place(relx=0.5, rely=0.55, anchor=CENTER)

        #Freeway Button
        font_button = tkFont.Font(size = 18)
        self.freeway_button = Button(master, text="Freeway", command=self.hello, font = font_button)
        self.freeway_button.place(relx=0.40, rely=0.65, anchor=CENTER, width = 180, height = 60)

        #Intersection Button
        self.intersection_button = Button(master, text="Intersection", command=master.quit, font = font_button)
        self.intersection_button.place(relx=0.6, rely=0.65, anchor=CENTER, width = 180, height = 60)

        #Quit Button
        self.quit_button = Button(master, text="Quit", command=master.quit, font=font_button)
        self.quit_button.place(relx=0.5, rely=0.90, anchor=CENTER, width = 100, height = 40)


    def hello(self):
        self.freeway.lift
 
root = Tk()
my_gui = GUI(root)
root.mainloop()

