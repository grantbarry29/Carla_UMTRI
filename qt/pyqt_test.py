from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys


#to get window size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()


class Start_Window(QMainWindow):
    def __init__(self):
        super(Start_Window, self).__init__()
        self.setGeometry(0,0,width,height)
        self.setWindowTitle("PyQt_test")
        self.initUI()

    def initUI(self):

        self.firstPage = QWidget()
        self.secondPage = QWidget()
        self.thirdPage = QWidget()
        self.stack = QStackedLayout()
        self.stack.addWidget(self.firstPage)
        self.stack.addWidget(self.secondPage)
        self.stack.addWidget(self.thirdPage)



        #grid       
        grid = QGridLayout()

        #just for layout grid sizing
        self.space = QtWidgets.QLabel(self)
        self.space.setText("")
        self.space2 = QtWidgets.QLabel(self)
        self.space2.setText("")
        grid.addWidget(self.space,100,100,1,1)
        grid.addWidget(self.space2,0,0,1,1)


        #title
        self.title = QtWidgets.QLabel(self)
        self.title.setText("Carla Driving Simulator")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 30))
        grid.addWidget(self.title,64,2)


        #version_text
        self.version = QtWidgets.QLabel(self)
        self.version.setText("Version 0.00")
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setFont(QFont("Arial", 18))
        grid.addWidget(self.version,65,2)


        #freeway button
        self.inter_button = QtWidgets.QPushButton(self)
        self.inter_button.setText("Intersection")
        self.inter_button.clicked.connect(self.inter_click)
        self.inter_button.setMaximumHeight(75)
        self.inter_button.setMaximumWidth(175)
        self.inter_button.setFont(QFont("Arial", 20))
        grid.addWidget(self.inter_button,75,3)


        #intersection button
        self.fway_button = QtWidgets.QPushButton(self)
        self.fway_button.setText("Freeway")
        self.fway_button.clicked.connect(self.fway_click)
        self.fway_button.setMaximumHeight(75)
        self.fway_button.setMaximumWidth(175)
        self.fway_button.setFont(QFont("Arial", 20))
        grid.addWidget(self.fway_button,75,1)


        #set first page to grid
        self.firstPage.setLayout(grid)



        ### SECOND PAGE ###
        grid2 = QGridLayout()
        self.secondPage.setLayout(grid2)

            #second page corner space
        space = QLabel()
        space.setText("")
        grid2.addWidget(space,10,4,1,1)

            #second page back button
        back = QPushButton()
        back.setText("Back")
        back.setFont(QFont("Arial", 16))
        back.clicked.connect(self.back_to_home)
        back.setMaximumHeight(50)
        back.setMaximumWidth(75)
        grid2.addWidget(back,0,0)

            #second page labels
        gen_settings = QLabel("General Settings")
        gen_settings.setFont(QFont("Arial", 20))
        grid2.addWidget(gen_settings,1,1)

        num_sections = QLabel("Number of Sections")
        allow_collision = QLabel("Allow Collisions")
        min_speed = QLabel("Minimum Speed")
        max_speed = QLabel("Maximum Speed")
        safety_dist = QLabel("Safety Distance (m)")

        num_sections.setFont(QFont("Arial", 16))
        allow_collision.setFont(QFont("Arial", 16))
        min_speed.setFont(QFont("Arial", 16))
        max_speed.setFont(QFont("Arial", 16))
        safety_dist.setFont(QFont("Arial", 16))

        grid2.addWidget(num_sections,2,1)
        grid2.addWidget(allow_collision,3,1)
        grid2.addWidget(min_speed,4,1)
        grid2.addWidget(max_speed,5,1)
        grid2.addWidget(safety_dist,6,1)

            #second page input boxes
        num_sections_box = QLineEdit()
        allow_collision_box = QLineEdit()
        min_speed_box = QLineEdit()
        max_speed_box = QLineEdit()
        safety_dist_box = QLineEdit()

        num_sections_box.setMaximumSize(30,30)
        allow_collision_box.setMaximumSize(30,30)
        min_speed_box.setMaximumSize(30,30)
        max_speed_box.setMaximumSize(30,30)
        safety_dist_box.setMaximumSize(30,30)

        grid2.addWidget(num_sections_box,2,2)
        grid2.addWidget(allow_collision_box,3,2)
        grid2.addWidget(min_speed_box,4,2)
        grid2.addWidget(max_speed_box,5,2)
        grid2.addWidget(safety_dist_box,6,2)

            #second page road image
        road_image = QPixmap("roads.png")
        road_image = road_image.scaledToHeight(int(height/2))
        image_label = QLabel()
        image_label.setPixmap(road_image)
        grid2.addChildWidget(image_label)
        image_label.move(int(width/2),int(height/4))

            #second page edit button
        edit_sim = QPushButton("Edit Simulation")
        edit_sim.setMaximumWidth(200)
        grid2.addWidget(edit_sim,7,1,1,1)






        ### THIRD PAGE ###
        grid3 = QGridLayout()
        self.thirdPage.setLayout(grid3)

            #third page corner space
        space3 = QLabel()
        space3.setText("")
        grid3.addWidget(space3,10,4,1,1)

            #third page back button
        back3 = QPushButton()
        back3.setText("Back")
        back3.setFont(QFont("Arial", 16))
        back3.clicked.connect(self.back_to_home)
        back3.setMaximumHeight(50)
        back3.setMaximumWidth(75)
        grid3.addWidget(back3,0,0)

            #third page labels
        gen_settings3 = QLabel("General Settings")
        gen_settings3.setFont(QFont("Arial", 20))
        grid3.addWidget(gen_settings3,1,1)

        num_sections3 = QLabel("Number of Intersections")
        allow_collision3 = QLabel("Allow Collisions")
        min_speed3 = QLabel("Minimum Speed")
        max_speed3 = QLabel("Maximum Speed")
        safety_dist3 = QLabel("Safety Distance (m)")

        num_sections3.setFont(QFont("Arial", 16))
        allow_collision3.setFont(QFont("Arial", 16))
        min_speed3.setFont(QFont("Arial", 16))
        max_speed3.setFont(QFont("Arial", 16))
        safety_dist3.setFont(QFont("Arial", 16))

        grid3.addWidget(num_sections3,2,1)
        grid3.addWidget(allow_collision3,3,1)
        grid3.addWidget(min_speed3,4,1)
        grid3.addWidget(max_speed3,5,1)
        grid3.addWidget(safety_dist3,6,1)


            #third page input boxes
        num_sections_box3 = QLineEdit()
        allow_collision_box3 = QLineEdit()
        min_speed_box3 = QLineEdit()
        max_speed_box3 = QLineEdit()
        safety_dist_box3 = QLineEdit()

        num_sections_box3.setMaximumSize(30,30)
        allow_collision_box3.setMaximumSize(30,30)
        min_speed_box3.setMaximumSize(30,30)
        max_speed_box3.setMaximumSize(30,30)
        safety_dist_box3.setMaximumSize(30,30)

        grid3.addWidget(num_sections_box3,2,2)
        grid3.addWidget(allow_collision_box3,3,2)
        grid3.addWidget(min_speed_box3,4,2)
        grid3.addWidget(max_speed_box3,5,2)
        grid3.addWidget(safety_dist_box3,6,2)


            #third page road image
        road_image3 = QPixmap("roads.png")
        road_image3 = road_image.scaledToHeight(int(height/2))
        image_label3 = QLabel()
        image_label3.setPixmap(road_image3)
        grid3.addChildWidget(image_label3)
        image_label3.move(int(width/2),int(height/4))

            #third page edit button
        edit_sim3 = QPushButton("Edit Simulation")
        edit_sim3.setMaximumWidth(200)
        grid3.addWidget(edit_sim3,7,1,1,1)



        #SET STACK
        widget = QWidget()
        widget.setLayout(self.stack)
        self.setCentralWidget(widget)

    def back_to_home(self):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,self.firstPage)

    def fway_click(self):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,self.secondPage)
    
    def inter_click(self):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,self.thirdPage)


def main():
    app = QApplication(sys.argv)
    win = Start_Window()
    win.show()
    sys.exit(app.exec_())


main()