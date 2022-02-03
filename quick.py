tab = [1,1,1,1,44,12,51,4,5,5,6,9,12]

def QuickSort(A,poczatek,koniec):     #ostatni element (-1)
    i = poczatek
    j = koniec
    m = A[(poczatek+koniec)//2]
    while i<=j:
        while A[i]<m : i+=1
        while A[j]>m : j-=1
        if i<=j:
            A[i],A[j] = A[j],A[i]
            i+=1
            j-=1
    if poczatek<j: QuickSort(A,poczatek,j)
    if i<koniec:QuickSort(A,i,koniec)
QuickSort(tab,0,len(tab)-1)
print(tab)
