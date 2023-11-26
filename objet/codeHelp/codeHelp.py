from tkinter import*
from tkinter import colorchooser
from tkinter.filedialog import*
from tkinter.messagebox import*
from librairy.travailJSON import*
from src.gestionRyley import *
import webbrowser as w

class CCodeHelp :
    def __init__(self,screen:Tk,gestionnaireRL:gestionRL) :
        self.__wScreen = screen
        self.__gestionnaireRyley = gestionnaireRL
        #image 
        self.__icon = PhotoImage(file="asset/codehelp/codeHelpIcon.png")
        #Creation Canvas
        #fondBGTopLeft
        self.__fondBGTopLeft = Canvas(self.__wScreen,width=150,height=600, highlightthickness=0)
        #fondBGTopRight
        self.__fondBGTopRight = Canvas(self.__wScreen,width=350,height=400, highlightthickness=0)
        #fondBGBottom
        self.__fondBGBottom = Canvas(self.__wScreen,width=350,height=200, highlightthickness=0)
        #Frame parametre
        self.__framePara = Frame(self.__wScreen,width=500,height=600)
        #widget parametre
        self.__labelPara = Label(self.__framePara,text="Parametre CodeHelp",font=("arial","15"))
        self.__btnQuitterPara = Button(self.__framePara,text="Quitter",font=("arial","15"),command=self.unViewPara)
        # BTN App sur Canvas fondBGTopLeft
        self.__btnBack = Button(self.__fondBGTopLeft,command=self.backRyley)
        self.__btnColorSelector = Button(self.__fondBGTopLeft,command=lambda:self.__selecteurColor.bootSelecteur())
        self.__btnEditeurDoc = Button(self.__fondBGTopLeft)
        self.__btnGithub = Button(self.__fondBGTopLeft)
        self.__btnLibrairy = Button(self.__fondBGTopLeft,command=lambda : self.__lib.librairy())
        self.__btnOrgaVar = Button(self.__fondBGTopLeft,command=lambda : self.__orgaVar.bootOrganisateur()) 
    
    def __affichage(self):
        self.setTheme()
        self.__largeurFondAPP = self.__fondBGTopLeft.winfo_reqwidth()
        self.__btnEditeurDoc.place(x=((self.__largeurFondAPP-self.__btnEditeurDoc.winfo_reqwidth())//2),y=100)
        self.__btnGithub.place(x=((self.__largeurFondAPP-self.__btnGithub.winfo_reqwidth())//2),y=170)
        self.__btnLibrairy.place(x=((self.__largeurFondAPP-self.__btnLibrairy.winfo_reqwidth())//2),y=240)
        self.__btnOrgaVar.place(x=((self.__largeurFondAPP-self.__btnOrgaVar.winfo_reqwidth())//2),y=310)
        self.__btnColorSelector.place(x=((self.__largeurFondAPP-self.__btnColorSelector.winfo_reqwidth())//2),y=380)
        self.__btnBack.place(x=((self.__largeurFondAPP-self.__btnBack.winfo_reqwidth())//2),y=(self.__fondBGTopLeft.winfo_reqheight()-self.__btnBack.winfo_reqheight()-20))

    def __clearView(self):
        self.__btnEditeurDoc.place_forget()
        self.__btnGithub.place_forget()
        self.__btnLibrairy.place_forget()
        self.__btnOrgaVar.place_forget()
        self.__btnColorSelector.place_forget()
        self.__btnBack.place_forget()


    def setFonctionback(self,fnc):
        self.__fncBack = fnc

    def setTheme(self):
        self.__mainColor = self.__gestionnaireRyley.getMaincolor()
        self.__mainTextColor = self.__gestionnaireRyley.getMainTextcolor()
        #objet 
        self.__selecteurColor = CCHcolorSelector(self.__mainColor,self.__mainTextColor)
        self.__orgaVar = CHOrgraVarriable(self.__mainColor,self.__mainTextColor)
        self.__lib = CHLibrairy(self.__mainColor,self.__mainTextColor)
        #Frame parametre
        self.__framePara.configure(bg=self.__mainColor)
        #Widget parametre
        self.__btnQuitterPara.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__labelPara.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        #fondBGTopLeft
        BGTopLeft = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpLeft(),master=self.__fondBGTopLeft)
        self.__fondBGTopLeft.image_names = BGTopLeft
        self.__fondBGTopLeft.create_image(0,0,image=BGTopLeft,anchor="nw")
        #fondBGTopRight
        BGTopRight = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpRight(),master=self.__fondBGTopRight)
        self.__fondBGTopRight.image_names = BGTopRight
        self.__fondBGTopRight.create_image(0,0,image=BGTopRight,anchor="nw")
        #fondBGBottom
        BGBottom = PhotoImage(file=self.__gestionnaireRyley.getBGBottomCodeHelp(),master=self.__fondBGBottom)
        self.__fondBGBottom.image_names = BGBottom
        self.__fondBGBottom.create_image(0,0,image=BGBottom,anchor="nw")
        # BTN App sur Canvas fondBGTopLeft
        #__btnBack
        IMGBack = PhotoImage(file=self.__gestionnaireRyley.getBTNIconBack(),master=self.__btnBack)
        self.__btnBack.image_names = IMGBack
        self.__btnBack.configure(image=IMGBack)
        #__btnColorSelector
        IMGColorSelector = PhotoImage(file=self.__gestionnaireRyley.getBTNIconColorSelector(),master=self.__btnColorSelector)
        self.__btnColorSelector.image_names = IMGColorSelector
        self.__btnColorSelector.configure(image=IMGColorSelector)
        #__btnEditeurDoc
        IMGEditeurDoc = PhotoImage(file=self.__gestionnaireRyley.getBTNIconEditeurDoc(),master=self.__btnEditeurDoc)
        self.__btnEditeurDoc.image_names = IMGEditeurDoc
        self.__btnEditeurDoc.configure(image=IMGEditeurDoc)#
        #__btnGithub
        IMGGithub = PhotoImage(file=self.__gestionnaireRyley.getBTNIconGitHub(),master=self.__btnGithub)
        self.__btnGithub.image_names = IMGGithub
        self.__btnGithub.configure(image=IMGGithub)#
        #__btnLibrairy
        IMGLibrairy = PhotoImage(file=self.__gestionnaireRyley.getBTNIconLibrairy(),master=self.__btnLibrairy)
        self.__btnLibrairy.image_names = IMGLibrairy
        self.__btnLibrairy.configure(image=IMGLibrairy)#
        #__btnOrgaVar
        IMGOrgaVar = PhotoImage(file=self.__gestionnaireRyley.getBTNIconOrgaVar(),master=self.__btnOrgaVar)
        self.__btnOrgaVar.image_names = IMGOrgaVar
        self.__btnOrgaVar.configure(image=IMGOrgaVar)#
        
    def viewPara(self):
        self.__wScreen.title("Codehelp : Parametre")
        self.__framePara.pack()
        self.__fondBGTopLeft.place_forget()
        self.__fondBGTopRight.place_forget()
        self.__fondBGBottom.place_forget()
    
    def unViewPara(self):
        self.__wScreen.title("Ryley : Codehelp")
        self.__framePara.pack_forget()
        self.__clearView()
        self.__affichage()
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)

    def view(self):
        #Modification de la fenetre 
        self.__wScreen.title("Ryley : Codehelp")
        self.__wScreen.iconphoto(False,self.__icon)
        self.__wScreen.update()
        self.__clearView()
        self.__affichage()
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)
        #Calcule frame para
        lageurFrame = self.__framePara.winfo_reqwidth()
        hauteurFrame = self.__framePara.winfo_reqheight()
        self.__btnQuitterPara.place(x=((lageurFrame-self.__btnQuitterPara.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnQuitterPara.winfo_reqheight()))
        self.__labelPara.place(x=((lageurFrame-self.__labelPara.winfo_reqwidth())//2),y=0)
    
    def backRyley(self):
        self.__fncBack()

    def unView(self):
        self.__fondBGTopLeft.place_forget()
        self.__fondBGTopRight.place_forget()
        self.__fondBGBottom.place_forget()
    
class CCHcolorSelector:
    def __init__(self,mainColor:str,textColor:str):
        self.__mainColor = mainColor
        self.__mainTextColor = textColor

    def bootSelecteur(self):
        self.__screenColor = Toplevel()
        self.__screenColor.title("CodeHelp : selecteur de couleur")
        self.__screenColor.config(bg=self.__mainColor)
        self.__screenColor.iconphoto(False,PhotoImage(file="asset/codehelp/codeHelpIcon.png"))
        self.__screenColor.maxsize(800,500)
        self.__screenColor.minsize(800,500)
        #fonction
        #cadre
        cadreNoir = Frame(self.__screenColor,bg="black",width=325,height=325,border=100)
        self.__cadreColor = Frame(cadreNoir,bg="#ffffff",width=310,height=310)
        #label
        self.__labelIndicationCode = Label(self.__screenColor,text="Code HTML : #ffffff \nCode RGB : (255,255,255)",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),justify="left")     
        #declaration des bouton
        buttonSelection = Button(self.__screenColor,text="Selectionner la couleur",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),command=self.__selecteur)
        self.__buttonCopiHTLM = Button(self.__screenColor,text="Copier le code HTML",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        self.__buttonCopiRGB = Button(self.__screenColor,text="Copier le code RGB",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        #affichage
        self.__cadreColor.place(relx=0.5, rely=0.5, anchor=CENTER)
        cadreNoir.pack(side="right")
        self.__labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        self.__buttonCopiHTLM.place(x=15,y=235)
        self.__buttonCopiRGB.place(x=15,y=335)
        
    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur",color=self.__mainColor)
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__cadreColor.config(bg=self.__colorHTLM)
        self.__buttonCopiHTLM.config(command=self.__copieHTLM)
        self.__buttonCopiRGB.config(command=self.__copieRGB)
        self.__labelIndicationCode.config(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorRGB)
    
class CHOrgraVarriable:
        def __init__(self,mainColor:str,textColor:str):
            self.__mainColor = mainColor
            self.__mainTextColor = textColor
            self.__docOpen = False
            self.__file = ""
        
        def bootOrganisateur(self):
            self.__docOpen = False
            self.__file = ""
            self.__screenOrganisateurVar = Toplevel()
            self.__screenOrganisateurVar.minsize(1000,700)
            self.__screenOrganisateurVar.maxsize(1000,700)
            self.__screenOrganisateurVar.title("CodeHelp : Organisateur de varriable")
            self.__screenOrganisateurVar.iconphoto(False,PhotoImage(file="asset/codehelp/codeHelpIcon.png"))
            self.__screenOrganisateurVar.config(bg="red")
            #var
            self.__varType = StringVar(self.__screenOrganisateurVar)
            self.__varSuppr = StringVar(self.__screenOrganisateurVar)
            self.__listSuppr = ["","",""]
            self.__listType = ["int", "bool", "char", "string", 
                               "float", "list", "tuple", "dict", 
                               "set", "bytes", "date", "time", 
                               "enum", "object"]
            #Frame
            self.__frameNoOpenDoc = Frame(self.__screenOrganisateurVar,width=500,height=700,bg=self.__mainColor)
            frameAdd = Frame(self.__screenOrganisateurVar,width=500,height=350,bg=self.__mainColor,relief=GROOVE,bd=5)
            self.__frameSuppr = Frame(self.__screenOrganisateurVar,width=500,height=350,bg=self.__mainColor,relief=GROOVE,bd=5)
            #Widget
            self.__zoneEcriture = Text(self.__screenOrganisateurVar)
            #Menu
            self.__menuediteur = Menu(self.__screenOrganisateurVar,bg=self.__mainColor,fg=self.__mainTextColor)
            self.__menuediteur.add_command(label="Enregistrer",command=self.__saveOnFile)
            self.__menuediteur.add_command(label="Nouveau",command=self.__newDoc)
            self.__menuediteur.add_command(label="Ouvrir",command=self.__openDoc)
            #frameNoOpenDoc
            labelNoDoc = Label(self.__frameNoOpenDoc,font=("arial","35"),bg=self.__mainColor,fg=self.__mainTextColor,text="Pas de document\nouvert")
            #Widget frameAdd
            labelAdd = Label(frameAdd,text="Ajouter une varriable",font=("arial","25"),bg=self.__mainColor,fg=self.__mainTextColor)
            btnAdd = Button(frameAdd,text="Valider",font=("arial","15"),bg=self.__mainColor,fg=self.__mainTextColor,command=self.__addValeur)
            frameEntry = Frame(frameAdd,bg=self.__mainColor,width=450,height=70)
            self.__entryName = Entry(frameEntry,font=("arial","13"),relief=SOLID)
            self.__entryValeur = Entry(frameEntry,font=("arial","13"),relief=SOLID)
            menuType = OptionMenu(frameEntry,self.__varType,*self.__listType)
            #Widget frameSuppr
            labelSuppr = Label(self.__frameSuppr,text="Supprimer une varriable",font=("arial","25"),bg=self.__mainColor,fg=self.__mainTextColor)
            btnSuppr = Button(self.__frameSuppr,text="Valider",font=("arial","15"),bg=self.__mainColor,fg=self.__mainTextColor,command=self.__supprValeur)
            self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
            #Affichage
            self.__frameNoOpenDoc.place(relx=0, rely=0, relwidth=0.5, relheight=1)
            frameAdd.place(x=self.__screenOrganisateurVar.winfo_width()/2, y=0)
            self.__frameSuppr.place(x=self.__screenOrganisateurVar.winfo_width()/2, y=self.__screenOrganisateurVar.winfo_height()/2)
            #frameAdd
            labelAdd.place(x=((frameAdd.winfo_reqwidth()-labelAdd.winfo_reqwidth())//2),y=2)
            btnAdd.place(x=((frameAdd.winfo_reqwidth()-btnAdd.winfo_reqwidth())//2),y=(frameAdd.winfo_reqheight()-btnAdd.winfo_reqheight()-2))
            frameEntry.place(relx=0.5,rely=0.5,anchor="center")
            self.__entryName.place(x=2,y=((frameEntry.winfo_reqheight()-self.__entryName.winfo_reqheight())//2))
            menuType.place(relx=0.5,rely=0.5,anchor="center")
            self.__entryValeur.place(x=((frameEntry.winfo_reqwidth()-self.__entryValeur.winfo_reqwidth())-2),y=((frameEntry.winfo_reqheight()-self.__entryValeur.winfo_reqheight())//2))
            #frameSuppr
            labelSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-labelSuppr.winfo_reqwidth())//2),y=0)
            self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
            btnSuppr.place(x=((self.__frameSuppr.winfo_reqwidth()-btnSuppr.winfo_reqwidth())//2),y=(self.__frameSuppr.winfo_reqheight()-btnSuppr.winfo_reqheight()-10))
            #frameNoOpenDoc
            labelNoDoc.place(relx=0.5,rely=0.5,anchor="center")
            #Ajout de menu a la fenetre
            self.__varType.set(self.__listType[0])
            self.__screenOrganisateurVar.config(menu=self.__menuediteur)
    
        def __openDoc(self):
            if self.__docOpen == True :
                showwarning("Document ouvert","Un document est encore ouvert fermer le avant d'ouvrir un autre")
            else :
                self.__file = askopenfilename(defaultextension=".chov", filetypes=[("Fichier Codehelp Orga Var", ".chov")])
                if self.__file :
                    self.__docOpen = True 
                    self.__menuediteur.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
                    self.__frameNoOpenDoc.place_forget()
                    self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                    with open(self.__file, "r") as f:
                        data = json.load(f)
                        self.__zoneEcriture.config(state="normal")
                        self.__zoneEcriture.delete("1.0", END)
                        for key, value in data.items():
                            self.__zoneEcriture.config(state="normal")
                            self.__zoneEcriture.insert(END, f"{key}:{value}\n")
                            self.__zoneEcriture.config(state="disable")
                        self.__refreshSuppr()
                else :
                    showwarning("Aucun document selectionner","Veuillez selectionner un document")

        def __newDoc(self):
            self.__file = asksaveasfilename(defaultextension=".chov", filetypes=[("Fichier Codehelp Orga Var", ".chov")])
            if self.__file :
                #Initialisation de zoneEcriture
                self.__zoneEcriture.config(state="normal")
                self.__zoneEcriture.delete("1.0",END)
                self.__zoneEcriture.insert("1.0","Type name : valeur")
                self.__zoneEcriture.config(state="disable")
                self.__docOpen = True 
                self.__menuediteur.entryconfigure("Ouvrir",label="Fermer",command=self.__closeDoc)
                self.__frameNoOpenDoc.place_forget()
                self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                self.__refreshSuppr()
            else :
                showwarning("Aucun document enregister","Veuillez enregister un document")

        def __closeDoc(self):
            if self.__docOpen == True :
                self.__file = ""
                self.__docOpen = False
                self.__menuediteur.entryconfigure("Fermer",label="Ouvrir",command=self.__openDoc)
                self.__zoneEcriture.place_forget()
                self.__frameNoOpenDoc.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                self.__clearMenuSuppr()
            else :
                showwarning("Aucun document ouvert","Aucun document n'est ouvert")
    
        def __addValeur(self):
            if self.__docOpen == True :
                self.__zoneEcriture.config(state="normal")
                name = self.__entryName.get()
                value = self.__entryValeur.get()
                typeVar = self.__varType.get()
                if name and value and typeVar :
                    key = typeVar+" "+name
                    self.__entryName.delete(0, END)
                    self.__entryValeur.delete(0, END)
                    d = self.__zoneEcriture.get("1.0", "end")
                    d = dict(map(str, item.split(':')) for item in d.strip().split('\n'))
                    d[key] = value
                    self.__zoneEcriture.delete("1.0", END)
                    for key, value in d.items():
                        self.__zoneEcriture.insert(END, f"{key}:{value}\n")
                    self.__zoneEcriture.place_forget()
                    self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                    self.__zoneEcriture.config(state="disable")
                    self.__saveOnFile()
                    self.__refreshSuppr()
                else:
                    showwarning("Erreur ecriture","Veuillez entrer tout la valeur pour ajouter une varriable")
            else :
                showwarning("Aucun document ouvert","Veuillez ouvrir un document")

        def __saveOnFile(self):
            if self.__docOpen == True :
                data = self.__zoneEcriture.get("1.0", "end")
                data = dict(map(str, item.split(':')) for item in data.strip().split('\n'))
                with open(self.__file, "w") as f:
                    json.dump(data, f)
            else :
                showwarning("Imposible d'enregistrer","Aucun document ouvert")

        def __refreshSuppr(self):
            self.__menuSuppr.place_forget()
            self.__menuSuppr.destroy()
            data = self.__zoneEcriture.get("1.0", "end")
            data = dict(map(str, item.split(':')) for item in data.strip().split('\n'))
            del data["Type name "]
            if not data :
                self.__listSuppr = ["","",""]
            else :
                self.__listSuppr = list(data.keys())
            self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
            self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
        
        def __supprValeur(self):
            valeur = self.__varSuppr.get()
            if valeur :
                d = self.__zoneEcriture.get("1.0", "end")
                d = dict(map(str, item.split(':')) for item in d.strip().split('\n'))
                del d[valeur]
                self.__zoneEcriture.config(state="normal")
                self.__zoneEcriture.delete("1.0", END)
                for key, value in d.items():
                    self.__zoneEcriture.insert(END, f"{key}:{value}\n")
                self.__zoneEcriture.place_forget()
                self.__zoneEcriture.place(relx=0, rely=0, relwidth=0.5, relheight=1)
                self.__zoneEcriture.config(state="disable")
                self.__saveOnFile()
                self.__refreshSuppr()
            else :
                showwarning("Imposible de supprimer une varriable","Aucun varriable selectionner")
        
        def __clearMenuSuppr(self):
            self.__menuSuppr.place_forget()
            self.__menuSuppr.destroy()
            self.__listSuppr = ["","",""]
            self.__menuSuppr = OptionMenu(self.__frameSuppr,self.__varSuppr,*self.__listSuppr)
            self.__menuSuppr.place(relx=0.5,rely=0.5,anchor="center")

class CHLibrairy:
    def __init__(self,mainColor:str,textColor:str):
        self.__lienLibrairy = "https://github.com/Arrera-Software/Arrera-librairy"
        self.__lienReadme =  "https://github.com/Arrera-Software/Arrera-librairy/blob/main/README.md"
        self.__lienObjetPython = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/python"
        self.__lienObjetCPP = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/C%2B%2B"
        self.__mainColor = mainColor
        self.__textColor = textColor
    
    def librairy(self):
        self.__screenLibrairy = Toplevel()
        self.__screenLibrairy.title("CodeHelp : librairy")
        self.__screenLibrairy.minsize(700,500)
        self.__screenLibrairy.configure(bg=self.__mainColor)
        #widget
        btnlib = Button(self.__screenLibrairy,text="Librairy",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openLib)
        btnReadme = Button(self.__screenLibrairy,text="Readme",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openReadme)
        btnObjetPyton = Button(self.__screenLibrairy,text="Objet Python",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openObjPython)
        btnObjetCPP = Button(self.__screenLibrairy,text="Objet C++",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openObjCPP)
        #affichage
        btnlib.place(relx=0.1, rely=0.1)
        btnObjetPyton.place(relx=0.1, rely=0.8)
        btnObjetCPP.place(relx=0.8, rely=0.1)
        btnReadme.place(relx=0.8, rely=0.8)

    def __destroyWindows(self):
        self.__screenLibrairy.destroy()

    def __openLib(self):
        w.open(self.__lienLibrairy)
        self.__destroyWindows()
    
    def __openReadme(self):
        w.open(self.__lienReadme)
        self.__destroyWindows()
    
    def __openObjPython(self):
        w.open(self.__lienObjetPython)
        self.__destroyWindows()
    
    def __openObjCPP(self):
        w.open(self.__lienObjetCPP)
        self.__destroyWindows()


