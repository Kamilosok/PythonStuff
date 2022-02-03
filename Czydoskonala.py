import math
def czy_doskonala(n):
    suma=0
    i=2
    while i*i<n:
        if n%i==0:
            suma=suma+i+n/i
        i+=1
    if suma+1==n:
        return True
    else:
        return False
n=int(input())
print(czy_doskonala(n))
