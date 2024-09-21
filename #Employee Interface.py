#Employee Interface

from customtkinter import *

home = CTk()
home.geometry("400x200")
def close():
    home.destroy()
#Decoration

title = CTkLabel(master=home, text = "PlateFlow", font = ("Coolvetica", 30), text_color="#FF6B00")
title.place(relx = 0.5, rely =0.12, anchor = "center")

subtitle = CTkLabel(master= home, text= "Your Drive-Thru Experience Made Seemless!", font = ("Coolvetica", 15), text_color="#FFFFFF")
subtitle.place(relx = 0.5, rely = 0.25, anchor = "center")



#Buttons

register = CTkButton(master=home, text= "Register ", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130)
register.place(relx = 0.32, rely = 0.55, anchor = "center")

history=  CTkButton(master=home, text= "History", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130)
history.place(relx = 0.68, rely = 0.55, anchor = "center")

close = CTkButton(master=home, text= "Close", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130, command= close)
close.place(relx = 0.5, rely = 0.85, anchor = "center")

home.mainloop()




