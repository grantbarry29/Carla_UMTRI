import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
import os
    
class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        

    

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #container frame inside page
        width = self.winfo_screenwidth()
        height =  self.winfo_screenheight()
        container = tk.Frame(self, width = width, height = height)
        container.grid_propagate(False)
        container.pack()        
        
        #page text and buttons
        tk.Label(container, text="Carla Driving Simulator", font=('Helvetica', 24, "bold")).place(relx = .5, rely = .45, anchor=CENTER)
        tk.Label(container, text="Version 0.00").place(relx = 0.5, rely = 0.49, anchor = CENTER)
        tk.Button(container, text="Freeway",
                  command=lambda: master.switch_frame(PageOne)).place(relx = .40, rely = .6, anchor = CENTER, width = 180, height = 60)
        tk.Button(container, text="Intersection",
                  command=lambda: master.switch_frame(PageTwo)).place(relx = .60, rely = .6, anchor = CENTER, width = 180, height = 60)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #container frame inside page
        width = self.winfo_screenwidth()
        height =  self.winfo_screenheight()
        container = tk.Frame(self, width = width, height = height)
        container.grid_propagate(False)
        container.pack()
        container['bg'] = 'white'

        #back button
        tk.Button(container, text="Back",
                  command=lambda: master.switch_frame(StartPage)).place(relx = 0.003, rely = 0.003, width = 60, height = 25)

        #####general settings#####
        tk.Label(container, text="General Settings", font=('Helvetica', 20)).place(relx = 0.1, rely = 0.1)

        #num intersections
        tk.Label(container, text="Number of Freeway Sections", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.2)
        num_intersections = tk.Entry(container)
        num_intersections.place(relx = 0.23, rely = 0.19, height = 40, width = 40)
        
        #min velocity
        tk.Label(container, text="Min Velocity (km/h)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.27)
        min_velocity = tk.Entry(container)
        min_velocity.place(relx = 0.23, rely = 0.26, height = 40, width = 40)

        #max velocity
        tk.Label(container, text="Max Velocity (km/h)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.35)
        max_velocity = tk.Entry(container)
        max_velocity.place(relx = 0.23, rely = 0.33, height = 40, width = 40)

        #section distance
        tk.Label(container, text="Section Distance (km)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.42)
        section_distance = tk.Entry(container)
        section_distance.place(relx = 0.23, rely = 0.40, height = 40, width = 40)

        #safety distance
        tk.Label(container, text="Safety Distance (m)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.49)
        safety_distance = tk.Entry(container)
        safety_distance.place(relx = 0.23, rely = 0.47, height = 40, width = 40)

        #toggle collisions
        tk.Label(container, text="Toggle Collisions", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.56)
        toggle_collisions = tk.Checkbutton(container, height = 40, width = 40)
        toggle_collisions.place(relx = 0.23, rely = 0.54, height = 40, width = 40)

        #edit sections
        tk.Button(container, text = "Edit Sections", font=('Helvetica', 16)).place(relx = 0.053, rely = 0.60)


        ######sections images#####
        road1 = PhotoImage(file = "/Users/gbarry/desktop/UMTRI/tk/road.gif")
        road1 = road1.subsample(2,2)
        map1 = Label(container, image=road1)
        map1.image = road1
        map1.place(relx = 0.5, rely = 0.3)
        map2 = Label(container, image=road1)
        map2.image = road1
        map2.place(relx = 0.56, rely = 0.3)
        map3 = Label(container, image=road1)
        map3.image = road1
        map3.place(relx = 0.62, rely = 0.3)
        map4 = Label(container, image=road1)
        map4.image = road1
        map4.place(relx = 0.68, rely = 0.3)
        map5 = Label(container, image=road1)
        map5.image = road1
        map5.place(relx = 0.74, rely = 0.3)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #container frame inside page
        width = self.winfo_screenwidth()
        height =  self.winfo_screenheight()
        container = tk.Frame(self, width = width, height = height)
        container.grid_propagate(False)
        container.pack()
        container['bg'] = 'white'

        #back button
        tk.Button(container, text="Back",
                  command=lambda: master.switch_frame(StartPage)).place(relx = 0.003, rely = 0.003, width = 60, height = 25)

        #####general settings#####
        tk.Label(container, text="General Settings", font=('Helvetica', 20)).place(relx = 0.1, rely = 0.1)

        #num intersections
        tk.Label(container, text="Number of Intersections", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.2)
        num_intersections = tk.Entry(container)
        num_intersections.place(relx = 0.23, rely = 0.19, height = 40, width = 40)
        
        #min velocity
        tk.Label(container, text="Min Velocity (km/h)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.27)
        min_velocity = tk.Entry(container)
        min_velocity.place(relx = 0.23, rely = 0.26, height = 40, width = 40)

        #max velocity
        tk.Label(container, text="Max Velocity (km/h)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.35)
        max_velocity = tk.Entry(container)
        max_velocity.place(relx = 0.23, rely = 0.33, height = 40, width = 40)



        #safety distance
        tk.Label(container, text="Safety Distance (m)", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.42)
        safety_distance = tk.Entry(container)
        safety_distance.place(relx = 0.23, rely = 0.40, height = 40, width = 40)

        #toggle collisions
        tk.Label(container, text="Toggle Collisions", font=('Helvetica', 16)).place(relx = 0.05, rely = 0.49)
        toggle_collisions = tk.Checkbutton(container, height = 40, width = 40)
        toggle_collisions.place(relx = 0.23, rely = 0.47, height = 40, width = 40)

        #edit sections
        tk.Button(container, text = "Edit Sections", font=('Helvetica', 16)).place(relx = 0.053, rely = 0.54)


        ######sections images#####
        road1 = PhotoImage(file = "/Users/gbarry/desktop/UMTRI/tk/road.gif")
        road1 = road1.subsample(2,2)
        map1 = Label(container, image=road1)
        map1.image = road1
        map1.place(relx = 0.5, rely = 0.3)
        map2 = Label(container, image=road1)
        map2.image = road1
        map2.place(relx = 0.56, rely = 0.3)
        map3 = Label(container, image=road1)
        map3.image = road1
        map3.place(relx = 0.62, rely = 0.3)
        map4 = Label(container, image=road1)
        map4.image = road1
        map4.place(relx = 0.68, rely = 0.3)
        map5 = Label(container, image=road1)
        map5.image = road1
        map5.place(relx = 0.74, rely = 0.3)
if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()