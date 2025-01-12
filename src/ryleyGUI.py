from librairy.arrera_tk import CArreraTK
from ObjetsNetwork.arreraNeuron import *
from src.CLanguageRyley import *

VERSION = "I2025-1.00"

class guiRyley:
    def __init__(self, neuronConfigFile: str):
        # Varriable
        self.__nameSoft = "Arrera RYLEY"
        # Boot ArreraTK
        self.__arrTK = CArreraTK()

        # Demarage Neuron Network
        self.__assistantRyley = ArreraNetwork(neuronConfigFile)

        # Demarage objet language Ryley
        self.__language = CLanguageRyley("",
                                              "fichierJSON/aideRyley.json",
                                              "")

        # Teste sur de l'OS hote
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        del objOS

        # Demarage de l'interface
        self.__screen = self.__arrTK.aTK(0,title=self.__nameSoft, resizable=False,
                                         width=500, height=600)
        self.__screen.protocol("WM_DELETE_WINDOW", self.__quitRyley)

        # Icon
        if self.__windowsOS:
            self.__emplacementIcon = "asset/Ryley.ico"
        else :
            self.__emplacementIcon = "asset/Ryley.png"

        # Definition des images
        emplacementLight = "asset/GUI/light/"
        emplacementDark = "asset/GUI/dark/"

        listIMG = ["top.png",#0
                   "bottom.png",#1
                   "send.png",#2
                   "settings.png",#3
                   "iconRyleyCodehelp.png",#4
                   "tableur.png",#5
                   "word.png",#6
                   "projet.png",#7
                   "bottomOpen.png",#8
                   ]
        # Creation des images

        imgSend = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[2],
                                           pathDark=emplacementDark + listIMG[2],
                                           tailleX=30, tailleY=30)
        imgPara = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[3],
                                             pathDark=emplacementDark + listIMG[3],
                                             tailleX=30, tailleY=30)

        imgCodehelp = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[4],
                                             pathDark=emplacementDark + listIMG[4],
                                             tailleX=30, tailleY=30)
        imgTableurOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[5],
                                                    pathDark=emplacementDark + listIMG[5],
                                                    tailleX=30, tailleY=30)
        imgWordOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[6],
                                                    pathDark=emplacementDark + listIMG[6],
                                                    tailleX=30, tailleY=30)
        imgProjetOpen = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[7],
                                                    pathDark=emplacementDark + listIMG[7],
                                                    tailleX=30, tailleY=30)

        # Frame
        self.__topBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + listIMG[0],
                                                                      imageDark=emplacementDark + listIMG[0],
                                                                      width=500, height=400)
        self.__bottomBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                         imageLight=emplacementLight + listIMG[1],
                                                                         imageDark=emplacementDark + listIMG[1],
                                                                         width=500, height=70)
        self.__frameBackgroud = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#081ec7",corner_radius=0)

        self.__frameBottomOpen = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                         imageLight=emplacementLight + listIMG[8],
                                                                         imageDark=emplacementDark + listIMG[8],
                                                                         width=500, height=70,bg="#081ec7")
        # Widget
        # Entry
        self.__entryUser = self.__arrTK.createEntry(self.__frameBackgroud,
                                             ppolice="Arial", ptaille=25, width=350)

        # Bouton
        btnSend = self.__arrTK.createButton(self.__frameBackgroud, image=imgSend,
                                            width=40, height=40, command=self.__envoi,
                                            bg="#3b4bca", hoverbg="#051484")

        btnPara = self.__arrTK.createButton(self.__frameBackgroud,image=imgPara,
                                            width=40, height=40,
                                            bg="#3b4bca",hoverbg="#051484")

        btnCodehelp = self.__arrTK.createButton(self.__frameBackgroud,image=imgCodehelp,
                                                width=40,height=40,
                                                bg="#3b4bca", hoverbg="#051484")

        # Label
        self.__lparole = self.__arrTK.createLabel(self.__topBackgroup,
                                                  bg="#041f75", fg="white",
                                                  ppolice="Arial",pstyle="bold",
                                                  ptaille=18,justify="left",pwraplength=400)

        # Button
        self.__btnTableurOpen = self.__arrTK.createButton(self.__frameBottomOpen, width=35, height=35,
                                                          image=imgTableurOpen,command=lambda : self.__winHelpFileAndProjet(1),
                                                          bg="#3b4bca",hoverbg="#051484")

        self.__btnWordOpen = self.__arrTK.createButton(self.__frameBottomOpen, width=35, height=35,
                                                       image=imgWordOpen,command=lambda : self.__winHelpFileAndProjet(2),
                                                       bg="#3b4bca",hoverbg="#051484")

        self.__btnProjetOpen = self.__arrTK.createButton(self.__frameBottomOpen, width=35, height=35,
                                                         image=imgProjetOpen,command=lambda : self.__winHelpFileAndProjet(3),
                                                         bg="#3b4bca",hoverbg="#051484")

        # Affichage des widgets
        self.__entryUser.place(relx=0.40, rely=0.3, anchor="center")
        btnSend.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparole.place(x=55, y=280)

        self.__arrTK.placeBottomLeft(btnPara)
        self.__arrTK.placeBottomRight(btnCodehelp)
        # Bind
        self.keyboard()
        # Instruction a supprimer par la suite
        self.__assistantRyley.boot(1)

    def active(self):
        self.__viewNormal()
        self.__arrTK.view()

    def __disableAllFrame(self):
        self.__topBackgroup.pack_forget()
        self.__bottomBackgroup.pack_forget()
        self.__frameBackgroud.pack_forget()
        self.__frameBottomOpen.pack_forget()

    def __viewNormal(self):
        self.__topBackgroup.pack()
        self.__bottomBackgroup.pack()
        self.__frameBackgroud.pack()

    def __viewOpen(self):
        self.__topBackgroup.pack()
        self.__frameBottomOpen.pack()
        self.__frameBackgroud.pack()

    def __paroleRyley(self, text: str):
        if text != "":
            self.__lparole.configure(text=text)
            self.__entryUser.delete(0, END)

    def __quitRyley(self):
        if (askyesno("Atention", "Voulez-vous vraiment fermer Ryley")):
            self.__close()

    def __close(self):
        self.__paroleRyley(self.__assistantRyley.shutdown())
        self.__screen.destroy()

    def __apropos(self):
        self.__arrTK.aproposWindows(
            nameSoft=self.__nameSoft,
            iconFile=self.__emplacementIcon,
            version=VERSION,
            copyright="Copyright Arrera Software by Baptiste P 2023-2025",
            linkSource="https://github.com/Arrera-Software/Ryley",
            linkWeb="https://arrera-software.fr/")

    def __envoi(self):

        texte = self.__entryUser.get().lower()
        self.__entryUser.delete(0, END)
        if ("parametre" in texte ) :
            pass
        else :
            self.__assistantRyley.neuron(texte)
            nbSortie = self.__assistantRyley.getValeurSortie()
            listSortie = self.__assistantRyley.getListSortie()
            match nbSortie:
                case 0 :
                    self.__paroleRyley(listSortie[0])
                case 1 :
                    self.__paroleRyley(listSortie[0])
                case 2 :
                    pass
                case 3 :
                    pass
                    # Sequence parole pour ouverture de l'actualité
                    # Fonction pour afficher l'actualité
                case 4 :
                    self.__paroleRyley(listSortie[0])
                case 5 :
                    self.__paroleRyley(listSortie[0])
                case 6 :
                    pass
                    # Sequence parole pour ouverture d'erreur actualité
                case 7 :
                    self.__paroleRyley(listSortie[0])
                    self.setButtonOpen()
                case 8 :
                    self.__paroleRyley(listSortie[0])
                    self.setButtonOpen()
                case 9 :
                    pass
                    # Sequence parole pour lesture de fichier
                    # Fonction qui ouvre un fenetre pour lire le contenu du fichier
                case 10 :
                    self.__paroleRyley(listSortie[0])
                    # Fonction pour mettre affichier les bouton fichier
                case 11 :
                    pass
                    # Sequence parole pour erreur du resumer actualité
                case 12 :
                    pass
                    # Sequence parole pour reussite du resumer actualité
                    # Fonction qui crée pour afficher le resumer
                case 13 :
                    pass
                    # Sequence parole pour lesture d'un tableur
                    # Fonction qui ouvre un fenetre pour lire le contenu du fichier
                case 14 :
                    self.__paroleRyley(listSortie[0])
                    self.setButtonOpen()
                case 15 :
                    self.__close()
                case 16 :
                    self.__paroleRyley(self.__assistantRyley.shutdown())
                case 17 :
                    pass
                    # Ouverture d'un fenetre pour afficher l'aide
                case 18 :
                    pass
                    # Sequence parole pour reussite du resumer agenda et tache
                    # Fonction qui crée pour afficher le resumer
                case 19 :
                    pass
                    # Sequence parole pour reussite du resumer total
                    # Fonction qui crée pour afficher le resumer
                case 20 :
                    pass
                    # Sequence parole du resumer totale en erreur
                case 21 :
                    self.__paroleRyley(listSortie[0])
                    self.setButtonOpen()
                case other :
                    pass

    def keyboard(self):
        def anychar(event):
            if self.__windowsOS:
                if event.keycode == 13:
                    self.__envoi()
            else:
                if event.keycode == 36:
                    self.__envoi()
        self.__screen.bind("<Key>", anychar)

    def setButtonOpen(self):
        tableur = self.__assistantRyley.getTableur()
        word = self.__assistantRyley.getWord()
        projet = self.__assistantRyley.getProject()
        if tableur :
            self.__arrTK.placeTopRight(self.__btnTableurOpen)
        else :
            self.__btnTableurOpen.place_forget()

        if word:
            self.__arrTK.placeTopLeft(self.__btnWordOpen)
        else :
            self.__btnWordOpen.place_forget()

        if projet:
            self.__arrTK.placeTopCenter(self.__btnProjetOpen)
        else :
            self.__btnProjetOpen.place_forget()

        if tableur or word or projet :
            self.__disableAllFrame()
            self.__viewOpen()
        else :
            self.__disableAllFrame()
            self.__viewNormal()

    def __winHelpFileAndProjet(self, mode: int):
        """
        :param mode:
            1. Tableur
            2. Word
            3. Projet
        :return:
        """
        winHelp = self.__arrTK.aTopLevel(width=500, height=600,
                                         resizable=False,
                                         icon=self.__emplacementIcon)

        labelTitleHelp = self.__arrTK.createLabel(winHelp, ppolice="Arial", ptaille=25, pstyle="bold")
        aideView = self.__arrTK.createTextBox(winHelp, width=475, height=500,
                                              wrap="word", ppolice="Arial",
                                              ptaille=20, pstyle="normal")
        match mode:
            case 1:
                winHelp.title("Arrera Ryley : Aide Tableur")
                labelTitleHelp.configure(text="Aide Tableur")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpTableur()))
            case 2:
                winHelp.title("Arrera Ryley : Aide Traitement de texte")
                labelTitleHelp.configure(text="Aide Traitement de texte")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpWord()))
            case 3:
                winHelp.title("Arrera Ryley : Aide Arrera Projet")
                labelTitleHelp.configure(text="Aide Arrera Projet")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpProjet()))

        self.__arrTK.placeTopCenter(labelTitleHelp)
        self.__arrTK.placeCenter(aideView)

    def __traitementTextHelpFileAndProjet(self, liste:list):
        newText = ""
        for i in range(0, len(liste)):
            text = liste[i]
            if text[0] == "-" :
                text = text.replace("-", "").strip().lstrip()
                newText += "\n"+text+"\n"
            else :
                if text[0]== "*":
                    text = text.replace("*","").strip().lstrip()
                    newText += "    "+text+"\n"

        return newText.strip()