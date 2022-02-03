class Person:   #Klasa rodzica ze stringiem
    A=str()     #Deklaracja zmiennej
    def __init__(self, a):  #Konstruktor
        self.A=a
class Byk(Person):  #Klasa dziecka
    pass    #Pass w środku, bo nic nie dodajemy
Osoba=Person("Mike")    #Tworzenie obiektu rodzica z konstruktorem
print(Osoba.A)  #Wypisywanie stringa
Kox=Byk("Chad") #Tworzenie obiektu dziecka z konstruktorem
print(Kox.A)    #Wypisywanie stringaw
