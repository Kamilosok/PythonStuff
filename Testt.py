class kw:
    __a = int ()

    def pole(self):
        if self.__a>0:
            print("Pole kwadratu wynosi: ", end='')
            return(self.__a*self.__a)
        else:
            return("Podano złą wartość")

    def wpisz(self):
        print ("Podaj długosc boku kwadratu: ", end='')
        self.__a = int (input ())
    def __init__(self, a=1):
        self.__a = a


class tr:
    __a=int ()
    __h=int ()

    def pole(self):
        if self.__a>0 and self.__h>0 :
            print("Pole trójkąta wynosi: ", end='')
            return((self.__a*self.__h)/2)
        else:
            return("Podano złe wartości!")

    def wpisz(self):
        print("Podaj długość podstawy i wysokość trójkąta: ", end='')
        self.__a = int (input())
        self.__h = int (input())

    def __init__(self, a=1, h=1):
        self.__a=a
        self.__h=h



print("Jeśli chcesz obliczyć pole kwadratu wpisz 0, jeśli chcesz obliczyć pole trójkata wpisz 1: ", end='')
x=input()
if x=='1':
    objo=tr
    objo.__init__(objo)
    objo.wpisz(objo)
    print(objo.pole(objo))
elif x=='0':
    objo=kw
    objo.__init__(objo)
    objo.wpisz(objo)
    print(objo.pole(objo))
else:
    print("Podano złą wartość!")


