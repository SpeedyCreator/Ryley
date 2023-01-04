from tkinter import *
from function.JSON import*
from setting.view import*

MainColor = "white"
MainTextColor = "black"
SecondColor = "#1e23d3"
SecondTextColor = "white"

def Assistant(cadre,screen,btn1,btn2,btn3,btn4):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=MainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4)
    def Afficher():
        labelAssistant1.place(x=20,y=125)
        labelAssistant2.place(x=20,y=225)
        btnAssistant1.place(x=250,y=125)
        btnAssistant2.place(x=250,y=225)
    def NoAfficher():
        labelAssistant1.place_forget()
        labelAssistant2.place_forget()
        btnAssistant1.place_forget()
        btnAssistant2.place_forget()
    def ExitName():
        labelAssistant3.place_forget()
        entryName.place_forget()
        btnAssistantValider.place_forget()
        btnAssistant3.config(command=exit)
        Afficher()
    def ExitUser():
        labelAssistant4.place_forget()
        entryName.place_forget()
        btnAssistantValider.place_forget()
        btnAssistant3.config(command=exit)
        Afficher()
    def AssistantName():
        NoAfficher()
        def ValiderName():
            newName = entryName.get()
            EcritureJSON("setting/config.json","nomAssistant",newName)
            ExitName()
            Afficher()
        btnAssistant3.config(command=ExitUser)
        btnAssistantValider.config(command=ValiderName)
        labelAssistant3.place(x=20,y=125)
        entryName.place(x=100,y=230)
        btnAssistantValider.place(x=225,y=300)
    def AssistantUser():
        NoAfficher()
        def ValiderUser():
            newUser = entryName.get()
            EcritureJSON("setting/config.json","user",newUser)
            ExitUser()
            Afficher()
        btnAssistant3.config(command=ExitUser)
        btnAssistantValider.config(command=ValiderUser)
        labelAssistant4.place(x=20,y=125)
        entryName.place(x=100,y=230)
        btnAssistantValider.place(x=225,y=300)
    #declaration widget
    #btn
    btnAssistant1 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=AssistantName)
    btnAssistant2 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=AssistantUser)
    btnAssistant3 = Button(section,text="Exit",bg=MainColor,font=("arial","15"),fg=MainTextColor,command=exit)
    btnAssistantValider = Button(section,text="Valider",bg=SecondColor,font=("arial","15"),fg=SecondTextColor)
    #Label
    labelIndication =Label(section,text="Changer le nom de l'assistant",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelAssistant1 = Label(section,text="Nom de l'assistant",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelAssistant2 = Label(section,text="Utilisateur ",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelAssistant3 = Label(section,text="Nouveau nom :",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelAssistant4 = Label(section,text="Comment vous-vous appelez :",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelIndication.place(x=125,y=0)
    #entry
    entryName = Entry(section,width=30,font=("arial","15"))
    Afficher()
    
    btnAssistant3.place(x=225,y=525)