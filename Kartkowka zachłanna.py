indeksy = [0, 1, 2 ,3, 4, 5]
wagi = [100, 200, 150, 100, 150, 50]
kalorie = [252, 205, 315, 441, 630, 126]
koszty = [2,2,2,3,3,3]
swapper =[0,0,0,0]
nominaly = [1,2,5]
licznik = 0
maxW = 500
zjedzonaW = 0
kosztB = 0
maxKoszt = 20
def bubbleSort():
    for licznik in range(len(indeksy)-1):
        for licznik in range (len (indeksy) - 1):
            if kalorie[licznik]/wagi[licznik]>kalorie[licznik+1]/wagi[licznik+1]:
                swapper[0] = kalorie[licznik+1]
                swapper[1] = wagi[licznik+1]
                swapper[2] = indeksy[licznik+1]
                swapper[3] = koszty[licznik+1]
                kalorie[licznik+1] = kalorie[licznik]
                wagi[licznik+1] = wagi[licznik]
                indeksy[licznik+1] = indeksy[licznik]
                kalorie[licznik] = swapper[0]
                wagi[licznik] = swapper[1]
                indeksy[licznik] = swapper[2]
                koszty[licznik] = swapper [3]
    print("Wagi: "+str(wagi))
    print("Kalorie: " +str(kalorie))
    print("Indeksy: " +str(indeksy))
#Sortowanie w zależności od wydajności kalorii do wagi

def obliczanieZjedzonaWK(zjedzonaW, kosztB):
    licznik = 5
    while maxW > zjedzonaW:
        while licznik>=0 and maxKoszt >= kosztB:
            if zjedzonaW + wagi[licznik] <= maxW and kosztB + koszty[licznik] <= maxKoszt:
                zjedzonaW = zjedzonaW + wagi[licznik]
                kosztB = kosztB + koszty[licznik]
            else:
                licznik=licznik-1
        licznik = 5
    kosztA=kosztB
    print("Maksymalna waga zjedzonych pączków: "+str(zjedzonaW))
    print("Koszt: " + str(kosztB))
    return kosztB
#Obliczanie maksymalnej zjedzonej wagi od najwydajniejszego pączka w dół i zapisywanie kosztów od każdego pączka

def ileMonetReszty(kosztB, maxKoszt):
    reszta = maxKoszt-kosztB
    licznik=len(nominaly)-1
    monety=0
    while reszta>0:
        if reszta - nominaly[licznik] >= 0:
            monety = monety+1
            reszta = reszta - nominaly[licznik]
        else:
            licznik = licznik-1
    print("Ilość monet reszty: " + str(monety))

#Obliczanie reszty

bubbleSort()
ileMonetReszty(obliczanieZjedzonaWK(zjedzonaW,kosztB), maxKoszt)