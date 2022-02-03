monety = [0,1000,1000,0,0,1000]
suma = 0
i=len(monety)-1
koszt=int(input(("Podaj koszt")))
while (suma<koszt):
    print(suma)
    if(monety[i]>0 and suma+i<=koszt):
        suma+=i
        monety[i]-=1
    else:
        i-=1
    if(i==0):
        print(("Nie można uzyskać takiej sumy"))
        break
print(monety)
print("Suma: " + str(suma))