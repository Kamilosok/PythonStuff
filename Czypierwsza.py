import math
import linecache
def czy_pierwsza(a):
    if(a%1>0):
        return False
    if(a%2 == 0 or a < 2):
        return False
    for i in range(3,int(math.sqrt(a))+1,2):
        if(a % i == 0):
            return False
    return True
print(czy_pierwsza(int(input())))
