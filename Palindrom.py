print("Wpisz słowo, a sprawdzę czy jest palindromem ")
a=input()
i=0
I=len(a)-1
while i<=I:
    if a[i]!=a[I]:
        print("Słowo -" + a + "- nie jest palindromem")
        break
    else:
        print("Sprawdzam")
    i+=1
    I-=1
if i>=I:
    print("Słowo -" + a + "- jest palindromem")
