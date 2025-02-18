from customtkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess
import psycopg

# Create the main login window
Login_Form = CTk()
Login_Form.title("School Library Login")
Login_Form.geometry("856x645")
set_appearance_mode("light")
# Function to call Dashboard.py and destroy the login window
def open_accounts():
    try: 
        subprocess.Popen(["python", "account.py"])
        Login_Form.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing account.py", e)
        
def call():
    Login_Form.destroy()
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

def call2():
    Login_Form.destroy()
    try:
        subprocess.Popen(["python", "index.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing index.py:", e)

# Function to handle login attempt
def login_attempt(username, password):
    try:
        conn = psycopg.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
        cur = conn.cursor()
        
        # Execute the query to fetch user with given username and password
        cur.execute('SELECT * FROM admin_ WHERE username = %s AND pass = %s', (username, password))
        
        # Fetch the first row (if exists)
        user = cur.fetchone()
        
        if user:
            messagebox.showinfo("Success", "Successfully logged in!")
            cur.close()
            conn.close()
            
            # Call the function to open Dashboard.py and destroy current window
            call()
        else:
            messagebox.showerror("Error", "Login failed: Incorrect username or password.")
        
    except (psycopg.DatabaseError, psycopg.Error) as e:
        messagebox.showerror("Error", f"Database error: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
def keyhandlerfunction(event):
   try:
       login_attempt(login_entry.get(), password_entry.get())
   except Exception as e:
       print("Error, Failed.", e)

            
# Sidebar frames and widgets
sidebar_frame2 = CTkFrame(master=Login_Form, fg_color="#FFF", width=526, height=645, corner_radius=10)
sidebar_frame2.pack_propagate(0)
sidebar_frame2.pack(anchor="ne", side="right")

sidebar_frame = CTkFrame(master=Login_Form, fg_color="#207244", width=330, height=645, corner_radius=10)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(anchor="nw", side="left")

lbl_welcome =CTkLabel(master=sidebar_frame2, text="Welcome Back Admin!", font=("Arial",40) )
lbl_welcome.pack(pady=50, padx = 10)

login_entry = CTkEntry(master=sidebar_frame2, width=400,height=40, placeholder_text="Enter username...", corner_radius=10,border_width=0, fg_color="#F0F0F0")
login_entry.pack(pady=10)

password_entry = CTkEntry(master=sidebar_frame2, width=400,height=40, placeholder_text="Enter password...",border_width=0,fg_color="#F0F0F0", show="*", corner_radius= 10)
password_entry.pack(pady=10)

btn_login2 = CTkButton(master=sidebar_frame2,hover_color= "#b5b5b5", width=300, height= 40, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=10, border_color="#207244", text="Login", command=lambda: login_attempt(login_entry.get(), password_entry.get()))
btn_login2.pack(pady=10)

btn_login5 = CTkButton(master=sidebar_frame2,hover_color= "#268750",  width=300, height= 10, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=100, border_color="#207244", text="Not an Admin? Register as a Student", command = call2)
btn_login5.pack(pady=10)

#img_logo_data = Image.open("MuchaTseBle.jpeg")
#img_logo = CTkImage(dark_image=img_logo_data, light_image=img_logo_data, size=(330, 650))
#CTkLabel(master=sidebar_frame, text="", image=img_logo).pack(anchor="center")

Login_Form.bind("<Return>", keyhandlerfunction)

Login_Form.mainloop()

