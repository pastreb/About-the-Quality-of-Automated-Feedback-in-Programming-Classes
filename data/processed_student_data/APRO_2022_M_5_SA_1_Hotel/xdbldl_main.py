import numpy as np


class Hotel():
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung, maxi, freiezimmer):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    self.maxi = zimmer
    self.freiezimmer = freiezimmer
  
  def MaxZimmer(self, stockwerke, zimmerProStockwerke):
    self.maxi = self.stockwerke * self.zimmerProStockwerke
    
    
  def einchecken(self, ein):
    self.belegungen = self.belegungen + ein
    
    
  def auschecken(self, aus):
    self.belegungen = self.belegungen - aus
    
    
  def GebuchteZimmer(self, freiezimmer):
    self.freiezimmer = self.max - self.belegungen
    
    
  def status(status):
    if self.belegungen >= max:
      status = 0
    if self.belegungen < max:
      status = 1
    
  def printtitle(self):
    print("Hotel", self.name, "*" for range(self.sterne)
    print(self.belegungen, "von", self.maxi, "belegt")
  
  
  def printInfo(self):
    print(self.belegungen, "von", self.maxi, "belegt")
    if status = 0:
      print("Das Hotel ist voll, keine weiteren Belegungen möglich")
    if status = 1:
      print("Das Hotel ist frei, Belegungen sind möglich")
    print()
    
    
hot1 = Hotel( "Edelweiss", 3, 4, 10, 0, 0, 0)
hot2 = Hotel( "Astoria", 5, 10, 20, 0, 0, 0)
hot3 = Hotel( "Alpenblick", 3, 2, 15, 0, 0, 0)
hot4 = Hotel( "Drei Könige", 2, 2, 2, 0, 0, 0)
hot5 = Hotel( "Terminus", 1, 2, 20, 0, 0, 0)


hot1.MaxZimmer
hot1.printtitle()
ein = int(input("Wie viele checken ein? \n"))
hot1.einchecken(ein)
aus = int(input("Wie viele checken aus? \n"))
hot1.auschecken(aus)
hot1.GebuchteZimmer()
hot.status()
hot1.printInfo()
