kosztyP = [3,3,3,4,4,4]
nominaly = [1,2,5]
wydaneMonety=[]
banknot = 30
lacznyKoszt = 0

for i in range(len(kosztyP)):
    lacznyKoszt = lacznyKoszt + kosztyP[i-1]

doWydania = banknot - lacznyKoszt
licznik = len(nominaly)-1

while doWydania > 0:
    while doWydania - nominaly[licznik] >=0:
        doWydania = doWydania - nominaly[licznik]
        wydaneMonety.append(nominaly[licznik])
    licznik=licznik-1

print("Ilość monet: " + str(len(wydaneMonety)))
print("Monety: " + str(wydaneMonety))