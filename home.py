import tkinter as tk
from tkinter import ttk
import customtkinter
import os
import sys
from PIL import Image
from Circular_meter import Meter
from tkinter import PhotoImage
import track_meals
# from Database.Calculations import calculate_daily_calories
from Database.meals_functions import get_nutrition_consumed,get_total_calories
from Database.user_activity_functions import UserActivity
from Watch.steps_walked import get_user_activity
from datetime import datetime
from globalStore import current_user,user_meal
from progress_report import Progress
import Workout_page_changes
import track_meals

date_string = "2024-03-29"
# Get today's date
today_date = datetime.today()

# Format today's date as a string in "YYYY-MM-DD" format
today_date_string = today_date.strftime("%Y-%m-%d")

# Parse the formatted date string back to a datetime object
parsed_date = datetime.strptime(today_date_string, "%Y-%m-%d")

class Dashboard(customtkinter.CTk):

    APP_NAME = "Custom Dashboard"
    WIDTH = 1300
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(Dashboard.APP_NAME)
        self.geometry(str(Dashboard.WIDTH) + "x" + str(Dashboard.HEIGHT))
        self.minsize(Dashboard.WIDTH, Dashboard.HEIGHT)
        self.user = current_user['username']
        print(self.user)
        self.user_activity = UserActivity(self.user,parsed_date)
        # self.bind("<<MealSubmitted>>", self.handle_meal_submission)

        self.today_nutrition_values = get_nutrition_consumed(self.user,parsed_date)
        self.totalCalories = round(get_total_calories(self.user))
        self.CaloriesUsed = round(self.today_nutrition_values["Total_Calories"])
        self.protiens_target = round(self.get_max_nutritional_contents()['protein_grams'])
        self.protiens_consumed = self.today_nutrition_values["Total_Protein"]
        self.protiens_percent = self.protiens_consumed/self.protiens_target

        self.carbs_target = round(self.get_max_nutritional_contents()['carbs_grams'])
        self.carbs_consumed = self.today_nutrition_values["Total_Carbohydrates"]
        self.carbs_percent = self.carbs_consumed/self.carbs_target
        self.fats_target = round(self.get_max_nutritional_contents()['fats_grams']) 
        self.fats_consumed = self.today_nutrition_values["Total_Fats"]
        self.fats_percent = self.fats_consumed/self.fats_target

        self.fiber_target =round(self.get_max_nutritional_contents()['fiber_grams'])
        self.fiber_consumed = self.today_nutrition_values["Total_Fiber"]
        self.fiber_percent = self.fiber_consumed/self.fiber_target

        #User Activity
        self.water_consumed = self.user_activity.get_attribute('water_drank')
        self.calories_burned = get_user_activity(parsed_date,self.user)['cals']
        self.target_calories_burned = 2400
        self.current_weight = 80
        self.target_weight = 65
        self.wt_lost = 0
        self.max_wt_lost = 15
        self.steps_walked = get_user_activity(parsed_date,self.user)['steps']
        self.hours_slept =self.user_activity.get_attribute('hours_slept')

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
        self.navigation_frame = customtkinter.CTkFrame(self,corner_radius = 5 , border_color = '#A4B494' , border_width = 1,fg_color='white')
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame,text="AarogyaZen", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius = 5 , border_color = '#A4B494' , border_width = 1, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius = 5 , border_color = '#A4B494' , border_width = 1, height=40, border_spacing=10, text="Workout",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius = 5 , border_color = '#A4B494' , border_width = 1, height=40, border_spacing=10, text="Yoga",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius = 5 , border_color = '#A4B494' , border_width = 1, height=40, border_spacing=10, text="Progress",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        #create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="white")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame.columnconfigure(0,weight=1)
        self.home_frame.rowconfigure(0,weight=10)
        self.home_frame.rowconfigure(1,weight=20)

        
        self.nutrition_frame = customtkinter.CTkFrame(self.home_frame,fg_color="white", corner_radius = 5 , border_color = '#A4B494' , border_width = 1)
        self.health_frame = customtkinter.CTkFrame(self.home_frame,fg_color="white")

        self.nutrition_frame.grid(row=0,column=0,sticky='nsew',padx=5,pady = 5)
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
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/spoon.png',wedgecolor='orange',appearance_mode= 'Light')
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

        self.progress_bar1_label = customtkinter.CTkLabel(self.progress_frame1,text=f"Protien: {self.protiens_consumed} of {self.protiens_target} g")
        self.progress_bar1 = customtkinter.CTkProgressBar(self.progress_frame1,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar1.grid(row=1,column=0)
        self.progress_bar1.set(self.protiens_percent)
        self.progress_bar1_label.grid(row=0,column=0)

        self.progress_bar2_label = customtkinter.CTkLabel(self.progress_frame2,text=f"Carbohydrates: {self.carbs_consumed} of {self.carbs_target} g")
        self.progress_bar2 = customtkinter.CTkProgressBar(self.progress_frame2,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar2.grid(row=1,column=0)
        self.progress_bar2.set(self.carbs_percent)
        self.progress_bar2_label.grid(row=0,column=0)

        self.progress_bar3_label = customtkinter.CTkLabel(self.progress_frame3,text=f"Fats: {self.fats_consumed} of {self.fats_target} g")
        self.progress_bar3 = customtkinter.CTkProgressBar(self.progress_frame3,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar3.grid(row=1,column=0)
        self.progress_bar3.set(self.fats_percent)
        self.progress_bar3_label.grid(row=0,column=0)

        self.progress_bar4_label = customtkinter.CTkLabel(self.progress_frame4,text=f"Fiber: {self.fiber_consumed} of {self.fiber_target} g")
        self.progress_bar4 = customtkinter.CTkProgressBar(self.progress_frame4,mode="determinate",progress_color="orange",width=150) 
        self.progress_bar4.grid(row=1,column=0)
        self.progress_bar4.set(self.fiber_percent)
        self.progress_bar4_label.grid(row=0,column=0)

        #Health Frame
        self.health_frame.rowconfigure((0,1),weight=1)
        self.health_frame.columnconfigure((0,1,2),weight=1)

        # 6 Frames
        self.cal_burned_frame = customtkinter.CTkFrame(self.health_frame,corner_radius = 5 , border_color = '#A4B494' , border_width = 1 , fg_color = 'white')
        self.target_wt_frame = customtkinter.CTkFrame(self.health_frame,corner_radius = 5 , border_color = '#A4B494' , border_width = 1,fg_color = 'white')
        self.steps_frame = customtkinter.CTkFrame(self.health_frame, border_color = '#A4B494' , border_width = 1 , fg_color = 'white')
        self.watch_frame = customtkinter.CTkFrame(self.health_frame, border_color = '#A4B494' , border_width = 1 , fg_color = 'white')
        self.sleep_frame = customtkinter.CTkFrame(self.health_frame, border_color = '#A4B494' , border_width = 1 , fg_color = 'white')
        self.waterr_frame = customtkinter.CTkFrame(self.health_frame,fg_color = 'white',border_color = '#A4B494' , border_width = 1)

        #Arranging Frames
        self.cal_burned_frame.grid(row=0,column=0)
        self.target_wt_frame.grid(row=0,column=1)
        self.steps_frame.grid(row=1,column=0)
        self.watch_frame.grid(row=1,column=1)
        self.sleep_frame.grid(row=1,column=2)
        self.waterr_frame.grid(row=0,column=2)
        

        #Creating 4 Cards
        self.calorie_burn_meter = Meter(self.cal_burned_frame, metersize=180, padding=0, amountused=self.calories_burned, amounttotal=self.target_calories_burned,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/runner3.png',wedgecolor='#41C9E2',appearance_mode= "Light")
        self.calorie_burn_label = customtkinter.CTkLabel(self.cal_burned_frame,text=f"{self.calories_burned} of {self.target_calories_burned}")
        self.calorie_burn_label2 = customtkinter.CTkLabel(self.cal_burned_frame,text="Cals Burned",text_color="#607274")

        self.calorie_burn_meter.pack(padx=45,pady=20)
        self.calorie_burn_label.pack()
        self.calorie_burn_label2.pack(pady = 2)

        self.plus_image = customtkinter.CTkImage(Image.open("assets/images/black_plus.png"))
        self.minus_image = customtkinter.CTkImage(Image.open("assets/images/black_minus.png"))
        self.target_wt_meter = Meter(self.target_wt_frame, metersize=180, padding=0, amountused=self.wt_lost, amounttotal=self.max_wt_lost,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image= './assets/images/weight.png',wedgecolor='#99BC85',appearance_mode= "Light")
        self.target_wt_label = customtkinter.CTkLabel(self.target_wt_frame,text=f"{self.wt_lost} of {self.max_wt_lost}")
        self.target_wt_label2 = customtkinter.CTkLabel(self.target_wt_frame,text="Weight Lost",text_color='#607274')
        self.add_wt_button = customtkinter.CTkButton(self.target_wt_frame,image=self.plus_image,text ="",fg_color='transparent',width=20, command=lambda: self.adjust_weight_meter(delta=-1))
        self.minus_wt_button = customtkinter.CTkButton(self.target_wt_frame,image=self.minus_image,text ="",fg_color='transparent',width=20, command=lambda: self.adjust_weight_meter(delta=1))
        self.target_wt_meter.pack(padx=45,pady=20)
        # For the plus button
        self.add_wt_button.place(relx=1, rely=0.5, anchor='e', x=-4)  # Adjust x position to add padding

        # For the minus button
        self.minus_wt_button.place(relx=0, rely=0.5, anchor='w', x=4)  # Adjust x position to add padding


        self.target_wt_label.pack()
        self.target_wt_label2.pack(pady = 1)
        # Place minus button on the left

        self.steps_meter = Meter(self.steps_frame, metersize=180, padding=0, amountused=self.steps_walked, amounttotal=10000,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/boots4.png',wedgecolor='#FBA834',appearance_mode= "Light")
        self.steps_label = customtkinter.CTkLabel(self.steps_frame,text="Steps walked Today",text_color='#607274')
        self.steps_label2 = customtkinter.CTkLabel(self.steps_frame,text= self.steps_walked)

        self.steps_meter.pack(padx=45,pady=20)
        self.steps_label.pack(pady = 1)
        self.steps_label2.pack(pady = 1)

        self.sleep_meter = Meter(self.watch_frame, metersize=180, padding=0, amountused=self.hours_slept, amounttotal=7,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image='./assets/images/night3.png',wedgecolor='#211C6A',appearance_mode= "Light")
        self.sleep_label = customtkinter.CTkLabel(self.watch_frame,text='Hours Slept',text_color='#607274')
        self.sleep_label2 = customtkinter.CTkLabel(self.watch_frame,text=self.hours_slept)
        self.add_sleep_button = customtkinter.CTkButton(self.watch_frame,image=self.plus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_sleep_hours(delta=-0.5))
        self.minus_sleep_button = customtkinter.CTkButton(self.watch_frame,image=self.minus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_sleep_hours(delta=0.5))
        self.sleep_meter.pack(padx=45,pady=20)
        self.add_sleep_button.place(relx=1, rely=0.5, anchor='e', x=-4)  # Place plus button at center right
        self.minus_sleep_button.place(relx=0, rely=0.5, anchor='w', x=4)
       
        self.sleep_label.pack()
        self.sleep_label2.pack(pady = 1)

        #Water Meter

        self.waterr_meter = Meter(self.waterr_frame, metersize=180, padding=0, amountused= self.water_consumed, amounttotal=10,
              labeltext='', textappend='', meterstyle='info.TLabel', stripethickness=0,image= './assets/images/water3.png',wedgecolor='#008DDA',appearance_mode= "Light")
        self.waterr_label = customtkinter.CTkLabel(self.waterr_frame,text=f"{self.water_consumed} of 10")
        self.waterr_label2 = customtkinter.CTkLabel(self.waterr_frame,text="Glasses consumed",text_color='#607274')
        self.add_water_button = customtkinter.CTkButton(self.waterr_frame,image=self.plus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_water_glass(delta=-1))
        self.minus_water_button = customtkinter.CTkButton(self.waterr_frame,image=self.minus_image,text ="",fg_color='transparent',width=20,command=lambda: self.adjust_water_glass(delta=1))
        self.waterr_meter.pack(padx=45,pady=20)
        self.add_water_button.place(relx=1, rely=0.5, anchor='e', x=-4)  # Place plus button at center right
        self.minus_water_button.place(relx=0, rely=0.5, anchor='w', x=4)
        self.waterr_label.pack()
        self.waterr_label2.pack(pady = 1)
            
        # create second frame
        self.second_frame = Progress(self)
        
        # create third frame
        self.third_frame = Progress(self)
        self.fourth_frame = Progress(self)

        #Meals Frame
        # self.new_meals_frame = Track_meals(self)
        # self.new_meals_frame = Progress(self)
        
        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        
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

        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

        # if name == "new_meals":
        #     self.new_meals_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.new_meals_frame.grid_forget()

    def home_button_event(self):
       
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        os.system('python Workout_page_changes.py')
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        os.system('python yoga.py')

        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    
    def adjust_water_glass(self, delta):
        if delta < 0:  
            self.waterr_meter.step(delta=-1)
            self.water_consumed += 1
        else: 
            self.waterr_meter.step(delta=1)
            self.water_consumed -= 1

        self.waterr_label.configure(text=f"{self.water_consumed} of 10")
        self.user_activity.update_attribute(username = self.user, date = parsed_date,value=self.water_consumed,
                                             attribute_name = 'water_drank' )

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
            self.sleep_meter.step(delta=1)
            self.hours_slept -= 1

        self.sleep_label2.configure(text=f"{self.hours_slept} of 7")
        self.user_activity.update_attribute(username = self.user, date = parsed_date,value=self.hours_slept,
                                             attribute_name = 'hours_slept' )
        
    def open_daily_meals(self):
        user_meal['username'] = current_user['username']
        # os.system('python track_meals.py')
        # self.destroy()
        track_meals_window = track_meals.Track_meals(self.handle_meal_submission)
        track_meals_window.mainloop()
        

        # self.select_frame_by_name("new_meals")
            
    def get_max_nutritional_contents(self):
        protein_percentage = 0.15  # 15%
        fiber_grams = 25  # grams
        fats_percentage = 0.25  # 25%
        carbs_percentage = 0.55

        calories = get_total_calories(self.user)

        protein_calories = calories * protein_percentage
        protein_grams = protein_calories / 4  # 1 gram of protein = 4 calories

        fats_calories = calories * fats_percentage
        fats_grams = fats_calories / 9  # 1 gram of fat = 9 calories

        carbs_calories = calories * carbs_percentage
        carbs_grams = carbs_calories / 4

        
        return {
            "protein_grams": protein_grams,
            "fiber_grams": fiber_grams,
            "fats_grams": fats_grams,
            "carbs_grams": carbs_grams
        }

    def handle_meal_submission(self):
       self.today_nutrition_values = get_nutrition_consumed(self.user,parsed_date)
       self.CaloriesUsed = round(self.today_nutrition_values["Total_Calories"])
       self.meter.update_values(self.CaloriesUsed)
       self.calorie_frame3_label1.configure(text=f"{self.CaloriesUsed} of {self.totalCalories}")
 
       self.protiens_consumed = self.today_nutrition_values["Total_Protein"]
       self.protiens_percent = self.protiens_consumed/self.protiens_target
       self.progress_bar1_label.configure(text=f"Protien: {self.protiens_consumed} of {self.protiens_target} g") 
       
       self.carbs_consumed = self.today_nutrition_values["Total_Carbohydrates"]
       self.carbs_percent = self.carbs_consumed/self.carbs_target
       self.progress_bar2_label.configure(text=f"Carbs: {self.carbs_consumed} of {self.carbs_target} g") 
        
       self.fats_consumed = self.today_nutrition_values["Total_Fats"]
       self.fats_percent = self.fats_consumed/self.fats_target
       self.progress_bar3_label.configure(text=f"Fats: {self.fats_consumed} of {self.fats_target} g") 

       self.fiber_consumed = self.today_nutrition_values["Total_Fiber"]
       self.fiber_percent = self.fiber_consumed/self.fiber_target
       self.progress_bar4_label.configure(text=f"Fiber: {self.fiber_consumed} of {self.fiber_target} g")

       self.progress_bar1.set(self.protiens_percent)
       self.progress_bar2.set(self.carbs_percent)
       self.progress_bar3.set(self.fats_percent)
       self.progress_bar4.set(self.fiber_percent)

       print("Callback Successful",self.CaloriesUsed)
    

        
        