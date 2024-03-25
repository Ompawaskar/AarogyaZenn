import tkinter as tk
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from Circular_meter import Meter

class MainDashBoard(customtkinter.CTk):
     def __init__(self, appearance_mode = "Light",master=None):
        super().__init__()
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame.columnconfigure(0,weight=1)
        # self.home_frame.rowconfigure(0,weight=1)
        self.home_frame.rowconfigure(0,weight=10)
        self.home_frame.rowconfigure(1,weight=20)

        # self.header_frame = customtkinter.CTkFrame(self.home_frame,fg_color='red')
        self.nutrition_frame = customtkinter.CTkFrame(self.home_frame)
        self.health_frame = customtkinter.CTkFrame(self.home_frame)

        # self.header_frame.grid(row=0,column=0,sticky='nsew')
        self.nutrition_frame.grid(row=0,column=0,sticky='nsew')
        self.health_frame.grid(row=1,column=0,sticky='nsew')

        self.nutrition_frame.columnconfigure(0,weight=3)
        self.nutrition_frame.columnconfigure(1,weight=1)
        self.nutrition_frame.rowconfigure(0,weight=1)

        self.calorie_frame = customtkinter.CTkFrame(self.nutrition_frame,fg_color=("white","black"))
        self.water_frame = customtkinter.CTkFrame(self.nutrition_frame,fg_color=("white","black"))

        self.calorie_frame.grid(row=0, column=0, sticky='nsew', padx=10,pady=10)
        self.water_frame.grid(row=0, column=1, sticky='nsew')

        self.water_frame.columnconfigure(0,weight=1)
        self.water_frame.rowconfigure(0,weight=1)

        self.water_subframe = customtkinter.CTkFrame(self.water_frame,fg_color=("white","black"))
        self.water_subframe.grid(row=0,column=0)

        self.water_subframe.columnconfigure(0,weight=1)
        self.water_subframe.columnconfigure(1,weight=4)
        self.water_subframe.columnconfigure(2,weight=1)
        self.water_subframe.rowconfigure(0,weight=1)

        self.calorie_frame.columnconfigure(0,weight=2)
        self.calorie_frame.columnconfigure(1,weight=2)
        self.calorie_frame.columnconfigure(2,weight=1)
        self.calorie_frame.rowconfigure(0,weight=1)

        self.meter = Meter(self.calorie_frame, metersize=180, padding=0, amountused=2400, amounttotal=2600,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='orange',appearance_mode= self.appearance_mode)
        self.meter.grid(row=0, column=0) 

        self.water_meter = Meter(self.water_subframe, metersize=180, padding=0, amountused=10, amounttotal=10,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='blue',appearance_mode= self.appearance_mode)
        self.water_meter.grid(row=0, column=1) 

        self.water_label = customtkinter.CTkLabel(self.water_frame,text='0 of 9 Glasses')
        self.water_label.grid(row=0,column=0,sticky='s')
        

        self.calorie_frame2 = customtkinter.CTkFrame(self.calorie_frame,fg_color=("white","black"))
        self.calorie_frame2.grid(row=0,column=2,sticky='ew')
        self.calorie_frame2.columnconfigure((0,1),weight=1)
        self.calorie_frame2.rowconfigure((0,1),weight=1)

        self.calorie_frame3 = customtkinter.CTkFrame(self.calorie_frame,fg_color=("white","black"))
        self.calorie_frame3.grid(row=0,column=1,sticky="nw")
        self.calorie_frame3.columnconfigure(0,weight=1)
        self.calorie_frame3.rowconfigure(0,weight=1)

        self.calorie_frame3_labels = customtkinter.CTkFrame(self.calorie_frame3,fg_color=("white","black"))
        self.calorie_frame3_labels.grid(row=0,column=0,sticky="w",pady=45)

        self.calorie_frame3_label1 = customtkinter.CTkLabel(self.calorie_frame3_labels,text="148 of 2250",font=("Helvetica", 24))
        self.calorie_frame3_label1.grid(row=0,column=0)
        self.calorie_frame3_label2 = customtkinter.CTkLabel(self.calorie_frame3_labels,text="Cal Eaten",font=("Helvetica", 12))
        self.calorie_frame3_label2.grid(row=1,column=0,sticky="w")


        self.progress_frame1 = customtkinter.CTkFrame(self.calorie_frame2,fg_color=("white","black"))
        self.progress_frame1.grid(row=0,column=0,padx=10,pady=10)
        self.progress_frame1.columnconfigure(0,weight=1)
        self.progress_frame1.rowconfigure((0,1),weight=1)

        self.progress_frame2 = customtkinter.CTkFrame(self.calorie_frame2,fg_color=("white","black"))
        self.progress_frame2.grid(row=0,column=1,padx=10,pady=10)
        self.progress_frame2.columnconfigure(0,weight=1)
        self.progress_frame2.rowconfigure((0,1),weight=1)

        self.progress_frame3 = customtkinter.CTkFrame(self.calorie_frame2,fg_color=("white","black"))
        self.progress_frame3.grid(row=1,column=0,padx=10,pady=10)
        self.progress_frame3.columnconfigure(0,weight=1)
        self.progress_frame3.rowconfigure((0,1),weight=1)

        self.progress_frame4 = customtkinter.CTkFrame(self.calorie_frame2,fg_color=("white","black"))
        self.progress_frame4.grid(row=1,column=1,padx=10,pady=10)
        self.progress_frame4.columnconfigure(0,weight=1)
        self.progress_frame4.rowconfigure((0,1),weight=1)

        self.progress_bar1_label = customtkinter.CTkLabel(self.progress_frame1,text="Protien:50%")
        self.progress_bar1 = customtkinter.CTkProgressBar(self.progress_frame1,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar1.grid(row=1,column=0)
        self.progress_bar1.set(0.5)
        self.progress_bar1_label.grid(row=0,column=0)

        self.progress_bar2_label = customtkinter.CTkLabel(self.progress_frame2,text="Carbs:50%")
        self.progress_bar2 = customtkinter.CTkProgressBar(self.progress_frame2,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar2.grid(row=1,column=0)
        self.progress_bar2.set(0.5)
        self.progress_bar2_label.grid(row=0,column=0)

        self.progress_bar3_label = customtkinter.CTkLabel(self.progress_frame3,text="Protien:50%")
        self.progress_bar3 = customtkinter.CTkProgressBar(self.progress_frame3,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar3.grid(row=1,column=0)
        self.progress_bar3.set(0.5)
        self.progress_bar3_label.grid(row=0,column=0)

        self.progress_bar4_label = customtkinter.CTkLabel(self.progress_frame4,text="Protien:50%")
        self.progress_bar4 = customtkinter.CTkProgressBar(self.progress_frame4,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar4.grid(row=1,column=0)
        self.progress_bar4.set(0.5)
        self.progress_bar4_label.grid(row=0,column=0)

        #Health Frame
        self.health_frame.rowconfigure((0,1),weight=1)
        self.health_frame.columnconfigure((0,1),weight=1)

        # 4 Frames
        self.cal_burned_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.target_wt_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.steps_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.watch_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))

        #Arranging Frames
        self.cal_burned_frame.grid(row=0,column=0)
        self.target_wt_frame.grid(row=0,column=1)
        self.steps_frame.grid(row=1,column=0)
        self.watch_frame.grid(row=1,column=1)
        

        #Creating 4 Cards
        self.calorie_burn_meter = Meter(self.cal_burned_frame, metersize=180, padding=0, amountused=10, amounttotal=447,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='purple',appearance_mode= self.appearance_mode)
        self.calorie_burn_label = customtkinter.CTkLabel(self.cal_burned_frame,text="0 of 447")
        self.calorie_burn_label2 = customtkinter.CTkLabel(self.cal_burned_frame,text="cals Burned")

        self.calorie_burn_meter.pack(padx=45,pady=20)
        self.calorie_burn_label.pack()
        self.calorie_burn_label2.pack()


        self.target_wt_meter = Meter(self.target_wt_frame, metersize=180, padding=0, amountused=10, amounttotal=447,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='purple',appearance_mode= self.appearance_mode)
        self.target_wt_label = customtkinter.CTkLabel(self.target_wt_frame,text="0 of 447")
        self.target_wt_label2 = customtkinter.CTkLabel(self.target_wt_frame,text="cals Burned")

        self.target_wt_meter.pack(padx=45,pady=20)
        self.target_wt_label.pack()
        self.target_wt_label2.pack()


        self.steps_meter = Meter(self.steps_frame, metersize=180, padding=0, amountused=10, amounttotal=447,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='purple',appearance_mode= self.appearance_mode)
        self.steps_label = customtkinter.CTkLabel(self.steps_frame,text="Steps walked Today")
        self.steps_label2 = customtkinter.CTkLabel(self.steps_frame,text="2000")

        self.steps_meter.pack(padx=45,pady=20)
        self.steps_label.pack()
        self.steps_label2.pack()

        self.sleep_meter = Meter(self.watch_frame, metersize=180, padding=0, amountused=10, amounttotal=447,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./spoon-and-fork.png',wedgecolor='purple',appearance_mode= self.appearance_mode)
        self.sleep_label = customtkinter.CTkLabel(self.watch_frame,text="Steps walked Today")
        self.sleep_label2 = customtkinter.CTkLabel(self.watch_frame,text="2000")

        self.sleep_meter.pack(padx=45,pady=20)
        self.sleep_label.pack()
        self.sleep_label2.pack()

     
   
    
