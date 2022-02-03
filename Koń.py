alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nalf=""
print("Wpisz klucz ")
k=int(input())%26
nalf=nalf+alf[k:]
nalf=nalf+alf[:k]
regula=str.maketrans(alf,nalf)
h="AAAA"
print(h.translate(regula))
