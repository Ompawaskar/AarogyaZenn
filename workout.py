import customtkinter as ctk
from tkinter import messagebox, StringVar, OptionMenu
from List_of_bodypart_api import fetch_bodyParts  
from Exercises_api import fetch_exercises  

class WorkoutPage:
    def __init__(self, master):
        self.master = master

        self.worklabel = ctk.CTkLabel(master=master, text="Awesome Exercises You Should Know", text_color="blue", font=("roboto", 50))
        self.worklabel.pack()

        self.search_bar = ctk.CTkEntry(master=master, placeholder_text="Search Exercises", width=600, corner_radius=10)
        self.search_bar.pack(padx=50, pady=10)
        self.search_bar.bind("<Return>", self.search_exercise)

        self.body_parts = ["All"] + fetch_bodyParts() 
        self.selected_body_part = StringVar(master)
        self.selected_body_part.set("All")  

        
        self.body_part_menu = OptionMenu(master, self.selected_body_part, *self.body_parts, command=self.filter_by_body_part)
        self.body_part_menu.pack(pady=10)
        

        self.card_frame = ctk.CTkFrame(master=master)
        self.card_frame.pack(pady=10)

        self.all_exercises = fetch_exercises()

        self.current_index = 0 
        self.filtered_exercises = self.all_exercises 
        self.display_exercises(self.filtered_exercises, num_to_display=10)  

    def display_exercises(self, exercises, num_to_display=10):
        for widget in self.card_frame.winfo_children():
            widget.destroy()

        if exercises:
            for index in range(self.current_index, min(len(exercises), self.current_index + num_to_display)):
                exercise = exercises[index]
                exercise_frame = ctk.CTkFrame(master=self.card_frame)
                exercise_frame.pack(pady=10)

                exercise_label = ctk.CTkLabel(master=exercise_frame, text=exercise.get('name'), font=("roboto", 14), cursor="hand2")
                exercise_label.pack()

                def show_exercise_details():
                    detailed_info = f"Exercise Name: {exercise.get('name')}\n" \
                                    f"GIF URL: {exercise.get('gifUrl')}\n" \
                                    f"Body Part: {exercise.get('bodyPart')}\n" \
                                    f"Equipment: {exercise.get('equipment')}\n" \
                                    f"Target: {exercise.get('target')}\n" \
                                    f"Secondary Muscles: {', '.join(exercise.get('secondaryMuscles'))}\n" \
                                    f"Instructions:\n" \
                                    f"{'; '.join(exercise.get('instructions'))}"
                    messagebox.showinfo("Exercise Details", detailed_info)

                exercise_label.bind("<Button-1>", lambda event, func=show_exercise_details: func())

            if self.current_index > 0:
                prev_button = ctk.CTkButton(master=self.card_frame, text="Previous", command=self.prev_page)
                prev_button.pack(side="left", padx=10, pady=10)

            if self.current_index + num_to_display < len(exercises):
                next_button = ctk.CTkButton(master=self.card_frame, text="Next", command=self.next_page)
                next_button.pack(side="right", padx=10, pady=10)

    def next_page(self):
        self.current_index += 10  
        self.display_exercises(self.filtered_exercises)

    def prev_page(self):
        self.current_index -= 10 
        self.display_exercises(self.filtered_exercises)

    def filter_by_body_part(self, selected_part):
        if selected_part == "All":
            self.filtered_exercises = self.all_exercises
        else:
            self.filtered_exercises = [exercise for exercise in self.all_exercises if exercise["bodyPart"].lower() == selected_part.lower()]
        self.display_exercises(self.filtered_exercises)

    def search_exercise(self, event):
        keyword = self.search_bar.get().lower()

        matching_exercises = [exercise for exercise in self.all_exercises if keyword in exercise["name"].lower()]
        self.display_exercises(matching_exercises)

    def hide(self):
        self.worklabel.pack_forget()
        self.search_bar.pack_forget()
        self.card_frame.pack_forget()
        self.body_part_menu.pack_forget()

    def show(self):
        self.worklabel.pack()
        self.search_bar.pack(pady=10)
        self.body_part_menu.pack(pady=10)
        self.card_frame.pack(pady=10)

        # Toggle the visibility of the WorkoutPage when shown
        self.master.geometry('800x600')
        self.master.title('Workout Page')

def main():
    root = ctk.CTk()
    workout_page = WorkoutPage(root)
    workout_page.show()
    root.mainloop()

if __name__ == "__main__":
    main()
