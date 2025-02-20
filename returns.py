from customtkinter import *
import tkinter
from CTkTable import CTkTable
from PIL import Image
import subprocess
from tkinter import messagebox
import psycopg

app = CTk()
app.geometry("856x645")
app.resizable(0,0)
app.title("School Library")
set_appearance_mode("light")
    
###########The Left hand side panel with the apps are in here -->>###########
quauntity_frame_no = 1
def quauntity_frame_count():
    global quauntity_frame_no
    quauntity_frame_no += 1
    lbl_quantity_count.configure(text = str(quauntity_frame_no))

def quantity_frame_count_subtraction():
    global quauntity_frame_no
    quauntity_frame_no -= 1
    lbl_quantity_count.configure(text = str(quauntity_frame_no))
    
def call():
    try:
        subprocess.Popen(["python", "returns_user.py"])
        app.destroy()
    except subprocess.CalledProcessError as e:
        print("Error executing returns_second.py", e)
        
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
    
def open_dashboard():
    app.destroy()
        
    try:
        subprocess.Popen(["python", "Dashboard_user.py"])
    except subprocess.CalledProcessError as e:
        print("Error executing Dashboard.py:", e)

def other_page():
    customer_name = customer_name_value.get()
    item_name = combobox.get()
    item_quantity = quauntity_frame_no
    address_name = address_value.get()

    if customer_name == "" or item_name == "" or item_quantity == "" or address_name =="":
        messagebox.showwarning("Warning", "Input fields are empty")
    else:
        try:
            conn = psycopg.connect("dbname='postgres' user='postgres' password='asdfghj3' host='localhost' port='5432'")
            cur = conn.cursor()
            cur.execute('INSERT INTO returns_(customer_name, items_name, item_quantity, address_name) VALUES (%s, %s, %s, %s)', (customer_name, item_name, item_quantity, address_name ))
            conn.commit()  # Commit the transaction
            call()
            
        except Exception as e:
            print(f"Error launching Orders_second.py: {e}")
        
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

#Sidebar- main
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

#Rocket image
logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

#Dashboard
analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command = open_dashboard).pack(anchor="center", ipady=5, pady=(60, 0))

#Feedback
feedback_img_data = Image.open("feedback_icon.png")
feedback_img = CTkImage(dark_image= feedback_img_data, light_image= feedback_img_data)
CTkButton(master = sidebar_frame, image = feedback_img, text = "Feedback", fg_color= "transparent", font = ("Arial Bold", 14), hover_color="#207244", anchor = "w", command= open_feedback).pack(anchor = "center", ipady =5, pady = (16, 0 ))
 
#Orders
#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
#CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command= open_orders).pack(anchor="center", ipady=5, pady=(16, 0))

#The order lists
#list_img_data = Image.open("list_icon.png")
#list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
#CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Returns
returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

#Settings
settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w", command = open_settings).pack(anchor="center", ipady=5, pady=(16, 0))

#Account
person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

#Whats happening in the main form where the feedback page is
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

CTkLabel(master= main_view, text = "Returns", font = ("Arial Bold", 25), text_color= "#207244").pack(anchor = "nw", pady= (20, 0), padx = 24)

customer_name_value = CTkEntry(master = main_view, placeholder_text= "Customer name...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
customer_name_value.pack(anchor = "nw", pady =(22, 0), padx = 24)

combobox_values = ["Biolgy KLB", "Chemistry KLB", "Physics KLB", "Mathematics KLB", "English KLB", "Kiswahili KLB", "History KLB", "Geography KLB", "CRE KLB", "Inventor Business", "Music KLB"]

combobox = CTkComboBox(master = main_view, values= combobox_values, width = 150,border_width= 3, border_color= "#207244")
combobox.pack(anchor = "nw", pady = (23,0), padx = 24)

#item_quantity_value = CTkEntry(master = main_view, placeholder_text= "Item quantity...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
#item_quantity_value.pack(anchor = "nw", pady =(23, 0), padx = 24)
quantity_frame = CTkFrame(master=main_view, fg_color="transparent",height=100,width=100, corner_radius=5)
quantity_frame.pack(anchor="nw", padx=24)

CTkLabel(master=quantity_frame, text="Quantity",text_color="#207244",font=("Arial Bold", 16)).pack(side="left", anchor="nw", padx=0,pady =(23, 0))
CTkButton(master=quantity_frame, text="-", width=25, fg_color="#2A8C55", hover_color="#207244", font=("Arial Black", 16), command=quantity_frame_count_subtraction).pack(side="left", anchor="nw",pady =(23, 0))
lbl_quantity_count = CTkLabel(master=quantity_frame, text="01", text_color="#2A8C55", font=("Arial Black", 16))
lbl_quantity_count.pack(side="left", anchor="nw", padx=10,pady =(23, 0))
CTkButton(master=quantity_frame, text="+", width=25,  fg_color="#2A8C55",hover_color="#207244", font=("Arial Black", 16),command= quauntity_frame_count).pack(side="left", anchor="nw",pady =(23, 0))


address_value = CTkEntry(master = main_view, placeholder_text= "Your address...", width = 250, font = ("Arial Bold", 14), border_width= 3, border_color= "#207244")
address_value.pack(anchor = "nw", pady =(24, 0), padx = 24)

package_img_data_2 = Image.open("package_icon.png")
package_img_2 = CTkImage(dark_image= package_img_data_2, light_image= package_img_data_2 )
CTkButton(master=main_view, image= package_img_2, text = "Submit", font= ("Arial Black", 14), border_color= "#207244", fg_color= "#fff", border_width= 3, command= other_page).pack(anchor = "nw", pady = 25, padx = 24)


app.mainloop()