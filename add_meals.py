import tkinter as tk
from PIL import Image
import customtkinter
import meal_qty
from globalStore import user_meal
from Nutrition.AutoComplete import auto_complete
from Nutrition.Nutritionapi_connection import nutritional_info

class add_meals(customtkinter.CTk):
    APP_NAME = "Track Meals"
    WIDTH =  400
    HEIGHT = 550

    def __init__(self,callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback
        self.title(add_meals.APP_NAME)
        self.geometry(str(add_meals.WIDTH) + "x" + str(add_meals.HEIGHT))
        self.minsize(add_meals.WIDTH, add_meals.HEIGHT)
        self.config(bg='white')
        
        # Create input frame
        self.input_frame = customtkinter.CTkFrame(self, bg_color='white', fg_color='white')
        self.input_frame.grid(row=0, column=0, padx=0, pady=10, sticky='ew')
        self.input_frame.columnconfigure((0, 1), weight=1)
        self.input_frame.rowconfigure(0, weight=1)
        
        # Create input field inside input frame
        self.input_field = customtkinter.CTkEntry(self.input_frame, placeholder_text="Search Food Name")
        self.input_field.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.resized_image = customtkinter.CTkImage(Image.open("./assets/images/orange_plus_image.png"))
        self.add_button = customtkinter.CTkButton(self.input_frame, text="Add item", fg_color='orange', command=self.open_meal_qty, width=20)
        self.add_button.grid(row=0, column=1)
        
        # Create autocomplete listbox
        self.autocomplete_listbox = tk.Listbox(self.input_frame, height=40, width=34, activestyle='dotbox', font="Helvetica", selectbackground='orange')
        self.autocomplete_listbox.grid(row=1, column=0, padx=0, pady=10, columnspan=2, sticky='nsew')
        font_size = 15
        font_style = "Arial"
        self.autocomplete_listbox.configure(font=(font_style, font_size))
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(self.input_frame, orient=tk.VERTICAL, command=self.autocomplete_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.autocomplete_listbox.config(yscrollcommand=scrollbar.set)
        
        # Sample data
        self.data = ["apple", "banana", "orange", "pineapple", "grape", "kiwi", "mango"]
        
        # Bind events
        self.autocomplete_listbox.bind('<<ListboxSelect>>', self.on_select)
        self.input_field.bind('<KeyRelease>', self.on_key_release)
    
    def on_key_release(self, event):
        if event.keysym == "Return" or event.keysym == "space":
            search_term = self.input_field.get()
            autocomplete_list = auto_complete(search_term)
            self.update_autocomplete_list(autocomplete_list)
    
    def on_select(self, event):
        index = self.autocomplete_listbox.curselection()
        if index:
            selected_item = self.autocomplete_listbox.get(index)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, selected_item)
    
    def update_autocomplete_list(self, items):
        self.autocomplete_listbox.delete(0, tk.END)
        for item in items:
            self.autocomplete_listbox.insert(tk.END, item)
    
    def open_meal_qty(self):
        meal_name = self.input_field.get()
        user_meal['meal_name'] = meal_name
        nutritional_json = nutritional_info(meal_name)
        self.destroy()
        self.meal_qty_window = meal_qty.add_meals2(nutrition_info=nutritional_json, callback=self.callback)
        self.meal_qty_window.mainloop()

if __name__ == '__main__':
    add_meals(callback=None).mainloop()
