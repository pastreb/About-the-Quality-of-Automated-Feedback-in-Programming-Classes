
class hotel:
    #Initialisierung des Objektes (Reihenfolge wichtig):
    def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
        self.name = name
        self.sterne = sterne
        self.stockwerke = stockwerke
        self.zimmerProStockwerk = zimmerProStockwerk
        self.belegung = belegung
        self.anzahl_zimmer = self.stockwerke * self.zimmerProStockwerk
    
    #Werte selber eingeben:
    def hotel_eingabe(self):
        self.name=input("\nHotel Name:")
        self.sterne=input("\nAnzahl Sterne:")
        self.stockwerke=input("\nAnzahl Stockwerke:")
        self.zimmerProStockwerk=input("\nWieviele Zimmer gibt es auf jedem Stockwerk:")
        self.belegung=input("\nWieviele Zimmer sind belegt:")

    def getGebuchteZimmer(self):
       # In dieser Methode wird zurückgegeben, wie viele Zimmer in einem Hotel aktuell gebucht werden können.
        print("Anzahl Zimmer, die noch gebucht werden können:" , self.anzahl_zimmer - self.belegung)
        return self.belegung

    def getMaxZimmer(self):
       # In dieser Methode wird zurückgegeben, wie viele Zimmer im Hotel maximal gebucht werden können.
        print("Maximale Anzahl Zimmer ist: ", self.anzahl_zimmer)
        return self.anzahl_zimmer

    def einchecken(self):
    # In dieser Methode wird der Wert der Belegung um eins erhöht:
        if self.belegung < self.anzahl_zimmer:
            self.belegung = self.belegung + 1
            return True
        else:
            print(self.name, ": ist leider voll.")
            return False
    
    # Ist die Maximalbelegung erreicht, kann nicht mehr eingecheckt werden (Rückgabewert:Boolean).

    def auschecken(self):
    # auschecken(): In dieser Methode wird der Wert der Belegung reduziert. Sind
    # keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden (Rückgabewert: Boolean).
        if self.belegung = 0:
            print(self.name, ": alle Zimmer sind frei.")
            return False
        else:
            self.belegung = self.belegung - 1
            print("bei " self.name, self.belegung" Zimmer noch verfügbar.") 
            return True

    def printInfo(self):
    # Mit dieser Methode wird der Name und die Anzahl der Sterne eines Hotels auf der Konsole ausgegeben.
    # Zudem wird angegeben, wie viele Zimmer das Hotel hat, und wie viele davon aktuell belegt sind.
    # Verwenden Sie dazu die Methoden getGebuchteZimmer() und getMaxZimmer().
        print ("")
        print ("****** HOTEL ******")
        print ("Hotel :",self.name, "  ",self.sterne, " Sterne")
        print (self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt")
       # print ("")

def main():

    # h1 = hotel() ; h2 = hotel(); h3 = hotel();  h4 = hotel(); h5 = hotel();
    h1 = hotel("Post", 2, 2, 4, 0)
    h2 = hotel("Miramare", 3, 3, 6, 0)
    h3 = hotel("Palace", 5, 5, 20, 0)
    h4 = hotel("bei Jonny"), 1, 2, 2, 0)
    h5 = hotel("Battello"), 4, 4, 6, 0)
    
    while (1):
        #Eine der 5 verschiedenen Möglichkeiten auswählen -> sehen dann "if":
        print("--------------------------------")
        print("1. Erstellen der Hotel-Objekten")
        print("2. Buchungsanfragen")
        print("3. Einchecken")
        print("4. Auschecken")
        print("5. EXIT")

        b=int(input("Was wünschen Sie machen?:"))
        if (b==1):
          # h1 = hotel() ; h2 = hotel(); h3 = hotel();  h4 = hotel(); h5 = hotel():
          # h1 = hotel("Post", 2, 2, 4, 0)
          # h2 = hotel("Miramare", 3, 3, 6, 0)
          # h3 = hotel("Palace", 5, 5, 20, 0)
            print(h1)
            print(h2)
            print(h3)
            print(h4)
            print(h5)
            
        #Aufrufen Methoden:
        if (b==2):
            h1.printInfo()
            h2.printInfo()
            h3.printInfo()
            h4.printInfo()
            h5.printInfo()
            
        if (b==3):
            
            print("EINCHECKEN, welches Hotel möchten Sie?:)
            print("1  ", h1.name, "  ", h1.stern)
            print("2  ", h2.name, "  ", h2.stern)
            print("3  ", h3.name, "  ", h3.stern)
            print("4  ", h4.name, "  ", h4.stern)
            print("5  ", h5.name, "  ", h5.stern)
            wunsch = int(input("Nummer eingeben zwischen 1-5: "))
            
            if wunsch == 1:
                print("Einchecken in: ", h1.name)
                h1.einchecken()
            elif wunsch == 2:
                print("Einchecken in: ", h2.name)
                h2.einchecken()
            elif wunsch == 3:
                print("Einchecken in: ", h3.name)
                h3.einchecken()
            elif wunsch == 4:
                print("Einchecken in: ", h4.name)
                h4.einchecken()
            else: 
                print("Einchecken in: ", h5.name)
                h5.einchecken()
            
              
        if (b==4):
            print("AUSCHECKEN, welches Hotel möchten Sie?:)
            print("1  ", h1.name, "  ", h1.stern)
            print("2  ", h2.name, "  ", h2.stern)
            print("3  ", h3.name, "  ", h3.stern)
            print("4  ", h4.name, "  ", h4.stern)
            print("5  ", h5.name, "  ", h5.stern)
            wunsch = int(input("Nummer eingeben zwischen 1-5: "))
            
            if wunsch == 1:
                print("Auschecken in: ", h1.name)
                h1.auschecken()
            elif wunsch == 2:
                print("Auschecken in: ", h2.name)
                h2.auschecken()
            elif wunsch == 3:
                print("Auschecken in: ", h3.name)
                h3.auschecken()
            elif wunsch == 4:
                print("Auschecken in: ", h4.name)
                h4.auschecken()
            else: 
                print("Auschecken in: ", h5.name)
                h5.auschecken()
            
              
        if (b==5):
            quit()

main()


    