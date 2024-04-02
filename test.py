import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import bcrypt
import os


import fontawesome as fa
from datetime import datetime
from DBfuntions import add_user
import sys
from DBfuntions import add_info 
from DBfuntions import info_data_check
from DB import connection



# from Login import current_username

information = ctk.CTk()
information.title("Login Page")
information.geometry("1300x700")
loginbg = ctk.CTkImage(Image.open("image3.png"),
                       
                        size=(1300, 700))
bg_label = ctk.CTkLabel(information, text="", corner_radius=5, image=loginbg)
bg_label.place(x=0, y=0)
information.resizable(False, False)

def credentials_pass_to_db():
    username=name.get()
    user_gender=gender
    user_age=age.get()
    user_activity=activity_status
    user_height=height.get()
    user_weight=weight.get()
    user_tar_weight=tar_weight.get()
    user_goal=goal
    user_conditions=selected_conditions

    insert_data(username,user_gender,user_conditions,user_activity,user_age,user_goal,user_height,user_weight,user_tar_weight)
    information.destroy()          
    os.system('python Login.py')

    
def insert_data(username,user_gender,user_conditions,user_activity,user_age,user_goal,user_height,user_weight,user_tar_weight):
    user_information={
       "information":{
        "gender":user_gender,
        "age":user_age,
        "activity":user_activity,
        "height":user_height,
        "weight":user_weight,
        "tar_weight":user_tar_weight,
        "goal":user_goal,
        "conditions":user_conditions

       }  
    }
    result=info_data_check(user_information,username)
    if result=="yes":
            print("information all ready exsist for the username")
    else :
            add_info(user_information,username)
            
    
def current_u():
    return name.get()
def update_gender(value):
    global gender
    gender = value 
def update_activity_status(value):
    global activity_status
    activity_status = value       
   
def update_goal(value):
    global goal
    goal = value       

# def current_user(value):
#     global current_user
#     current_user = value     
   





#add_meal(meal_example)

# username=current_username()
# print(username)
tab = ctk.CTkTabview(information, width=800, height=1500, fg_color="#ffffff")
tab.place(x=550, y=-100)

tab_1 = tab.add("tab1")
tab_2 = tab.add("tab2")
tab_3 = tab.add("tab3")
tab_4 = tab.add("tab4")
tab_5 = tab.add("tab5")
tab_6 = tab.add("tab6")
tab_7 = tab.add("tab7")
tab_8 = tab.add("tab8")
tab_9 = tab.add("tab9")

def skip(tno):
  tabcall = "tab" + str(tno) 
  tab.set(tabcall)
def prev(tno):
  tabcall = "tab" + str(tno) 
  tab.set(tabcall)

# def calculate_bmi():
#     height_cm=float(height.get())
#     weight_kg=float(weight.get())
#     height_m = height_cm / 100  # Convert height from cm to meters
#     bmi = weight_kg / (height_m ** 2)  # Calculate BMI
#     return bmi


# def tab_1_db():
  



