import customtkinter
from tkinter import PhotoImage
from PIL import ImageTk, Image
import os
import add_meals


class Track_meals(customtkinter.CTk):
    APP_NAME = "Track Meals"
    WIDTH =  400
    HEIGHT = 550

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(Track_meals.APP_NAME)
        self.geometry(str(Track_meals.WIDTH) + "x" + str(Track_meals.HEIGHT))
        self.minsize(Track_meals.WIDTH, Track_meals.HEIGHT)
        self.appearance_mode = "Light"

        #Images
        # Construct absolute path to the images directory
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/images")
        # self.recipe = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        # self.resized_image1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        # self.resized_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
         
        self.load_images()
       
        # Buttons Frame
        self.frame1 = customtkinter.CTkFrame(self)
        self.frame1.grid(row=0,column=0,pady=10)
        self.frame1.rowconfigure(0,weight=1)
        self.frame1.columnconfigure((0,1),weight=1)
       
        self.recipes = customtkinter.CTkButton(self.frame1,image=self.recipe,text="Recipes",fg_color='white',text_color='black',corner_radius=10,border_width=1)
        self.meals = customtkinter.CTkButton(self.frame1,image=self.resized_image1,text="Diet Plan",fg_color='white',text_color='black',corner_radius=10,border_width=1)

        self.recipes.grid(row=0,column = 0,padx=10)
        self.meals.grid(row=0,column = 1,padx=10)

        #Scrollable Frame
        self.add_meals_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="white",width=400,height=550)
        self.add_meals_frame.grid(row=1,column=0)
        self.add_meals_frame.columnconfigure( 0 , weight=1)
        self.add_meals_frame.rowconfigure( (0,1,2,3,4) , weight=1)
      
        #Breakfast Frame
        self.breakfast_frame = customtkinter.CTkFrame(self.add_meals_frame,fg_color="white")
        self.breakfast_frame.grid(row=0,column=0,sticky = 'ew')
        self.breakfast_frame.columnconfigure( 0 , weight=1)
        self.breakfast_frame.rowconfigure( (0,1) , weight=1)

        # Header Frame
        self.breakfast_label = customtkinter.CTkLabel(self.breakfast_frame,text="Breakfast")
        self.breakfast_label.grid(row=0,column = 0,sticky = 'w',padx = 10)

        self.breakfast_calories = customtkinter.CTkLabel(self.breakfast_frame,text="0 of 337 cals",text_color='#949494')
        self.breakfast_calories.grid(row=0,column=1)
        self.breakfast_button = customtkinter.CTkButton(self.breakfast_frame, image=self.resized_image, width=30, text="", fg_color='transparent', command=lambda: self.open_add_meals(meal='breakfast'))
        self.breakfast_button.grid(row=0,column = 2,padx = 5)

        #Meals Frame
        self.breakfast_meals_frame = customtkinter.CTkFrame(self.breakfast_frame)
        self.breakfast_meals_frame.grid(row=1,column=0,padx=20,pady=20,sticky = 'ew',columnspan = 3)

        self.breakfast_label1 = customtkinter.CTkLabel(self.breakfast_meals_frame,text="All you need is some breakfast!",text_color='#949494')
        self.breakfast_label1.pack(padx=20,pady=20)


        # Morning Snack Frame
        self.morning_snack_frame = customtkinter.CTkFrame(self.add_meals_frame,fg_color="white")
        self.morning_snack_frame.grid(row=1, column=0, sticky='ew', pady=10)  # Changed row to 2

        self.morning_snack_frame.columnconfigure(0, weight=1)
        self.morning_snack_frame.rowconfigure((0, 1), weight=1)

        # Header Frame
        self.morning_snack_label = customtkinter.CTkLabel(self.morning_snack_frame, text="Morning Snack",)  # Changed label text to "Morning Snack"
        self.morning_snack_label.grid(row=0, column=0, sticky='w', padx=10)

        self.morning_snack_calories = customtkinter.CTkLabel(self.morning_snack_frame, text="0 of 100 cals",text_color='#949494')  # Changed label text
        self.morning_snack_calories.grid(row=0, column=1)

        self.morning_snack_button = customtkinter.CTkButton(self.morning_snack_frame, image=self.resized_image, width=30, text="", fg_color='transparent')
        self.morning_snack_button.grid(row=0, column=2,padx = 5)

        # Meals Frame
        self.morning_snack_meals_frame = customtkinter.CTkFrame(self.morning_snack_frame, fg_color="#D3D3D3")
        self.morning_snack_meals_frame.grid(row=1, column=0, padx=20, pady=20, sticky='ew', columnspan=3)

        self.morning_snack_label1 = customtkinter.CTkLabel(self.morning_snack_meals_frame, text="Enjoy your morning snack!",text_color='#949494')  # Changed label text
        self.morning_snack_label1.pack(padx=20, pady=20)

        # Lunch Frame
        self.lunch_frame = customtkinter.CTkFrame(self.add_meals_frame,fg_color="white")
        self.lunch_frame.grid(row=2, column=0, sticky='ew', pady=10)  # Changed row to 1

        self.lunch_frame.columnconfigure(0, weight=1)
        self.lunch_frame.rowconfigure((0, 1), weight=1)

        # Header Frame
        self.lunch_label = customtkinter.CTkLabel(self.lunch_frame, text="Lunch")  # Changed label text to "Lunch"
        self.lunch_label.grid(row=0, column=0, sticky='w', padx=10)

        self.lunch_calories = customtkinter.CTkLabel(self.lunch_frame, text="0 of 337 cals",text_color='#949494')  # Changed label text
        self.lunch_calories.grid(row=0, column=1)

        self.lunch_button = customtkinter.CTkButton(self.lunch_frame, image=self.resized_image, width=30, text="", fg_color='transparent')
        self.lunch_button.grid(row=0, column=2,padx=5)

        # Meals Frame
        self.lunch_meals_frame = customtkinter.CTkFrame(self.lunch_frame)
        self.lunch_meals_frame.grid(row=1, column=0, padx=20, pady=20, sticky='ew', columnspan=3)

        self.lunch_label1 = customtkinter.CTkLabel(self.lunch_meals_frame, text="Enjoy your lunch!",text_color='#949494')  # Changed label text
        self.lunch_label1.pack(padx=20, pady=20)

        # Evening Snack Frame
        self.evening_snack_frame = customtkinter.CTkFrame(self.add_meals_frame, fg_color="white")
        self.evening_snack_frame.grid(row=3, column=0, sticky='ew', pady=10)  # Changed row to 3

        self.evening_snack_frame.columnconfigure(0, weight=1)
        self.evening_snack_frame.rowconfigure((0, 1), weight=1)

        # Header Frame
        self.evening_snack_label = customtkinter.CTkLabel(self.evening_snack_frame, text="Evening Snack")  # Changed label text to "Evening Snack"
        self.evening_snack_label.grid(row=0, column=0, sticky='w', padx=10)

        self.evening_snack_calories = customtkinter.CTkLabel(self.evening_snack_frame, text="0 of 150 cals",text_color='#949494')  # Changed label text
        self.evening_snack_calories.grid(row=0, column=1)

        self.evening_snack_button = customtkinter.CTkButton(self.evening_snack_frame, image=self.resized_image, width=30, text="", fg_color='transparent')
        self.evening_snack_button.grid(row=0, column=2,padx=5)

        # Meals Frame
        self.evening_snack_meals_frame = customtkinter.CTkFrame(self.evening_snack_frame)
        self.evening_snack_meals_frame.grid(row=1, column=0, padx=20, pady=20, sticky='ew', columnspan=3)

        self.evening_snack_label1 = customtkinter.CTkLabel(self.evening_snack_meals_frame, text="Enjoy your evening snack!",text_color='#949494')  # Changed label text
        self.evening_snack_label1.pack(padx=20, pady=20)

        # Dinner Frame
        self.dinner_frame = customtkinter.CTkFrame(self.add_meals_frame, fg_color="white")
        self.dinner_frame.grid(row=4, column=0, sticky='ew', pady=10)  # Changed row to 4

        self.dinner_frame.columnconfigure(0, weight=1)
        self.dinner_frame.rowconfigure((0, 1), weight=1)

        # Header Frame
        self.dinner_label = customtkinter.CTkLabel(self.dinner_frame, text="Dinner")  # Changed label text to "Dinner"
        self.dinner_label.grid(row=0, column=0, sticky='w', padx=10)

        self.dinner_calories = customtkinter.CTkLabel(self.dinner_frame, text="0 of 500 cals",text_color='#949494')  # Changed label text
        self.dinner_calories.grid(row=0, column=1)

        self.dinner_button = customtkinter.CTkButton(self.dinner_frame, image=self.resized_image, width=30, text="", fg_color='transparent')
        self.dinner_button.grid(row=0, column=2,padx=5)

        # Meals Frame
        self.dinner_meals_frame = customtkinter.CTkFrame(self.dinner_frame)
        self.dinner_meals_frame.grid(row=1, column=0, padx=20, pady=20, sticky='ew', columnspan=3)

        self.dinner_label1 = customtkinter.CTkLabel(self.dinner_meals_frame, text="Enjoy your dinner!",text_color='#949494')  # Changed label text
        self.dinner_label1.pack(padx=20, pady=20)

    def load_images(self):
        try:
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/images")
            self.recipe = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
            self.resized_image1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
            self.resized_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        except Exception as e:
            print("Error loading images:", e)

    def open_add_meals(self,meal):
        add_meals.add_meals(meals = meal).mainloop()


if __name__ == '__main__':
    Track_meals().mainloop()
