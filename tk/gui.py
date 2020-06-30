import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
    
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
        self._frame.pack()


    
        

    

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #container frame inside page
        width = self.winfo_screenwidth()
        height =  self.winfo_screenheight()
        container = tk.Frame(self, width = width, height = height)
        container.pack()        
        
        #page text and buttons
        tk.Label(container, text="Carla Driving Simulator", font=('Helvetica', 24, "bold")).place(relx = .5, rely = .45, anchor=CENTER)
        tk.Label(container, text="Version 0.00").place(relx = 0.5, rely = 0.49, anchor = CENTER)
        tk.Button(container, text="Freeway",
                  command=lambda: master.switch_frame(PageOne)).place(relx = .40, rely = .6, anchor = CENTER, width = 180, height = 60)
        tk.Button(container, text="Intersection",
                  command=lambda: master.switch_frame(PageTwo)).place(relx = .60, rely = .6, anchor = CENTER, width = 180, height = 60)



#freeway page
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #container frame inside page
        width = self.winfo_screenwidth()
        height =  self.winfo_screenheight()
        container = tk.Frame(self, width = width, height = height)
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
        tk.Button(container, text = "Edit Sections", font=('Helvetica', 16), 
                                                    command=lambda: swap_frames(container, edit_container)).place(relx = 0.053, rely = 0.60)


        ######sections##### 

        #road images
        tk.Label(container, bg="grey77").place(relx = 0.34, rely = 0.07, relwidth = 0.64, relheight = 0.86)
        road1 = PhotoImage(file = "road.gif")
        road1 = road1.subsample(1,1)
        map1 = Label(container, image=road1)
        map1.image = road1
        map1.place(relx = 0.36, rely = 0.1)
        map2 = Label(container, image=road1)
        map2.image = road1
        map2.place(relx = 0.48, rely = 0.1)
        map3 = Label(container, image=road1)
        map3.image = road1
        map3.place(relx = 0.60, rely = 0.1)
        map4 = Label(container, image=road1)
        map4.image = road1
        map4.place(relx = 0.72, rely = 0.1)
        map5 = Label(container, image=road1)
        map5.image = road1
        map5.place(relx = 0.84, rely = 0.1)
        ego = tk.Text(container, highlightthickness=2, font=('Helvetica', 8))
        ego.place(relx = 0.452, rely = 0.55, relheight = 0.045, relwidth = 0.016)
        ego.config(highlightbackground = "red", highlightcolor= "red", bg="red")
        ego.insert('1.0','ego')
        

        #square label buttons on top of roads
        button_text = [1,2,3,4,5]
        Button(container,text = button_text[0], fg="red", bg="red",command=lambda: swap_frames(container, edit_container)
                                        ).place(relx = 0.405, rely = 0.44, relwidth = 0.03, relheight = 0.03)
        Button(container,text = button_text[1], fg="red", bg="red").place(relx = 0.525, rely = 0.44, relwidth = 0.03, relheight = 0.03)
        Button(container,text = button_text[2], fg="red", bg="red").place(relx = 0.645, rely = 0.44, relwidth = 0.03, relheight = 0.03)
        Button(container,text = button_text[3], fg="red", bg="red").place(relx = 0.765, rely = 0.44, relwidth = 0.03, relheight = 0.03)
        Button(container,text = button_text[4], fg="red", bg="red").place(relx = 0.885, rely = 0.44, relwidth = 0.03, relheight = 0.03)



        #####Edit Sections Container#####
        edit_container = tk.Frame(self, width = width, height = height, bg="white")
        edit_container.pack()

        #back button
        tk.Button(edit_container, text="Back",
                  command=lambda: swap_frames(edit_container,container)).place(relx = 0.003, rely = 0.003, width = 60, height = 25)
        
        #road picture
        tk.Canvas(edit_container, bg="grey77").place(relx = 0.48, rely = 0.07, relwidth = 0.16, relheight = 0.85)
        road1 = PhotoImage(file = "road.gif")
        map1 = Label(edit_container, image=road1)
        map1.image = road1
        map1.place(relx = 0.50, rely = 0.1)
        ego = tk.Text(edit_container, highlightthickness=2, font=('Helvetica', 8))
        ego.place(relx = 0.592, rely = 0.55, relheight = 0.045, relwidth = 0.016)
        ego.config(highlightbackground = "red", highlightcolor= "red", bg="red")
        ego.insert('1.0','ego')

        #Intersection Options and Buttons
        tk.Label(edit_container, text="Intersection ID", font=('Helvetica', 20)).place(relx = 0.1, rely = 0.1)
        tk.Button(edit_container, text="Intersection 1", font=('Helvetica', 20)).place(relx = 0.2, rely = 0.1)
        tk.Button(edit_container, text="Spawn Actors", font=('Helvetica', 20),
                                command=lambda : swap_frames(edit_container,spawn_container)).place(relx = 0.1, rely = 0.3)



        #####Spawn Sections Container#####
        spawn_container = tk.Frame(self, width = width, height = height, bg="white")
        spawn_container.pack()
        tk.Label(spawn_container, text="Spawn", font=('Helvetica', 20)).place(relx = 0.13, rely = 0.03)
        tk.Button(spawn_container, text="Spawn", font=('Helvetica', 20)).place(relx = 0.03, rely = 0.9)

        #back button
        tk.Button(spawn_container, text="Back",
                  command=lambda: swap_frames(spawn_container,edit_container)).place(relx = 0.003, rely = 0.003, width = 60, height = 25)
        
        #road picture
        tk.Canvas(spawn_container, bg="grey77").place(relx = 0.48, rely = 0.07, relwidth = 0.16, relheight = 0.85)
        road1 = PhotoImage(file = "road.gif")
        map1 = Label(spawn_container, image=road1)
        map1.image = road1
        map1.place(relx = 0.50, rely = 0.1)
        ego = tk.Text(spawn_container, highlightthickness=2, font=('Helvetica', 8))
        ego.place(relx = 0.592, rely = 0.55, relheight = 0.045, relwidth = 0.016)
        ego.config(highlightbackground = "red", highlightcolor= "red", bg="red")
        ego.insert('1.0','ego')

        #position
        tk.Label(spawn_container, text="Position", font=('Helvetica', 20)).place(relx = 0.025, rely = 0.1)
            #x
        tk.Label(spawn_container, text="x:",font=('Helvetica', 15)).place(relx = 0.033, rely = 0.155)
        x_position = tk.Entry(spawn_container)
        x_position.place(relx = 0.05, rely = 0.15, relwidth = 0.04, relheight = 0.05)
            #y
        tk.Label(spawn_container, text="y:",font=('Helvetica', 15)).place(relx = 0.103, rely = 0.155)
        y_position = tk.Entry(spawn_container)
        y_position.place(relx = 0.12, rely = 0.15, relwidth = 0.04, relheight = 0.05)
            #z
        tk.Label(spawn_container, text="z:",font=('Helvetica', 15)).place(relx = 0.173, rely = 0.155)
        z_position = tk.Entry(spawn_container)
        z_position.place(relx = 0.19, rely = 0.15, relwidth = 0.04, relheight = 0.05)

        #rotation
        tk.Label(spawn_container, text="Rotation", font=('Helvetica', 20)).place(relx = 0.025, rely = 0.25)
            #pitch
        tk.Label(spawn_container, text="Pitch:",font=('Helvetica', 15)).place(relx = 0.02, rely = 0.305)
        pitch = tk.Entry(spawn_container)
        pitch.place(relx = 0.05, rely = 0.30, relwidth = 0.04, relheight = 0.05)
            #yaw
        tk.Label(spawn_container, text="Yaw:",font=('Helvetica', 15)).place(relx = 0.09, rely = 0.305)
        yaw = tk.Entry(spawn_container)
        yaw.place(relx = 0.12, rely = 0.30, relwidth = 0.04, relheight = 0.05)
            #roll
        tk.Label(spawn_container, text="Roll:",font=('Helvetica', 15)).place(relx = 0.16, rely = 0.305)
        roll = tk.Entry(spawn_container)
        roll.place(relx = 0.19, rely = 0.30, relwidth = 0.04, relheight = 0.05)


        #type
        tk.Label(spawn_container, text="Type", font=('Helvetica', 20)).place(relx = 0.025, rely = 0.4)

        #model


        
        

#intersection page
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



#for switching frames while keeping input data intact
def swap_frames(frame_class1, frame_class2):
        frame_class1.forget()
        frame_class2.pack()


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()