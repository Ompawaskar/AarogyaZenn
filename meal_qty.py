import customtkinter
import tkinter as tk
from PIL import Image,ImageTk
import os
import globalStore
import add_meals
import home
from Nutrition.Nutritionapi_connection import nutritional_info
from Database.meals_functions import add_meal
from datetime import datetime

today_date = datetime.today()

# Format today's date as a string in "YYYY-MM-DD" format
today_date_string = today_date.strftime("%Y-%m-%d")

# Parse the formatted date string back to a datetime object
parsed_date = datetime.strptime(today_date_string, "%Y-%m-%d")

class add_meals2(customtkinter.CTk):
    APP_NAME = "Add Meals"
    WIDTH =  400
    HEIGHT = 550
   
    def __init__(self,nutrition_info, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_images()
        self.title(add_meals2.APP_NAME)
        self.geometry(str(add_meals2.WIDTH) + "x" + str(add_meals2.HEIGHT))
        self.minsize(add_meals2.WIDTH, add_meals2.HEIGHT)
        self.config(bg='white')

        self.nutritional_info = nutrition_info
        self.food_units_info = nutrition_info['foods'][0]["alt_measures"]
        self.food_units = self.get_units(self.food_units_info)


        self.top_frame = customtkinter.CTkFrame(self,height=20)
        self.top_frame.pack()

        # self.protien_image = None
        # self.carbs_image = None
        # self.fats_image = None
        # self.fiber_image = None
        # self.main_image= None
        # photo = None
        
        self.top_label = customtkinter.CTkLabel(self.top_frame,image=self.photo,text="")
        self.top_label.pack(fill="both")
        
        self.text_label = customtkinter.CTkLabel(self.top_frame, text=globalStore.user_meal['meal_name'], font=("Your Font", 20),bg_color= 'transparent',fg_color='transparent')
        self.text_label.place(relx=0.5, rely=0.5, anchor="center")

        self.mid_frame = customtkinter.CTkFrame(self,fg_color='white')
        self.mid_frame.pack(fill='x',padx=10,pady=10)
        self.mid_frame.columnconfigure((0,1),weight=1)
        self.mid_frame.rowconfigure(0,weight=1)
 
        self.quantity = customtkinter.CTkEntry(self.mid_frame,placeholder_text="Enter Quantity")
        self.units = customtkinter.CTkComboBox(self.mid_frame,values=self.food_units)

        self.quantity.grid(row=0,column=0,padx=5,pady=20)
        self.units.grid(row=0,column=1,padx=5,pady=20)

        # Bind events
        self.units.bind('<<ComboboxSelected>>', self.on_select)
        self.quantity.bind('<KeyRelease>', self.on_key_release)

        self.bottom_frame = customtkinter.CTkFrame(self,fg_color='white')
        self.bottom_frame.pack(fill='x',padx=10,pady=15)
        self.bottom_frame.columnconfigure((0,1,2,3),weight=1)
        self.bottom_frame.rowconfigure((0,1,2),weight=1)
       
        self.macro_label = customtkinter.CTkLabel(self.bottom_frame,text="Macronutrients Breakdown")
        self.macro_label.grid(row=0,column=0,sticky = "w",padx = 8,pady=8,columnspan = 4)

        self.protien_frame = customtkinter.CTkFrame(self.bottom_frame,fg_color='white')
        self.protien_frame.grid(row=1,column=0)
        self.carbs_frame = customtkinter.CTkFrame(self.bottom_frame,fg_color='white')
        self.carbs_frame.grid(row=1,column=1)
        self.fats_frame = customtkinter.CTkFrame(self.bottom_frame,fg_color='white')
        self.fats_frame.grid(row=1,column=2)
        self.fiber_frame = customtkinter.CTkFrame(self.bottom_frame,fg_color='white')
        self.fiber_frame.grid(row=1,column=3)

        self.protien_label = customtkinter.CTkLabel(self.protien_frame,text="Protien")
        self.protien_label.pack()
        self.button_protien = customtkinter.CTkButton(self.protien_frame,text="",image=self.protien_image,width=15,fg_color='white')
        self.button_protien.pack(pady=5,padx=5)
        self.protien_qty = customtkinter.CTkLabel(self.protien_frame,text= f"{globalStore.user_meal['protein']}g")
        self.protien_qty.pack()
       
        self.carbs_label = customtkinter.CTkLabel(self.carbs_frame,text="Carbs")
        self.carbs_label.pack()
        self.button_carbs = customtkinter.CTkButton(self.carbs_frame,text="",image=self.carbs_image,width=15,fg_color='white')
        self.button_carbs.pack(pady=5,padx=5)
        self.carbs_qty = customtkinter.CTkLabel(self.carbs_frame,text= f"{globalStore.user_meal['carbs']}g")
        self.carbs_qty.pack()

        self.fats_label = customtkinter.CTkLabel(self.fats_frame,text="Fats")
        self.fats_label.pack()
        self.button_fats = customtkinter.CTkButton(self.fats_frame,text="",image=self.fats_image,width=15,fg_color='white')
        self.button_fats.pack(pady=5,padx=5)
        self.fats_qty = customtkinter.CTkLabel(self.fats_frame,text= f"{globalStore.user_meal['fats']}g")
        self.fats_qty.pack()

        self.fiber_label = customtkinter.CTkLabel(self.fiber_frame,text="Fiber")
        self.fiber_label.pack()
        self.button_fiber = customtkinter.CTkButton(self.fiber_frame,text="",image=self.fiber_image,width=15,fg_color='white')
        self.button_fiber.pack(pady=5,padx=5)
        self.fiber_qty = customtkinter.CTkLabel(self.fiber_frame,text= f"{globalStore.user_meal['fiber']}g")
        self.fiber_qty.pack()

        self.submit_button = customtkinter.CTkButton(self.bottom_frame,fg_color='orange',text="Add Food",text_color='white',command=self.submit_meal)
        self.submit_button.grid(row=2,column=0,columnspan = 4,pady=10,sticky = 'sew')

    def on_key_release(self, event):
        if event.keysym == "Return":  # Check if Enter key is pressed
            search_term = self.quantity.get()
            selected_unit = self.units.get()
            self.set_nutritional_contents(search_term,selected_unit)
            self.reset_labels()

    def on_select(self, event):
        search_term = self.quantity.get()
        selected_unit = self.units.get()
        self.set_nutritional_contents(search_term,selected_unit)
        self.reset_labels()
    
    def get_units(self,arr):
        units_arr = []
        for each in arr:
            units_arr.append(each['measure'])
        return units_arr
    
    def set_nutritional_contents(self,quantity,unit):
        serving_wt = 0
        quantity_int = float(quantity)
        unit_qty = 1

        for each in self.food_units_info:
            if each['measure'] == unit:
                serving_wt = each['serving_weight']
                unit_qty = each['qty']

        orignal_wt = self.nutritional_info['foods'][0]["serving_weight_grams"]
        factor_value = (quantity_int*serving_wt)/(orignal_wt*unit_qty)
        factor = round(factor_value,2)
        calories = round(factor * self.nutritional_info['foods'][0]['nf_calories'], 2)
        protein = round(factor * self.nutritional_info['foods'][0]['nf_protein'], 2)
        carbs = round(factor * self.nutritional_info['foods'][0]['nf_total_carbohydrate'], 2)
        fats = round(factor * self.nutritional_info['foods'][0]['nf_total_fat'], 2)
        fiber = round(factor * self.nutritional_info['foods'][0]['nf_dietary_fiber'], 2)
        
        globalStore.user_meal['Total_Calories'] = calories
        globalStore.user_meal['protein'] = protein
        globalStore.user_meal['carbohydrates'] = carbs
        globalStore.user_meal['fats'] = fats
        globalStore.user_meal['fiber'] = fiber

    def reset_labels(self):
        self.protien_qty.configure(text= f"{globalStore.user_meal['protein']}g") 
        self.carbs_qty.configure(text= f"{globalStore.user_meal['carbs']}g") 
        self.fats_qty.configure(text= f"{globalStore.user_meal['fats']}g") 
        self.fiber_qty.configure(text= f"{globalStore.user_meal['fiber']}g") 

    def load_images(self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/images")
        self.protien_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "protien.png")))
        self.carbs_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "carbs.png")))
        self.fats_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fats.png")))
        self.fiber_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fibre.png")))
        # self.main_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "food1.png")))
        self.image2 = Image.open("./assets/images/food1.png")
        self.photo = ImageTk.PhotoImage(self.image2)
   
    def submit_meal(self):
        quantity = self.quantity.get()
        quantity_float = float(quantity)
        unit = self.units.get()
        globalStore.user_meal['quantity'] = quantity_float
        globalStore.user_meal['unit'] = unit
        globalStore.user_meal['date'] = parsed_date
        # print(globalStore.user_meal)
        add_meal(globalStore.user_meal)
        self.destroy()
        home.Dashboard().mainloop()
        
        
if __name__ == '__main__':
    app = add_meals2()
    app.mainloop().attributes('-transparentcolor', 'white')
    


        