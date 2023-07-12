#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:03:35 2022

@author: mariusschneider
"""

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostock, belegung):
    self.name=str(name)
    self.sterne=int(sterne)
    self.stockwerke=int(stockwerke)
    self.zimmerprostock=int(zimmerprostock)
    self.belegung=int(belegung)     

     
  def getGebuchteZimmer(self):
      unbooked=(self.stockwerke*self.zimmerprostock)-self.belegung
      print(unbooked) 
      
      
  def getMaxZimmer(self):
      maximum=self.stockwerke*self.zimmerprostock
      print(maximum)
      
      
  def print_info(self):
      string=""
      for i in range(0,self.sterne):
          string=string+"*"
      print(self.name,string)
      print(self.belegung," von ", (self.stockwerke*self.zimmerprostock)," belget")
      print()

  def buchungsanfrage(self,anfr):
      string=""
      for i in range(0,self.sterne):
          string=string+"*"
      print(self.name,string)
      print("Anfrage für ",anfr," Zimmer")
      print(self.belegung," von ", (self.stockwerke*self.zimmerprostock)," belget")

      if self.belegung==(self.stockwerke*self.zimmerprostock):
          print("Das Hotel ",self.name," nicht buchbar belegt")
      
      elif (self.stockwerke*self.zimmerprostock)-self.belegung<=anfr:
          print("Das Hotel ",self.name," ist nicht buchbar")
          print()
      else:
          print("Buchung im Hotel ", self.name, " möglich")  
          print()
          q=str(input("Möchten Sie Einchecken? [y]=yes [n]=no "))
          if q=="y":
              self.belegung=self.belegung+anfr
              print("Neue Belegung: ",self.belegung)
              print()
        
          elif q=="n":
              print("Buchung abgebrochen")

          else:
              print("error")


  def checkout(self):
      print("Aktuelle Belegung: ",self.belegung)
      x=int(input("Wie viele möchten Auschecken? "))
      self.belegung=self.belegung-x
      print("Neue Belegung: ",self.belegung)
      
      

hot1=Hotel("Edelweiss",3,3,20,15)
hot2=Hotel("Rössli",5,8,25,30)
hot3=Hotel("Sternen",1,2,3,4)
hot4=Hotel("Calanda",2,5,2,2)
hot5=Hotel("Schesaplana Hütte",1,2,25,22)

def abfrage():
    hot1.print_info()
    hot2.print_info()
    hot3.print_info()
    hot4.print_info()
    hot5.print_info()


def buchung_anfrage():   
    anfr=int(input("Anzahl Zimmer: "))    
    hot1.buchungsanfrage(anfr)
    hot1.checkout()


buchung_anfrage()

hot1.print_info()