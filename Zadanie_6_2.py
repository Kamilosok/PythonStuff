alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plikw=open("wyniki_6_2.txt","w")
plik=open("dane_6_2.txt","r")
for i in range (3000):
    nalf=""
    a=0
    klucz=0
    tresc=plik.readline()
    znak=tresc[len(tresc)-2]
    while ord(znak)!=32:
        if a>0:
            klucz+=int(znak)*(10**a)
        else:
            klucz+=int(znak)
        a+=1
        znak=tresc[len(tresc)-2-a]
    klucz%=26
    nalf+=alf[klucz:]
    nalf=nalf+alf[:klucz]
    regula=str.maketrans(nalf,alf)
    wpisz=plikw.write(tresc[:len(tresc)-2-a].translate(regula)+"\n")
plik.close()
plikw.close()




