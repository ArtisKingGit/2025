from customtkinter import *
import tkinter
from PIL import Image
import subprocess
from CTkTable import *
import psycopg
from tkinter import messagebox

def open_accounts():
    try:
        subprocess.Popen(["python", "account.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)

# Connect to database and fetch data
def fetch_orders_data():
    try:
        conn = psycopg.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute('SELECT order_name, customer_name, address_name, quantity FROM orders_')
        orders_data = cur.fetchall()
        return [["Order Name", "Customer Name", "Address", "Quantity"]] + [list(row) for row in orders_data]
    except (psycopg.DatabaseError, psycopg.Error) as e:
        messagebox.showerror("Error", f"Database error: {e}")
        return []
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# GUI setup
app = CTk()
app.geometry("856x645")
app.resizable(0, 0)
set_appearance_mode("light")

# Functions to open other scripts
def open_feedback():
    app.destroy()
    try:
        subprocess.Popen(["python", "feedback.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing feedback.py:", e)

def open_settings():
    app.destroy()
    try:
        subprocess.Popen(["python", "settings.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing settings.py:", e)

def open_returns():
    app.destroy()
    try:
        subprocess.Popen(["python", "returns.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing returns.py:", e)

def open_dashboard():
    app.destroy()
    try:
        subprocess.Popen(["python", "Dashboard_user.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

# Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Logo Image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

# Buttons in Sidebar
buttons = [
    ("Dashboard", "analytics_icon.png", open_dashboard),
    ("Feedback", "feedback_icon.png", open_feedback),
    ("Returns", "returns_icon.png", open_returns),
    ("Settings", "settings_icon.png", open_settings),
    ("Account", "person_icon.png", open_accounts),
]

for text, img_name, command in buttons:
    img_data = Image.open(img_name)
    img = CTkImage(dark_image=img_data, light_image=img_data)
    CTkButton(master=sidebar_frame, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14), 
               hover_color="#207244", anchor="w", command=command).pack(anchor="center", ipady=5, pady=(16, 0))

# Main View
main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master=main_view, text="""Thank you for Confirming your order!
         Or Feedback""", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=27)
CTkLabel(master=main_view, text="Submit your feedback if needed to.", font=("Arial Black", 20), text_color="#2A8C55").pack(anchor="nw", pady=(30, 0), padx=27)

app.mainloop()
