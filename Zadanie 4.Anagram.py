import linecache
import math
def czy_rowne(a,b,c,d,e):
    return len(a)==len(b)==len(c)==len(d)==len(e)

def czy_anagram(a,b,c,d,e):
    return sorted(a) == sorted(b) == sorted(c) == sorted(d) == sorted(e)


plik = "anagram.txt"
odpa = open("odp_4a.txt","w")
odpb = open("odp_4b.txt","w")
for i in range(200):
    s = linecache.getline(plik,i+1)
    w = s.split()
    if czy_rowne(w[0],w[1],w[2],w[3],w[4]):
        odpa.write(s)
        if czy_anagram(w[0],w[1],w[2],w[3],w[4]):
            odpb.write(s)
odpa.close()
odpb.close()