# Tab 1
# l1 = ctk.CTkLabel(tab_1, text="Hello there!", font=('Century Gothic', 40), text_color="black", bg_color="#ffffff")
# l1.place(x=500, y=405)
l2 = ctk.CTkLabel(tab_1, text="We're happy that you've taken the first step towards a healthier you.\n We need a few details to kickstart your journey", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l2.place(x=10, y=300)
l3 = ctk.CTkLabel(tab_1, text="What is your name!", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l3.place(x=200, y=400)
name = ctk.CTkEntry(tab_1,  border_color="#94a8fe", placeholder_text="Name", width=315, height=48, corner_radius=30, bg_color="#ffffff")
name.place(x=185, y=470)
nextbtn = ctk.CTkButton(tab_1,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(2))

nextbtn.place(x=600, y=700)

# nextbtn = ctk.CTkButton(tab_1,  border_color="#94a8fe", text="next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: (skip(3), credentials_pass_to_db()))


# nextbtn.place(x=450, y=700)

# Tab 2
l4 = ctk.CTkLabel(tab_2, text="What is your gender", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l4.place(x=225, y=300)
l5 = ctk.CTkLabel(tab_2, text="We support all forms of gender expression.\n However, we need this to calculate your body metrics", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l5.place(x=80, y=350)
chk_box1 = ctk.CTkRadioButton(tab_2, width=16, height=16, text="Male", 
                               font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                               value="Male", 
                               command=lambda: update_gender("Male"))
chk_box1.place(x=250, y=450)

chk_box2 = ctk.CTkRadioButton(tab_2, width=16, height=16, text="Female", 
                               font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                               value="Female", 
                               command=lambda: update_gender("Female"))
chk_box2.place(x=400, y=450)
nextbtn = ctk.CTkButton(tab_2,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(3))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_2,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(1))
prevbtn.place(x=450, y=700)


# Tab 3
l6 = ctk.CTkLabel(tab_3, text="What's your Age?", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l6.place(x=225, y=300)
l7 = ctk.CTkLabel(tab_3, text="Your age determines how much you should consume \n (Age in years)", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l7.place(x=80, y=350)
age = ctk.CTkEntry(tab_3,  border_color="#94a8fe", placeholder_text="Enter your age", width=150, height=48, corner_radius=30, bg_color="#ffffff")
age.place(x=275, y=425)
nextbtn = ctk.CTkButton(tab_3,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: (skip(4)))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_3,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(2))
prevbtn.place(x=450, y=700)

# Tab 4
l8 = ctk.CTkLabel(tab_4, text="How active are you?", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l8.place(x=225, y=300)
l9 = ctk.CTkLabel(tab_4, text="Based on your lifestyle, we can assess\n your daily calorie requirements", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l9.place(x=180, y=350)
# Create radiobuttons
chk_box1 = ctk.CTkRadioButton(tab_4, width=16, height=16, text="Little or No Activity", 
                                font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                               value="Little or No Activity", 
                               command=lambda: update_activity_status("Little or No Activity"))
chk_box1.place(x=250, y=485)

chk_box2 = ctk.CTkRadioButton(tab_4, width=16, height=16, text="Lightly Active", 
                                font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                                value="Lightly Active", 
                               command=lambda:(update_activity_status("Lightly Active")))
chk_box2.place(x=250, y=535)

chk_box3 = ctk.CTkRadioButton(tab_4, width=16, height=16, text="Moderately Active", 
                                font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                                value="Moderately Active", 
                               command=lambda: (update_activity_status("Moderately Active")))
chk_box3.place(x=250, y=585)

chk_box4 = ctk.CTkRadioButton(tab_4, width=16, height=16, text="Very Active", 
                                font=('Century Gothic', 20), text_color="black",
                               border_color="#94a8fe", corner_radius=30, bg_color="#ffffff", 
                                value="Very Active", 
                               command=lambda: (update_activity_status("Very Active")))
chk_box4.place(x=250, y=635)
nextbtn = ctk.CTkButton(tab_4,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(5))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_4,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(3))
prevbtn.place(x=450, y=700)

# Tab 5
l10 = ctk.CTkLabel(tab_5, text="How tall are you?", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l10.place(x=225, y=300)
l11 = ctk.CTkLabel(tab_5, text="Your height will help us calculate important body stats \n to help you reach your goal faster", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l11.place(x=100, y=350)
height = ctk.CTkEntry(tab_5,  border_color="#94a8fe", placeholder_text="Height in cm only", width=150, height=48, corner_radius=30, bg_color="#ffffff")
height.place(x=280, y=425)

height_u=height.get()

nextbtn = ctk.CTkButton(tab_5,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(6))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_5,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(4))
prevbtn.place(x=450, y=700)


# Tab 6
l12 = ctk.CTkLabel(tab_6, text="What's your current weight", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l12.place(x=225, y=300)
l13 = ctk.CTkLabel(tab_6, text="This will help us determine your goal, and monitor \n your progress over time", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l13.place(x=170, y=350)
weight = ctk.CTkEntry(tab_6,  border_color="#94a8fe", placeholder_text="Weight in kg's only", width=160, height=48, corner_radius=30, bg_color="#ffffff")
weight.place(x=340, y=425)
nextbtnbtn = ctk.CTkButton(tab_6,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(7))
nextbtnbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_6,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(5))
prevbtn.place(x=450, y=700)
weight_u=weight.get()
# Tab 7
l14 = ctk.CTkLabel(tab_7, text="What's your target weight", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l14.place(x=225, y=300)

l15 = ctk.CTkLabel(tab_7, text="Your current BMI is which is in the X range", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l15.place(x=205, y=350)
tar_weight = ctk.CTkEntry(tab_7,  border_color="#94a8fe", placeholder_text="Weight in kg's only", width=160, height=48, corner_radius=30, bg_color="#ffffff")
tar_weight.place(x=340, y=425)
nextbtn = ctk.CTkButton(tab_7,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(8))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_7,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(6))
prevbtn.place(x=450, y=700)

# Tab 8
l16 = ctk.CTkLabel(tab_8, text="What is your goal?", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l16.place(x=225, y=300)
l17= ctk.CTkLabel(tab_8, text="Based on your lifestyle, we can assess\n your daily calorie requirements", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l17.place(x=180, y=350)
chk_box = ctk.CTkCheckBox(tab_8, width=16, height=16, text="Gain Muscle", 
                              font=('Century Gothic', 20), text_color="black",
                              border_color="#94a8fe", 
                              corner_radius=30, bg_color="#ffffff",command=lambda: (update_goal("Gain Muscle")))
chk_box.place(x=250, y=485)
chk_box = ctk.CTkCheckBox(tab_8, width=16, height=16, text="Reduce Weight", 
                              font=('Century Gothic', 20),
                              text_color="black",
                              border_color="#94a8fe", 
                              corner_radius=30, bg_color="#ffffff",command=lambda: (update_goal("Reduce Weight")))
chk_box.place(x=250, y=535)
chk_box = ctk.CTkCheckBox(tab_8, width=16, height=16, text="Maintain Weight", 
                               border_width=1.5
                              ,font=('Century Gothic', 20),
                              border_color="#94a8fe", 
                              text_color="black",
                              corner_radius=30, bg_color="#ffffff",command=lambda: (update_goal("Maintain Weight")))
chk_box.place(x=250, y=585)

nextbtn = ctk.CTkButton(tab_8,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: skip(9))
nextbtn.place(x=600, y=700)
prevbtn = ctk.CTkButton(tab_8,  border_color="#94a8fe", text="Previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: prev(7))
prevbtn.place(x=450, y=700)

# Tab 9
l18 = ctk.CTkLabel(tab_9, text="Any Health issues?", font=('Century Gothic', 30), text_color="black", bg_color="#ffffff")
l18.place(x=225, y=300)
# l19= ctk.CTkLabel(tab_9, text="Based on your lifestyle, we can assess\n your daily calorie requirements", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
# l19.place(x=180, y=350)
selected_conditions = []

# Define a function to update the selected_conditions list
def update_selected_conditions(checkbox_text, variable):
    if variable.get():
        selected_conditions.append(checkbox_text)
    else:
        selected_conditions.remove(checkbox_text) if checkbox_text in selected_conditions else None

# Create the checkboxes
checkbox_texts = ["None", "Diabetes", "Cholestrol", "Hypertension", "PCOS", "Thyroid", "Excessive Stress", "Sleep Issues", "Depression"]
checkbox_positions = [
    (310, 450), (150, 500), (150, 550), (150, 600), (150, 650),
    (450, 500), (450, 550), (450, 600), (450, 650)
]

checkboxes = []
for i in range(len(checkbox_texts)):
    checkbox_text = checkbox_texts[i]  # Capture checkbox text here
    chk_box = ctk.CTkCheckBox(tab_9, width=16, height=16, text=checkbox_text, border_width=1.5,
                              border_color="#94a8fe", 
                              font=('Century Gothic', 20),
                              text_color="black",
                              corner_radius=30, bg_color="#ffffff")
    chk_box.place(x=checkbox_positions[i][0], y=checkbox_positions[i][1])
    var = tk.BooleanVar()
    chk_box.configure(variable=var)
    var.trace_add("write", lambda *_, text=checkbox_text, var=var: update_selected_conditions(text, var))  # Use checkbox_text here

    checkboxes.append(chk_box)
nextbtn = ctk.CTkButton(tab_9,  border_color="#94a8fe", text="Next", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: (credentials_pass_to_db()))
nextbtn.place(x=600, y=700) 
   
prevbtn = ctk.CTkButton(tab_9,  border_color="#94a8fe", text="previous", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: (prev(8)))
prevbtn.place(x=450, y=700) 

# Print the selected conditions array
print("Selected conditions:")



information.mainloop()


