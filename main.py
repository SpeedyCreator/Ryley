from ryley import*

ryley = Ryley()
var = int(input("(1,2) : "))
match var :
    case 1 :
        ryley.bootAssistant()
    case 2 :
        ryley.bootCodeHelp()
    case 3 :
        ryley.bootPara()
    case other :
        print("Erreur")