import tkinter as tk
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from Circular_meter import Meter
from tkinter import PhotoImage
import track_meals
from Database.meals_functions import get_nutrition_consumed
from Database.user_activity_functions import get_water_consumed , update_water_consumed,get_hours_slept,update_sleep_hours
from Watch.steps_walked import get_user_activity
from datetime import datetime
from globalStore import current_user
# from Workout_page_changes import run_workout_page
from final_workout import run_workout_page
# from yoga import YogaScrollableFrame
# from Workout_page_changes import ExerciseImageLoader


date_string = "2024-03-29"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

class Dashboard(customtkinter.CTk):

    APP_NAME = "Custom Dashboard"
    WIDTH = 1300
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Dashboard.APP_NAME)
        self.geometry(str(Dashboard.WIDTH) + "x" + str(Dashboard.HEIGHT))
        self.minsize(Dashboard.WIDTH, Dashboard.HEIGHT)
        self.appearance_mode = "Light"
        # print(current_user['username'])
        # self.today_date = datetime.today().date()
        self.today_nutrition_values = get_nutrition_consumed("AtharvaYadav",parsed_date)

        self.totalCalories = 3000
        self.CaloriesUsed = self.today_nutrition_values["Total_Calories"]

        self.protiens_target = 300
        self.protiens_consumed = self.today_nutrition_values["Total_Protein"]
        self.protiens_percent = self.protiens_consumed/self.protiens_target

        self.carbs_target = 600
        self.carbs_consumed = self.today_nutrition_values["Total_Carbohydrates"]
        self.carbs_percent = self.carbs_consumed/self.carbs_target

        self.fats_target = 800 
        self.fats_consumed = self.today_nutrition_values["Total_Fats"]
        self.fats_percent = self.fats_consumed/self.fats_target

        self.fiber_target = 80 
        self.fiber_consumed = self.today_nutrition_values["Total_Fiber"]
        self.fiber_percent = self.fiber_consumed/self.fiber_target

        #User Activity
        self.water_consumed = get_water_consumed("AtharvaYadav",parsed_date)
        self.calories_burned = get_user_activity(parsed_date)['cals']
        self.target_calories_burned = 2400
        self.current_weight = 80
        self.target_weight = 65
        self.wt_lost = 4
        self.max_wt_lost = 15
        self.steps_walked = get_user_activity(parsed_date)['steps']
        self.hours_slept = get_hours_slept("AtharvaYadav",parsed_date)
        
        

        # self.resizable(False, False)


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Custom Dashboard", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Chat",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="User",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="workout",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.add_user_image, anchor="w",  command=self.open_workout_page)
        self.frame_4_button.grid(row=3, column=0, sticky="ew")



  

        #create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame.columnconfigure(0,weight=1)
        self.home_frame.rowconfigure(0,weight=10)
        self.home_frame.rowconfigure(1,weight=20)

        
        self.nutrition_frame = customtkinter.CTkFrame(self.home_frame)
        self.health_frame = customtkinter.CTkFrame(self.home_frame)

      
        self.nutrition_frame.grid(row=0,column=0,sticky='nsew')
        self.health_frame.grid(row=1,column=0,sticky='nsew')

        self.nutrition_frame.columnconfigure(0,weight=3)
        self.nutrition_frame.rowconfigure(0,weight=1)

        self.calorie_frame = customtkinter.CTkFrame(self.nutrition_frame,fg_color=("white","black"),corner_radius=10)
        self.calorie_frame.grid(row=0, column=0, sticky='nsew', padx=10,pady=10)
        
        self.calorie_frame.columnconfigure(0,weight=2)
        self.calorie_frame.columnconfigure(1,weight=2)
        self.calorie_frame.columnconfigure(2,weight=1)
        self.calorie_frame.rowconfigure(0,weight=1)

        self.meter = Meter(self.calorie_frame, metersize=180, padding=0, amountused= self.CaloriesUsed, amounttotal=self.totalCalories,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/spoon.png',wedgecolor='orange',appearance_mode= self.appearance_mode)
        self.meter.grid(row=0, column=0) 

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

        self.calorie_frame3_label1 = customtkinter.CTkLabel(self.calorie_frame3_labels,text=f"{self.CaloriesUsed} of {self.totalCalories}",font=("Helvetica", 24))
        self.calorie_frame3_label1.grid(row=0,column=0,sticky="w")
        self.calorie_frame3_label2 = customtkinter.CTkLabel(self.calorie_frame3_labels,text="Cal Eaten",font=("Helvetica", 12),text_color='#D3D3D3')
        self.calorie_frame3_label2.grid(row=1,column=0,sticky="w",pady=5)
        self.add_meals = customtkinter.CTkButton(self.calorie_frame3_labels,text="Add meals",fg_color='orange',command=self.open_daily_meals)
        self.add_meals.grid(row=2,column=0)


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

        self.progress_bar1_label = customtkinter.CTkLabel(self.progress_frame1,text=f"Protien:{self.protiens_percent * 100:.2f}%")
        self.progress_bar1 = customtkinter.CTkProgressBar(self.progress_frame1,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar1.grid(row=1,column=0)
        self.progress_bar1.set(self.protiens_percent)
        self.progress_bar1_label.grid(row=0,column=0)

        self.progress_bar2_label = customtkinter.CTkLabel(self.progress_frame2,text=f"Carbohydrates:{self.carbs_percent*100:.2f}%")
        self.progress_bar2 = customtkinter.CTkProgressBar(self.progress_frame2,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar2.grid(row=1,column=0)
        self.progress_bar2.set(self.carbs_percent)
        self.progress_bar2_label.grid(row=0,column=0)

        self.progress_bar3_label = customtkinter.CTkLabel(self.progress_frame3,text=f"Fats:{self.fats_percent*100:.2f}%")
        self.progress_bar3 = customtkinter.CTkProgressBar(self.progress_frame3,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar3.grid(row=1,column=0)
        self.progress_bar3.set(self.fats_percent)
        self.progress_bar3_label.grid(row=0,column=0)

        self.progress_bar4_label = customtkinter.CTkLabel(self.progress_frame4,text=f"Fiber:{self.fiber_percent*100:.2f}%")
        self.progress_bar4 = customtkinter.CTkProgressBar(self.progress_frame4,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar4.grid(row=1,column=0)
        self.progress_bar4.set(self.fiber_percent)
        self.progress_bar4_label.grid(row=0,column=0)

        #Health Frame
        self.health_frame.rowconfigure((0,1),weight=1)
        self.health_frame.columnconfigure((0,1,2),weight=1)

        # 6 Frames
        self.cal_burned_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.target_wt_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.steps_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.watch_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.sleep_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))
        self.waterr_frame = customtkinter.CTkFrame(self.health_frame,fg_color=("white","black"))

        #Arranging Frames
        self.cal_burned_frame.grid(row=0,column=0)
        self.target_wt_frame.grid(row=0,column=1)
        self.steps_frame.grid(row=1,column=0)
        self.watch_frame.grid(row=1,column=1)
        self.sleep_frame.grid(row=1,column=2)
        self.waterr_frame.grid(row=0,column=2)
        

        
        #Creating 4 Cards
        self.calorie_burn_meter = Meter(self.cal_burned_frame, metersize=180, padding=0, amountused=self.calories_burned, amounttotal=self.target_calories_burned,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/runner3.png',wedgecolor='#41C9E2',appearance_mode= self.appearance_mode)
        self.calorie_burn_label = customtkinter.CTkLabel(self.cal_burned_frame,text=f"{self.calories_burned} of {self.target_calories_burned}")
        self.calorie_burn_label2 = customtkinter.CTkLabel(self.cal_burned_frame,text="Cals Burned",text_color="#607274")

        self.calorie_burn_meter.pack(padx=45,pady=20)
        self.calorie_burn_label.pack()
        self.calorie_burn_label2.pack()


        self.plus_image = customtkinter.CTkImage(Image.open("assets/images/black_plus.png"))
        self.minus_image = customtkinter.CTkImage(Image.open("assets/images/black_minus.png"))
        self.target_wt_meter = Meter(self.target_wt_frame, metersize=180, padding=0, amountused=self.wt_lost, amounttotal=self.max_wt_lost,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image= './assets/images/weight.png',wedgecolor='#99BC85',appearance_mode= self.appearance_mode)
        self.target_wt_label = customtkinter.CTkLabel(self.target_wt_frame,text=f"{self.wt_lost} of {self.max_wt_lost}")
        self.target_wt_label2 = customtkinter.CTkLabel(self.target_wt_frame,text="Weight Lost",text_color='#607274')
        self.add_wt_button = customtkinter.CTkButton(self.target_wt_frame,image=self.plus_image,text ="",fg_color='transparent',width=20, command=lambda: self.adjust_weight_meter(delta=-1))
        self.minus_wt_button = customtkinter.CTkButton(self.target_wt_frame,image=self.minus_image,text ="",fg_color='transparent',width=20, command=lambda: self.adjust_weight_meter(delta=1))
        self.target_wt_meter.pack(padx=45,pady=20)
        self.add_wt_button.place(relx=1, rely=0.5, anchor='e')  # Place plus button at center right
        self.minus_wt_button.place(relx=0, rely=0.5, anchor='w')
        self.target_wt_label.pack()
        self.target_wt_label2.pack()
        # Place minus button on the left


        self.steps_meter = Meter(self.steps_frame, metersize=180, padding=0, amountused=self.steps_walked, amounttotal=10000,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/boots4.png',wedgecolor='#FBA834',appearance_mode= self.appearance_mode)
        self.steps_label = customtkinter.CTkLabel(self.steps_frame,text="Steps walked Today",text_color='#607274')
        self.steps_label2 = customtkinter.CTkLabel(self.steps_frame,text= self.steps_walked)

        self.steps_meter.pack(padx=45,pady=20)
        self.steps_label.pack()
        self.steps_label2.pack()

        self.sleep_meter = Meter(self.watch_frame, metersize=180, padding=0, amountused=self.hours_slept, amounttotal=7,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/night3.png',wedgecolor='#211C6A',appearance_mode= self.appearance_mode)
        self.sleep_label = customtkinter.CTkLabel(self.watch_frame,text='Hours Slept',text_color='#607274')
        self.sleep_label2 = customtkinter.CTkLabel(self.watch_frame,text=self.hours_slept)
        self.add_sleep_button = customtkinter.CTkButton(self.watch_frame,image=self.plus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_sleep_hours(delta=-0.5))
        self.minus_sleep_button = customtkinter.CTkButton(self.watch_frame,image=self.minus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_sleep_hours(delta=0.5))
        self.sleep_meter.pack(padx=45,pady=20)
        self.add_sleep_button.place(relx=1, rely=0.5, anchor='e')  # Place plus button at center right
        self.minus_sleep_button.place(relx=0, rely=0.5, anchor='w')
       
        self.sleep_label.pack()
        self.sleep_label2.pack()

        #Water Meter

        self.waterr_meter = Meter(self.waterr_frame, metersize=180, padding=0, amountused= self.water_consumed, amounttotal=10,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image= './assets/images/water3.png',wedgecolor='#008DDA',appearance_mode= self.appearance_mode)
        self.waterr_label = customtkinter.CTkLabel(self.waterr_frame,text=f"{self.water_consumed} of 10")
        self.waterr_label2 = customtkinter.CTkLabel(self.waterr_frame,text="Glasses consumed",text_color='#607274')
        self.add_water_button = customtkinter.CTkButton(self.waterr_frame,image=self.plus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_water_glass(delta=-1))
        self.minus_water_button = customtkinter.CTkButton(self.waterr_frame,image=self.minus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_water_glass(delta=1))
        self.waterr_meter.pack(padx=45,pady=20)
        self.add_water_button.place(relx=1, rely=0.5, anchor='e')  # Place plus button at center right
        self.minus_water_button.place(relx=0, rely=0.5, anchor='w')
        self.waterr_label.pack()
        self.waterr_label2.pack()
            
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def open_workout_page(self):
                run_workout_page()

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def adjust_water_glass(self, delta):
        if delta < 0:  
            self.waterr_meter.step(delta=-1)
            self.water_consumed += 1
        else: 
            self.waterr_meter.step(delta=1)
            self.water_consumed -= 1

        self.waterr_label.configure(text=f"{self.water_consumed} of 10")
        update_water_consumed("AtharvaYadav",parsed_date,self.water_consumed)

    def adjust_weight_meter(self, delta):
        if delta < 0:  
            self.target_wt_meter.step(delta=-1)
            self.wt_lost += 1
        else: 
            self.target_wt_meter.step(delta=1)
            self.wt_lost -= 1

        self.target_wt_label.configure(text=f"{self.wt_lost} of {self.max_wt_lost}")

    def adjust_sleep_hours(self,delta):
        if delta < 0:  
            self.sleep_meter.step(delta=-1)
            self.hours_slept += 1
        else: 
            self.sleep_meter.step(delta=0.5)
            self.hours_slept -= 1

        self.sleep_label2.configure(text=f"{self.hours_slept} of 7")
        update_sleep_hours("AtharvaYadav",parsed_date,self.hours_slept)

    def open_daily_meals(self):
        self.destroy()  
        track_meals.Track_meals().mainloop()
        
    def change_appearance_mode_event(self, new_appearance_mode):
        self.appearance_mode = new_appearance_mode
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.meter.change_appearance(new_appearance_mode)
        self.waterr_meter.change_appearance(new_appearance_mode)
        self.steps_meter.change_appearance(new_appearance_mode)
        self.calorie_burn_meter.change_appearance(new_appearance_mode)
        self.self.target_wt_meter.change_appearance(new_appearance_mode)
        
        