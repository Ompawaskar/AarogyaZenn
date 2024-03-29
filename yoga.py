import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import yogadata


from pygame import mixer

def update_label_text(text):
    label_text = ""
    if len(text) > 18:
        label_text = text[:18] + "..." # Truncate and add ellipsis
    else:
        label_text = text
    return label_text


def display_image_from_url(item,url, window, width=None, height=None):
    """Displays the image from the URL directly in the CustomTkinter window."""
  
        
    image = ctk.CTkImage(light_image=Image.open("./yimages/"+str(item['id'])+".png"),
                                  dark_image=Image.open("./yimages/"+str(item['id'])+".png"),
                                  size=(280,280))
     
    image_label = CTkButton(window, image=image,text="",corner_radius=15,hover=False,fg_color="#ffefd6",command=lambda item=item: seedetails(item),height=350,width=320)
        
    return image_label

def create_data_frame(item,row_index, column_index,no):
    frame = ctk.CTkFrame(master=f1,width=500,height=500,fg_color="transparent")
    frame.grid(row=row_index, column=column_index,padx =40,pady=20)

    image = display_image_from_url(item,no, frame, width=350, height=350)
    image.pack()
    ltext = update_label_text(item["sanskrit_name_adapted"])
    l2 = ctk.CTkLabel(master=image, text=ltext,font=("TkFixedFont", 22),text_color="#111111",bg_color="transparent")  
    l2.place(x= 25,y=280)
    l3 = ctk.CTkLabel(master=image, text=item["english_name"],font=("TkFixedFont", 19),text_color="#444444",bg_color="transparent")  
    l3.place(x= 30,y=310)


    return frame


def seedetails(item):
    mixer.init()

    def close():
        new_frame.place_forget()
        mixer.music.stop()

    new_frame = ctk.CTkScrollableFrame(master=root,width=1200,height=700,fg_color="#cec5f0")
    new_frame.place(x=0,y=0)
    new_frame.lift()
    filename = str(item["id"]) + ".mp3"
    path = os.getcwd()
    p = os.path.join(path,"audios",filename)

    imagef = ctk.CTkScrollableFrame(master=new_frame,width=350,height=700,fg_color="#cec5f9",scrollbar_button_color="#cec5f9",scrollbar_button_hover_color="#cec5f9")
    imagef.pack(side =RIGHT,pady = 20)
    image = display_image_from_url(item,item['url_png'], imagef, width=350, height=350)
    image.pack(side = TOP)
    buttonf = ctk.CTkFrame(master=imagef,width=350,height=100,fg_color="#cec5f9")
    buttonf.pack(pady = 20)
  
    mixer.music.load(p)
    def hear():
        mixer.music.play()
    
    
    sound = ctk.CTkImage(light_image=Image.open("./yimages/speaker.png"),
                                  dark_image=Image.open("./yimages/speaker.png"),
                                  size=(30,30))
    btn = CTkButton(master=buttonf, text="",image=sound, height=50,width=155,fg_color="#555555",hover=False,command=hear)
    btn.pack(side = LEFT,padx=2) 

  
    back = ctk.CTkImage(light_image=Image.open("./yimages/left.png"),
                                  dark_image=Image.open("./yimages/left.png"),
                                  size=(30,30))
    close_button = ctk.CTkButton(master=buttonf, text="",image=back,height=50,width=155,fg_color="#555555",hover=False,command=close)
    close_button.pack(side = RIGHT,padx=2)
    titlef = ctk.CTkScrollableFrame(master=new_frame,width=950,height=700,fg_color="#cec5f9",scrollbar_button_color="#cec5f9",scrollbar_button_hover_color="#cec5f9")
    titlef.pack(side =LEFT)
    titleframe1 = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    titleframe1.pack(padx =20,fill = "x",expand =True)
    name1 = ctk.CTkLabel(master = titleframe1,text=item["sanskrit_name_adapted"],font=("TkFixedFont", 60),bg_color="transparent")
    name1.pack(side =LEFT)
    titleframe2 = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    titleframe2.pack(padx =20,fill = "x",expand =True)
    name2 = ctk.CTkLabel(master = titleframe2,text="("+item["english_name"]+")",font=("TkFixedFont", 35),bg_color="transparent",text_color="#777777")
    name2.pack(side =LEFT)
    descframe = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    descframe.pack(padx =30,fill = "x",expand =True,pady =20)
    desc = ctk.CTkLabel(master = descframe,text="Instruction:",font=("TkFixedFont", 35),bg_color="transparent")
    desc.pack(side = LEFT)
    desccframe = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    desccframe.pack(padx =30,fill = "x",expand =True)
    descc = ctk.CTkLabel(master = desccframe,text=item["pose_description"],font=    ("TkFixedFont", 27),bg_color="transparent",width=950,wraplength=752,justify = "left",   text_color="#555555")
    descc.pack(pady = 20)
    benframe = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    benframe.pack(padx =30,fill = "x",expand =True)
    ben = ctk.CTkLabel(master = benframe,text="Benefits:",font=("TkFixedFont", 35), bg_color="transparent")
    ben.pack(side = LEFT)
    bennframe = CTkFrame(master=titlef,width=950,height=100,fg_color="#cec5f9")
    bennframe.pack(padx =30,fill = "x",expand =True)
    benn = ctk.CTkLabel(master = bennframe,text=item["pose_benefits"],font=("TkFixedFont",  27),bg_color="transparent",width=950,wraplength=752,justify = "left",text_color="#555555")
    benn.pack(pady = 20)

   
    
    

ctk.set_appearance_mode("Light") 

root = CTk()
root.geometry('1200x700')
root.title('Arogya Zenn')
root.configure(bg='#333333')

f1 = ctk.CTkScrollableFrame(master=root,width=1200,height=700,fg_color="#cec5f0")
f1.pack()

root.grid_columnconfigure(0, weight=1)  # Allow columns to expand equally
root.grid_rowconfigure(0, weight=1)

num_rows = (len(yogadata.data) // 4) + (len(yogadata.data) % 4 > 0)
row_counter = 0
column_counter = 0
no = 1
for item in yogadata.data:
   
    data_frame = create_data_frame(item, row_counter, column_counter,no)
    column_counter += 1
    if column_counter == 3:  # Reset column counter after 4 columns
        column_counter = 0
        row_counter += 1
    no = no + 1
    
   

root.mainloop()
