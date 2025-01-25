from customtkinter import *
from PIL import Image
app = CTk()
app.geometry("856x645")




main_view = CTkFrame(master=app, fg_color="#49a628",  width=856, height=645, corner_radius=0)
main_view.pack(anchor="center")
main_view.pack_propagate(0)

main_img_data = Image.open("Easy_Market/EASY MARKETER.png")
main_img = CTkImage(light_image=main_img_data, dark_image= main_img_data)
img =CTkLabel(master=main_view, image=main_img, text="", height=100, width=100).pack(anchor="n", pady=10)

lbl = CTkLabel(master= main_view, text="Easy market", font=("Arial ", 40), text_color="white")
lbl.pack()

lbl1 = CTkLabel(master= main_view, text="Language", font=("Arial ", 30), text_color="white")
lbl1.pack(pady=20)

btn_login2 = CTkButton(master=main_view ,hover_color= "#b5b5b5", width=300, height= 40, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=10, border_color="#207244", text="English",)
btn_login2.pack(pady=10)

btn_login = CTkButton(master=main_view ,hover_color= "#b5b5b5", width=300, height= 40, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=10, border_color="#207244", text="Swahili",)
btn_login.pack(pady=10)

btn_login1 = CTkButton(master=main_view ,hover_color= "#b5b5b5", width=300, height= 40, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=10, border_color="#207244", text="Ugandan",)
btn_login1.pack(pady=10)

btn_login3 = CTkButton(master=main_view ,hover_color= "#b5b5b5", width=300, height= 40, font=("Arial", 16), text_color="Black", fg_color="#fff", border_width=3,corner_radius=10, border_color="#207244", text="German",)
btn_login3.pack(pady=10)





app.mainloop()