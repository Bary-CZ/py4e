#Základní program na vypočet výplaty!
#webhook přidán na discord!
def a() :
    z = input("jaký je měsíc?")
    korun = input("Kolik dostáváte kč za hodinu?")
    hodiny = input("kolik hodin jste odpracoval za tento měsíc?")
    výplata = int(korun) * int(hodiny)
    x = 'kč'
    y = "Toto je vaše výplata za měsíc " + z + " "  "bez dph"
    print (výplata,x,y)
a() #function můžeme použít vicekrát v kodu!
