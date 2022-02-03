alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nalf=""
plikw=open("wyniki_6_3.txt","w")
plik=open("dane_6_3.txt","r")
for i in range (3000):
    a=1
    nalf=""
    linia=plik.readline()
    slowo1=linia[:(len(linia)//2)-1]
    slowo2=linia[len(linia)//2:len(linia)-1]
    l=0
    while l<26:
        nalf=""
        nalf+=alf[l:]
        nalf+=alf[:l]
        regula=str.maketrans(alf,nalf)
        if slowo1[0].translate(regula)==slowo2[0]:
            break
        l+=1
    regula=str.maketrans(alf,nalf)
    while a<len(slowo1):
        if slowo1[a].translate(regula)==slowo2[a]:
            print(slowo1[a].translate(regula),slowo2[a])
            pass
        else:
            wpisz=plikw.write(slowo1+"\n")
            break
        a+=1
plik.close()
plikw.close()