import linecache
alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nalf=""
k=107%26
plikw=open("wyniki_6_1.txt","w")
nalf+=alf[k:]
nalf=nalf+alf[:k]
regula=str.maketrans(alf,nalf)
for i in range(101):
    wiersz=linecache.getline("dane_6_1.txt",i)
    tresc=plikw.write(wiersz.translate(regula))
plikw.close()
print("Koniec")