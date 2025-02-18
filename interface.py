from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import psycopg

window = CTk()
window.geometry("856x645")
window.resizable(0,0)
window.title("School Library")

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=window, fg_color="#207244", width=330, height=645, corner_radius=10)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(anchor="nw", side="left")

sidebar_frame2 = CTkFrame(master=window, fg_color="#FFF", width=526, height=645, corner_radius=10,)
sidebar_frame2.pack_propagate(0)
sidebar_frame2.pack(fill="y", anchor="center")


#img_logo_data = Image.open("poopoo.jpeg")
#img_logo = CTkImage(dark_image=img_logo_data, light_image=img_logo_data, size=(330, 650))
#CTkLabel(master=sidebar_frame, text="", image=img_logo).pack(anchor="center")

def open_accounts():
    try: 
        subprocess.Popen(["python", "account.py"])
        window.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)
# Function to open login form
def call():
    window.destroy()  # Destroy the main window
    subprocess.Popen(["python", "index2.py"])  # Update with the correct path to index2.py

def call2():
    window.destroy()
    subprocess.Popen(["python", "/Users/beginner/Desktop/Advanced Arthur/Python-Advanced-main/index2.py"])  # Update with the correct path to index2.py

# Function to open registration form
def opensecondarywindow():
    window.destroy()
    subprocess.Popen(["python","index2.py"])
            

# Widgets for registration form
lbl_welcome =CTkLabel(master=sidebar_frame2, text="Are you a Student or Admin?", font=("Arial", 30))
lbl_welcome.pack(pady=50)

img_regist = Image.open("register.png")
btn_regist = CTkButton(sidebar_frame2, width=300,height=40,border_spacing= 10,text_color="Black", font=("Arial", 20), fg_color="#fff", border_width=3, border_color="#207244",hover_color="#268750", text="Student",corner_radius= 10,image=CTkImage(dark_image= img_regist), command=opensecondarywindow)
btn_regist.pack(pady=50)

img_regist2 = Image.open("register.png")
btn_regist2 = CTkButton(sidebar_frame2, width=300,height=40,border_spacing= 10,text_color="Black", font=("Arial", 20), fg_color="#fff", border_width=3, border_color="#207244",hover_color="#268750", text="Admin",corner_radius= 10,image=CTkImage(dark_image= img_regist))
btn_regist2.pack(pady=50)

# Centering buttons
btn_regist.pack(pady=(50, 10), anchor="center")
btn_regist2.pack(pady=(50, 10), anchor="center")



window.mainloop()