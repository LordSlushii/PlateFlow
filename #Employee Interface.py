#Employee Interface
from customtkinter import *
import csv

home = ""
def openHome():
    home = CTk()
    home.geometry("400x200")

    #Decoration

    title = CTkLabel(master=home, text = "PlateFlow", font = ("Coolvetica", 30), text_color="#FF6B00")
    title.place(relx = 0.5, rely =0.12, anchor = "center")

    subtitle = CTkLabel(master= home, text= "Your Drive-Thru Experience Made Seemless!", font = ("Coolvetica", 15), text_color="#FFFFFF")
    subtitle.place(relx = 0.5, rely = 0.25, anchor = "center")



    #Buttons
    def reg():
        home.withdraw()
        register = CTk()
        register.geometry("500x150")

        def openCam():
            pass

        openCam = CTkButton(master=register, text= "Open Camera", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130 , command = openCam)
        openCam.place(relx = 0.22, rely = 0.5, anchor = "center")
        
        def openManual():
            register.withdraw()
            man = CTk()
            man.geometry("500x200")


            numLabel = CTkLabel(master=man, text = "Enter Number Plate:", font = ("Coolvetica", 20), text_color="#FFFFFF")
            numLabel.place(relx = 0.22, rely = 0.2, anchor = "center")

            file_text = CTkEntry(master = man, placeholder_text="UP14XX0123", width=200, height=50)
            file_text.place(relx = 0.68, rely = 0.2, anchor = "center")

            orderLabel = CTkLabel(master=man, text = "Enter Order:", font = ("Coolvetica", 20), text_color="#FFFFFF")
            orderLabel.place(relx = 0.22, rely = 0.5, anchor = "center")

            order = CTkEntry(master = man, width=200, height=50)
            order.place(relx = 0.68, rely = 0.5, anchor = "center")

            def Back():
                man.withdraw()
                reg()

            back = CTkButton(master=man, text= "Go Back", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 45, width = 130 , command = Back)
            back.place(relx = 0.35, rely = 0.8, anchor = "center")
            
            def submit():
                pass

            submit = CTkButton(master=man, text= "Submit", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 45, width = 130 , command = submit())
            submit.place(relx = 0.63, rely = 0.8, anchor = "center")

            man.mainloop()

        manual = CTkButton(master=register, text= "Enter Manually ", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130 , command = openManual)
        manual.place(relx = 0.5, rely = 0.5, anchor = "center")

        def goBack():
            register.withdraw()
            openHome()
        back  = CTkButton(master=register, text= "Go Back ", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130 , command = goBack)
        back.place(relx = 0.78, rely = 0.5, anchor = "center")

        register.mainloop()
    register = CTkButton(master=home, text= "Register", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130 , command = reg)
    register.place(relx = 0.32, rely = 0.55, anchor = "center")
    
    def orderHistory():
        home.withdraw()
        historyWindow = CTk()
        historyWindow.geometry("300x400")
        orderFile = open("/Users/navaneethkrishna/Desktop/DevJams\'24/orders.csv", 'r')
        readFile = csv.reader(orderFile)
        lis = []
        for i in readFile:
            lis.append(i)

        heading = CTkLabel(master = historyWindow, text= "Order History", font = ("Coolvetica", 30), text_color="#FF6B00")
        heading.place(relx = 0.5, rely = 0.08, anchor = "center")

        c1 = CTkLabel(master = historyWindow, text = lis[-1][0], font = ("Coolvetica", 20), text_color="#FFFFFF")
        c1.place(relx = 0.5, rely = 0.2, anchor = "center")
        t1 = lis[-1][1].replace("[", "")
        t1 = t1.replace("]", "")

        def o1green():
             o1 = CTkButton(master = historyWindow, text = t1, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, fg_color= "green")
             o1.place(relx = 0.5, rely = 0.3, anchor = "center")

        o1 = CTkButton(master = historyWindow, text = t1, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, command= o1green)
        o1.place(relx = 0.5, rely = 0.3, anchor = "center")

        c2 = CTkLabel(master = historyWindow, text = lis[-2][0], font = ("Coolvetica", 20), text_color="#FFFFFF")
        c2.place(relx = 0.5, rely = 0.45, anchor = "center")
        t2 = lis[-2][1].replace("[", "")
        t2 = t2.replace("]", "")

        def o2green():
             o2 = CTkButton(master = historyWindow, text = t2, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, fg_color= "green")
             o2.place(relx = 0.5, rely = 0.55, anchor = "center")

        o2 = CTkButton(master = historyWindow, text = t2, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, command = o2green)
        o2.place(relx = 0.5, rely = 0.55, anchor = "center")

        c3 = CTkLabel(master = historyWindow, text = lis[-3][0], font = ("Coolvetica", 20), text_color="#FFFFFF")
        c3.place(relx = 0.5, rely = 0.70, anchor = "center")
        t3 = lis[-3][1].replace("[", "")
        t3 = t3.replace("]", "")

        def o3green():
            o3 = CTkButton(master = historyWindow, text = t3, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, fg_color='green')
            o3.place(relx = 0.5, rely = 0.80, anchor = "center")
        o3 = CTkButton(master = historyWindow, text = t3, font = ("Coolvetica", 20), text_color="#FFFFFF", height=50, width=250, command=o3green)
        o3.place(relx = 0.5, rely = 0.80, anchor = "center")

        def ref():
            historyWindow.destroy()
            orderHistory()
        
        refresh = CTkButton(master = historyWindow, text = "Refresh", font = ("Coolvetica", 20), text_color="#FFFFFF", height=20, width=130, command=ref)
        refresh.place(relx= 0.275, rely= 0.92, anchor = 'center')

        def backk():
            historyWindow.withdraw()
            openHome()

        back = CTkButton(master = historyWindow, text = "Go Back", font = ("Coolvetica", 20), text_color="#FFFFFF", height=20, width=130, command=backk)
        back.place(relx= 0.725, rely= 0.92, anchor = 'center')

    history=  CTkButton(master=home, text= "History", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130, command= orderHistory)
    history.place(relx = 0.68, rely = 0.55, anchor = "center")

    def close():
        home.destroy()

    close = CTkButton(master=home, text= "Close", font=("Bebas", 15), fg_color="#FF6B00", text_color="#000000", height = 50, width = 130, command= close)
    close.place(relx = 0.5, rely = 0.85, anchor = "center")

    home.mainloop()

    

openHome()
