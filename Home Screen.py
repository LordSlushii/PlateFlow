from customtkinter import *
home = CTk()
home.geometry("400x210")

mainMenu = ""
def register():
    home.withdraw()
    mainMenu = CTk()
    mainMenu.geometry("400x600")

    #Decoration
    title = CTkLabel(master=mainMenu, text = "MENU", font = ("Coolvetica", 30), text_color="#FFFF00")
    title.place(relx = 0.5, rely =0.05, anchor = "center")

#Decoration
title = CTkLabel(master=home, text = "PlateFlow", font = ("Coolvetica", 30), text_color="#FFFF00")
title.place(relx = 0.5, rely =0.12, anchor = "center")

subtitle = CTkLabel(master= home, text= "Click Here to Sign In", font = ("Arial", 15), text_color="#FFEE8C")
subtitle.place(relx = 0.5, rely = 0.35, anchor = "center")

#Buttons

register = CTkButton(master=home, text= "Sign In", font=("Arial", 15), fg_color="#FFFF00", text_color="#000000", command = register)
register.place(relx = 0.5, rely = 0.55, anchor = "center")
home.mainloop()

