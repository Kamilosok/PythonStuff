class kwadrat:
    def __init__(self, a):
        self._A=a
    def pole(self):
        print(self._A*self._A)
class trojkat(kwadrat):
    def __init__(self, a,h):
        kwadrat.__init__(self,a)
        self.__H=h
    def pole(self):
        print(self._A*self.__H/2)
K=kwadrat(2)
T=trojkat(2,4)
K.pole()
T.pole()
