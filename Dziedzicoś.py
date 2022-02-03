class Punkt:
    def _wpisz(self):
        i=bool(1)
        while i:
            try:
                self._x=int(input("Podaj pozycję x punktu: "))
                self._y=int(input("Podaj pozycję y punktu: "))
                i=0
            except ValueError:
                print("Błędna wartość!")
    def _wypisz(self):
        print("Współrzędne punktu to ("+str(self._x),",",str(self._y),")",sep='')
    def __init__(self,xx,yy):
        self._x=xx
        self._y=yy
class Kolo(Punkt):
    def _wpisz(self):
        print("(Koło)")
        Punkt._wpisz(self)
        i=bool(1)
        while i:
            try:
                self.r=int(input("Podaj promień koła: "))
                i=0
            except ValueError:
                print("Błędna wartość!")
    def _wypisz(self):
        print("(Koło)")
        Punkt._wypisz(self)
        print("Pole koła wynosi "+str(self.r*self.r*3.14))
    def _spr(self,pp):
        if (((pp._x-self._x)*(pp._x-self._x))+((pp._y-self._y)*(pp._y-self._y)))<=self.__r*self.__r: #Nie znalazłem dobrego algorytmu, więc placeholder
            print("Punkt znajduje się w kole")
        else:
            print("Punkt nie znajduje się w kole")

    def __init__(self,xx,yy,rr):
        Punkt.__init__(self,xx,yy)
        self.__r=rr
pop=Punkt(0,0)
pap=Kolo(0,0,0)
pop._wpisz()
pap._wpisz()
pop._wypisz()
pap._wypisz()
pap._spr(pop)