from librairy.arrera_tk import CArreraTK
from ObjetsNetwork.arreraNeuron import *

VERSION = "I2025-1.00"

class guiRyley:
    def __init__(self, neuronConfigFile: str):
        # Boot ArreraTK
        self.__arrTK = CArreraTK()

        # Demarage Neuron Network
        self.__assistant = ArreraNetwork(neuronConfigFile)

        # Teste sur de l'OS hote
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        del objOS

        # Demarage de l'interface
        self.__screen = self.__arrTK.aTK(0,title="Ryley", resizable=False,
                                         width=500, height=600)

        # Creation des image de fond
        emplacementLight = "asset/GUI/light/"
        emplacementDark = "asset/GUI/dark/"

        listIMG = ["top.png", "bottom.png"]

        # Frame
        self.__topBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + listIMG[0],
                                                                      imageDark=emplacementDark + listIMG[0],
                                                                      width=500, height=400)
        self.__bottomBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                         imageLight=emplacementLight + listIMG[1],
                                                                         imageDark=emplacementDark + listIMG[1],
                                                                         width=500, height=200)
        # Widget
        entryUser = self.__arrTK.createEntry(self.__bottomBackgroup, ppolice="Arial", ptaille=25, width=300)

        btnSend = self.__arrTK.createButton(self.__bottomBackgroup, text="Envoyer",
                                            ppolice="Arial", ptaille=20,
                                            pstyle="bold", )


        # Affichage des widgets
        self.__arrTK.placeLeftCenter(entryUser)
        self.__arrTK.placeRightCenter(btnSend)

    def active(self):
        self.__topBackgroup.pack()
        self.__bottomBackgroup.pack()
        self.__arrTK.view()

