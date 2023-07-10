# Hotelverwaltung

class Hotel:
    def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
        self.name = name
        self.sterne = sterne
        self.stockwerke = stockwerke
        self.zimmerProStockwerk = zimmerProStockwerk
        self.belegung = belegung

    def printInfo(self):
        # type: () -> which hotel
        print(self.name, 'hat', self.sterne * "*")
        print(self.getMaxZimmer() - self.getFreieZimmer(), "von", self.getMaxZimmer(),
              "sind belegt")


    # Zimmer die maximal im Hotel gebucht werden koennen
    def getMaxZimmer(self):
        return self.stockwerke * self.zimmerProStockwerk

    # Anzahl Zimmer die aktuell gebucht werden koennen
    def getFreieZimmer(self):
        return (self.stockwerke * self.zimmerProStockwerk) - self.belegung


    def einchecken(self, zimmer):
        if self.belegung + zimmer > self.getMaxZimmer():
            print("So viele Zimmer koennen wir leider nicht zur Verfuegung stellen.")
        else:
            self.belegung = self.belegung + zimmer
            print("Sie koennen im", self.name, "einchecken.")
            print("Sie haben", zimmer, "Zimmer im", self.name, "gebucht.")


    def auschecken(self, zimmer):
        if self.belegung - zimmer <= 0:
            print("Kein Auschecken moeglich")
        else:
            self.belegung = self.belegung - zimmer
            print("Es wurden" , zimmer , "ausgecket. Neu sind" ,  self.getFreieZimmer() , "Zimmer frei.")
    #methode objekt von altem kopieren
    def copy(self):
        neues_objekt =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung) #z.b an6=an3.copy >> an6 = Animals(an3.name, an3.gattung, an3.art, an3.gewicht, an3.laenge, an3.geschwindigkeit, an3.schutz)
        return neues_objekt



#Objekte initialisieren
hot1=Hotel("Hotel Edelweiss", 3, 4, 14, 30)
hot2=Hotel("Hotel Astoria", 5, 3, 4, 8)
hot3=Hotel("Hotel Alpenblick", 3, 2, 7, 11)
hot4=Hotel("Hotel Drei Koenige", 4, 4, 4, 16)
hot5=Hotel("Hotel Terminus", 2, 8, 6, 30)

#Buchungsanfragen und Check in
#zimmer = int(input("Wie viele Zimmer wollen sie belegen?"))
#print("Anfrage fuer", zimmer, "Zimmer im Hotel", hot1.name , ".")
#ot1.einchecken(zimmer)

#Check-out
#zimmerout = int(input("Wie viele Zimmer wollen sie auschecken?"))
#hot1.auschecken(zimmerout)

#???Buchungsanfragen und Check in
#zimmer = int(input("Wie viele Zimmer wollen sie belegen?"))
#x = str(input("Welches Hotel?"))
#wie dann von self.name auf hoti?

#???Informationen zu den Hotels
#hot1.printInfo()
#for i in range(1,6):
    #hoti.printInfo()

#Kopieren
hot6 = hot1.copy()
hot1.printInfo()
hot6.printInfo()
hot7 = hot6.copy()
hot7.printInfo()

