import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io


class CustomWorkoutPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Custom Workout")
        self.configure(bg="#E0E0E0")

        self.exercises_added_label = tk.Label(self, text="Exercises Added:", bg="#E0E0E0", fg="#333333", font=("Helvetica", 12))
        self.exercises_added_label.pack(pady=10)

        self.exercises_frame = tk.Frame(self, bg="#E0E0E0")
        self.exercises_frame.pack(pady=5)

        self.exercise_vars = {} 
        self.exercise_widgets = {} 
        self.scrollbar = tk.Scrollbar(self.exercises_frame, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        self.exercises_listbox = tk.Listbox(self.exercises_frame, width=50, height=10, yscrollcommand=self.scrollbar.set)
        self.exercises_listbox.pack(side=tk.LEFT, padx=5)

        self.scrollbar.config(command=self.exercises_listbox.yview)

        self.remove_button = tk.Button(self, text="Remove Selected", command=self.remove_selected_exercises)
        self.remove_button.pack(pady=5)

        
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_exercises_list(self, exercises):
       
        for exercise in exercises:
            if exercise['name'] in self.exercise_widgets:
                label = self.exercise_widgets[exercise['name']]['label']
                label.config(text=exercise['name'])

                var = self.exercise_vars[exercise['name']]
                if var.get() == 1:  
                    var.set(1) 

            else:
                
                exercise_frame = tk.Frame(self.exercises_listbox, bg="#E0E0E0")
                exercise_frame.pack(fill="x", padx=5, pady=2)
                var = tk.IntVar(value=0) 
                self.exercise_vars[exercise['name']] = var

                checkbox = tk.Checkbutton(exercise_frame, variable=var, bg="#E0E0E0")
                checkbox.pack(side=tk.LEFT)

                label = tk.Label(exercise_frame, text=exercise['name'], bg="#E0E0E0")
                label.pack(side=tk.LEFT)

               
                label.bind("<Button-1>", lambda event, ex=exercise: self.show_exercise_details(ex))

                self.exercise_widgets[exercise['name']] = {'frame': exercise_frame, 'label': label}

    def remove_selected_exercises(self):
        selected_exercises = [name for name, var in self.exercise_vars.items() if var.get() == 1]
        for name in selected_exercises:
            frame = self.exercise_widgets[name]['frame']
            frame.destroy()  
            del self.exercise_widgets[name] 
            del self.exercise_vars[name]  
    def show_exercise_details(self, exercise):
       
        exercise_window = tk.Toplevel(self)
        exercise_window.title("Exercise Details")
        exercise_window.configure(bg="#E0E0E0")

       
        detailed_info = f"Exercise Name: {exercise.get('name')}\n" \
                        f"Body Part: {exercise.get('bodyPart')}\n" \
                        f"Equipment: {exercise.get('equipment')}\n" \
                        f"Target: {exercise.get('target')}\n" \
                        f"Secondary Muscles: {', '.join(exercise.get('secondaryMuscles'))}\n" \
                        f"Instructions:\n" \
                        f"{'; '.join(exercise.get('instructions'))}"

       
        details_label = tk.Label(exercise_window, text=detailed_info, bg="#E0E0E0", fg="#333333", font=("Helvetica", 12), wraplength=400)
        details_label.pack(pady=10, padx=10)

        
        gif_url = exercise.get('gifUrl')
        if gif_url:
            response = requests.get(gif_url)
            if response.status_code == 200:
               
                img_data = response.content
                img = Image.open(io.BytesIO(img_data))

                
                gif_label = tk.Label(exercise_window, bg="#E0E0E0")
                gif_label.pack(pady=10)

              
                def update_gif(frame_num=0):
                    frame = img.seek(frame_num)
                    frame = img.copy().convert('RGBA')
                    photo = ImageTk.PhotoImage(frame)
                    gif_label.config(image=photo)
                    gif_label.image = photo  
                    exercise_window.after(200, update_gif, (frame_num + 1) % img.n_frames)

                
                update_gif()
            else:
              
                messagebox.showerror("Error", "Failed to fetch GIF image.")
        else:
           
            messagebox.showinfo("Info", "No GIF image available for this exercise.")

    def clear_exercises(self):
        for frame in self.exercise_widgets.values():
            frame['frame'].destroy()
        self.exercise_widgets.clear()
        self.exercise_vars.clear()

    def close_window(self):
        self.clear_exercises()
        self.withdraw()

def open_custom_workout_page():
    global custom_workout_page
    
    if custom_workout_page is None or not custom_workout_page.winfo_exists() or not custom_workout_page.winfo_ismapped():
        custom_workout_page = CustomWorkoutPage(window)
        exercises = fetch_exercises()
        custom_workout_page.update_exercises_list(exercises)
    else:
        custom_workout_page.deiconify() 

def fetch_exercises(exercise_id=None):
    url = "https://exercisedb.p.rapidapi.com/exercises"
    querystring = {"limit": "1324"}  
    if exercise_id:
        querystring["id"] = exercise_id
    headers = {
        "X-RapidAPI-Key": "e1388555aamsh715a82d5d0acf9ap12e4d8jsna244a61e64aa",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()