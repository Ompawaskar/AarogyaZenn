import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io
import custom_wkt
import threading
import urllib3

def run_workout_page():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    custom_workout_page = None 


    from concurrent.futures import ThreadPoolExecutor

    executor = ThreadPoolExecutor(max_workers=10)

    class ExerciseImageLoader:
        def __init__(self):
            self.image_cache = {}

        def load_image(self, url, callback):
            if url in self.image_cache:
           
                callback(self.image_cache[url])
            else:
           
                future = executor.submit(self._fetch_image, url, callback)

        def _fetch_image(self, url, callback):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    img_data = response.content
                    img = Image.open(io.BytesIO(img_data))
                    photo = ImageTk.PhotoImage(img)
                    self.image_cache[url] = photo
                    callback(photo)
                else:
                    print(f"Failed to fetch image from {url}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error fetching image from {url}: {e}")
    def search():
        query = search_entry.get().lower() 
        body_part = body_part_var.get()
        target = target_var.get()
        secondary_muscle = secondary_muscle_var.get()
        equipment = equipment_var.get()

    # Filter exercises based on search query and selected options
        filtered_exercises = [exercise for exercise in exercises if
                          (query in exercise['name'].lower()) and
                          (body_part == "All" or body_part.lower() == exercise['bodyPart'].lower()) and
                          (target == "All" or target.lower() == exercise['target'].lower()) and
                          (secondary_muscle == "All" or secondary_muscle.lower() in map(str.lower, exercise['secondaryMuscles'])) and
                          (equipment == "All" or equipment.lower() == exercise['equipment'].lower())]

        display_exercises(filtered_exercises)  

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

    def on_configure(event):
   
        canvas.configure(scrollregion=canvas.bbox("all"))

    def show_exercise_details(exercise):
    
        exercise_window = tk.Toplevel(window)
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

    # Load GIF image
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
    def display_exercises(exercises_to_display):
        loader = ExerciseImageLoader()  
    
        for widget in inner_frame.winfo_children():
            widget.destroy()

    
        for i, exercise in enumerate(exercises_to_display):
            label_references = [] 
            card_frame = tk.Frame(inner_frame, bg="black", width=200, height=100, padx=10, pady=10)
            card_frame.grid(row=i // num_columns, column=i % num_columns, padx=10, pady=10)
            label = tk.Label(card_frame, text=exercise["name"], bg="black", fg="white")
            label.pack()

       
            label.bind("<Button-1>", lambda event, ex=exercise: show_exercise_details(ex))
         
        
            select_button = tk.Button(card_frame, text="Add to Workout", command=lambda ex=exercise: add_to_custom_workout(ex))
            select_button.pack()

        
            gif_url = exercise.get('gifUrl')
            if gif_url:
                gif_label = tk.Label(card_frame, bg="#E0E0E0")
                gif_label.pack(pady=5)

            
                loader.load_image(gif_url, lambda img, gl=gif_label: gl.config(image=img))
          
           
                label_references.append(gif_label)
            else:
                messagebox.showinfo("Info", "No GIF image available for this exercise.")
        
        
            label_references.append(gif_label)

    def add_to_custom_workout(exercise):
        global custom_workout_page  
    
        if custom_workout_page is None:
            custom_workout_page = custom_wkt.CustomWorkoutPage(window)

        custom_workout_page.update_exercises_list([exercise])
        messagebox.showinfo("Added", "Exercise added to Custom Workout.")


    window = tk.Tk()
    window.title("Workout")
    window.configure(bg="black") 


    exercises = fetch_exercises()


    search_frame = tk.Frame(window, pady=20, bg="black")
    search_frame.pack(fill="x")


    search_label = tk.Label(search_frame, text="Search:", bg="black", fg="white") 
    search_label.pack(side=tk.LEFT)


    search_entry = tk.Entry(search_frame, width=50, bg="black", fg="white") 
    search_entry.pack(side=tk.LEFT, padx=5)


    body_part_var = tk.StringVar(window)
    body_part_var.set("All")
    body_part_menu = tk.OptionMenu(search_frame, body_part_var, "All", *sorted(set(exercise['bodyPart'] for exercise in exercises)))
    body_part_menu.config(bg="black", fg="white") 
    body_part_menu.pack(side=tk.LEFT, padx=5)


    target_var = tk.StringVar(window)
    target_var.set("All")
    target_menu = tk.OptionMenu(search_frame, target_var, "All", *sorted(set(exercise['target'] for exercise in exercises)))
    target_menu.config(bg="black", fg="white")  
    target_menu.pack(side=tk.LEFT, padx=5)


    secondary_muscle_var = tk.StringVar(window)
    secondary_muscle_var.set("All")
    secondary_muscle_menu = tk.OptionMenu(search_frame, secondary_muscle_var, "All", *sorted(set(muscle for exercise in exercises for muscle in exercise['secondaryMuscles'])))
    secondary_muscle_menu.config(bg="black", fg="white") 
    secondary_muscle_menu.pack(side=tk.LEFT, padx=5)


    equipment_var = tk.StringVar(window)
    equipment_var.set("All")
    equipment_menu = tk.OptionMenu(search_frame, equipment_var, "All", *sorted(set(exercise['equipment'] for exercise in exercises)))
    equipment_menu.config(bg="black", fg="white")  
    equipment_menu.pack(side=tk.LEFT, padx=5)


    search_button = tk.Button(search_frame, text="Search", command=search, bg="black", fg="white")
    search_button.pack(side=tk.LEFT)

    custom_workout_label = tk.Label(search_frame, text="Custom Workout", bg="black", fg="white")
    custom_workout_label.pack(side=tk.LEFT, padx=5)

    custom_workout_label.bind("<Button-1>", lambda event: open_custom_workout_page())


    def open_custom_workout_page():
        global custom_workout_page 

   
        from custom_wkt import CustomWorkoutPage

    
        if custom_workout_page is None:
            custom_workout_page = CustomWorkoutPage(window)






    canvas = tk.Canvas(window, bg="black")
    canvas.pack(side=tk.LEFT, fill="both", expand=True)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)


    inner_frame = tk.Frame(canvas, bg="black")
    inner_frame.bind("<Configure>", on_configure)  

    canvas.create_window((0, 0), window=inner_frame, anchor="nw")


    num_exercises = len(exercises)
    num_columns = 5 
    num_rows = -(-num_exercises // num_columns)  


    display_exercises(exercises)


    window.mainloop()
