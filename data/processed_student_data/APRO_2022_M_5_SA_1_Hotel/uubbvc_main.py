class  Hotel: #Was gehört alles zum Hotel wird als Klasse definiert
    def __init__(self, name, sterne, stockwerke, zps, belegung):    #wie kann Anzahl Sterne bei Objektdefinition als int angegeben werden?
        self.name = name #self steht dabei als Referenz             #init für Eigenschaften des Objekts
        self.sterne = sterne
        self.stockwerke = stockwerke
        self.zimmmerProStockwerk = zps
        self.belegung = belegung

    def printInfo(self): #Funktion definieren für Informationen mit Namen und Sterne und Stockwerke
        print(self.name, " ", self.sterne) 
        #print(self.name, " ", "*"*self.sterne)
        zimmer = self.stockwerke * self.zimmmerProStockwerk #variable mit für Anzahl Zimmer, fixe zahl
        print(self.belegung, "von", zimmer, "belegt")

    def getGebuchteZimmer(self):
        freieZimmer= self.getMaxZimmer() - self.belegung
        return freieZimmer

    def getMaxZimmer(self):
        maxZimmer = self.stockwerke * self.zimmmerProStockwerk
        return maxZimmer

    def einchecken(self, i): #i von Buchungsanfrage steht für Anzahl Zimmmer
        if self.getGebuchteZimmer() >= i:
            self.belegung = self.belegung+i
            print("Sie können im ", self.name, " einchecken.")
            return True
        else:
            print("Das ", self.name, "hat nicht genügend Plätze frei!")
            return False

    def auschecken(self):
        if self.belegung > 0:
            self.belegung = self.belegung-1
            return True
        else:
            print("Es kann nicht ausgecheckt werden!")
            return False

h1=Hotel("Hotel Edelweiss", "***", 4, 10, 5)
#h1=Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2=Hotel("Hotel Astoria", "*****", 10, 20, 41)
h3=Hotel("Hotel Alpenblick", "***", 5, 6, 21)
h4=Hotel("Hotel Drei Könige", "**", 1, 4, 4)
h5=Hotel("Hotel Terminus", "*", 4, 10, 0)

#Ausgabe der Informationen zu den Hotels und Buchungsanfrage

buchungsanfrage = int(input("Wie viele Zimmer wollen Sie buchen?"))
'''
print("***********************************")
print()
h1.printInfo()
h1.einchecken(buchungsanfrage)
print()
h2.printInfo()
h2.einchecken(buchungsanfrage)
print()
h3.printInfo()
h3.einchecken(buchungsanfrage)
print()
h4.printInfo()
h4.einchecken(buchungsanfrage)
print()
h5.printInfo()
h5.einchecken(buchungsanfrage)
print()
'''

#Leute einchecken oder auschecken lassen
boa=int(input("Buchen oder Auschecken? (Buchen = 0; Auschecken = 1)"))
if boa == 0:
    buchen=int(input("In welches Hotel wollen Sie? (1=Edelweiss, 2=Astoria, 3=Alpenblick, 4=Drei Könige, 5= Terminus)"))
    print()
    if buchen == 1:
        if h1.einchecken(buchungsanfrage) == True:
            print(buchungsanfrage, " Zimmer im ", h1.name, "gebucht")
            h1.printInfo()  #zeigt zu viele belegte Zimmer an???
        else:
            print("Das ", h1.name, "hat nicht genügend freie Plätze")
    if buchen == 2:
        if h2.einchecken(buchungsanfrage) == True:
            print(buchungsanfrage, " Zimmer im ", h2.name, "gebucht")
            h2.printInfo()
        else:
            print("Das ", h1.name, "hat nicht genügend freie Plätze")
    if buchen == 3:
        if h3.einchecken(buchungsanfrage) == True:
            print(buchungsanfrage, " Zimmer im ", h3.name, "gebucht")
            h3.printInfo()
        else:
            print("Das ", h1.name, "hat nicht genügend freie Plätze")
    if buchen == 4:
        if h4.einchecken(buchungsanfrage) == True:
            print(buchungsanfrage, " Zimmer im ", h4.name, "gebucht")
            h4.printInfo()
        else:
            print("Das ", h1.name, "hat nicht genügend freie Plätze")
    if buchen == 5:
        if h5.einchecken(buchungsanfrage) == True:
            print(buchungsanfrage, " Zimmer im ", h5.name, "gebucht")
            h5.printInfo()
        else:
            print("Das ", h5.name, "hat nicht genügend freie Plätze")
#um auszuchecken, müsste einfach oben Geschriebenes verwendet werden, anstatt einchecken() halt auschecken() verwenden
#Die Überprüfung, ob genügend Zimmer frei sind oder nicht könnte im oberen Teil weggelassen werden, da es bereits im unteren Teil überprüft wird.
#Weshalb zeigt printInfo nun zu viele gebuchte Zimmer an?
