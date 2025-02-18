from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import subprocess
import psycopg


app = CTk()
app.geometry("856x645")
app.resizable(0,0)
app.title("School Library")

set_appearance_mode("light") 

def open_dashboard():
    try:
        subprocess.Popen(["python", "Dashboard.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py", e)
        
def open_accounts():
    try: 
        subprocess.Popen(["python", "account.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)
        
            
def open_orders():
    app.destroy()
    try:
        subprocess.Popen(["python", "Orders.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_feedback():
    app.destroy()
    try:
        subprocess.Popen(["python", "feedback.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_settings():
    app.destroy()
    try:
        subprocess.Popen(["python", "settings_second.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
def open_returns():
    app.destroy()
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)
    
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#The logo for the app
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

#Analytics
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w", command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#Orders
#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(light_image=package_img_data)
#CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=open_orders).pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_returns).pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Account Signed in 
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
btn_accounts = CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w",command=open_accounts).pack(anchor="center", ipady=5, pady=(160, 0))

#Left Pannel
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

#The Title Frame
title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

CTkLabel(master=title_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")

CTkButton(master=title_frame, text="+ New Order",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", command= open_orders).pack(anchor="ne", side="right")

textframe= CTkFrame(master=main_view, fg_color="#dedcdc", width=680, height=550, border_color="#207244", border_width=3, corner_radius=5)
textframe.pack(anchor="s", fill="x", padx=27, pady=(29,0))

CTkLabel(master=textframe, text="The Orders Page allows customers to browse available products and", text_color="#207244",font=("Arial", 20)).pack(anchor="center", pady=20)
CTkLabel(master=textframe, text="place orders effortlessly. Users can select items, specify quantities", text_color="#207244",font=("Arial", 20)).pack(anchor="center")
CTkLabel(master=textframe, text=" and view the total cost before confirming their purchase.", text_color="#207244",font=("Arial", 20)).pack(anchor="center")
CTkLabel(master=textframe, text="A simple, intuitive interface ensures a smooth ordering process, with", text_color="#207244",font=("Arial", 20)).pack(anchor="center")
CTkLabel(master=textframe, text="options for delivery or pickup. Customers can track their order status", text_color="#207244",font=("Arial", 20)).pack(anchor="center")
CTkLabel(master=textframe, text="If you want to Create a new order then.", text_color="#207244",font=("Arial", 20)).pack(anchor="center")
CTkLabel(master=textframe, text="Create a new order with the button above", text_color="#207244",font=("Arial Bold", 25)).pack(anchor="center", pady=20)



app.mainloop()