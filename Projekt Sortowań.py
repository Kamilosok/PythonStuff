def quicksort(tab):
    if(len(tab)<=1):
        return (tab)
    else:
        pivot=tab.pop()
    wieksze=[]
    mniejsze=[]
    for i in tab:
        if (i>pivot):
            wieksze.append(i)
        else:
            mniejsze.append(i)
    return quicksort(mniejsze)+[pivot]+quicksort(wieksze)


def mergesort(tab):
    if len (tab) > 1:
        mid = len (tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        mergesort (L)
        mergesort (R)
        i = j = k = 0
        while i < len (L) and j < len (R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1
        while i < len (L):
            tab[k] = L[i]
            i += 1
            k += 1
        while j < len (R):
            tab[k] = R[j]
            j += 1
            k += 1
        return (tab)


def heapify(tab, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tab[i] < tab[l]:
        largest = l

    if r < n and tab[largest] < tab[r]:
        largest = r

    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]  # swap

        heapify (tab, n, largest)


def heapsort(tab):
    n = len (tab)
    for i in range (n // 2 - 1, -1, -1):
        heapify (tab, n, i)

    for i in range (n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify (tab, i, 0)

    return (tab)


def countingsort(tab):
    max=0
    taB=[0]*(len(tab))

    for i in range(len(tab)):
        if(tab[i]>max):
            max=tab[i]

    numbers=[0]*(max+1)

    for i in range(len(tab)):
        numbers[tab[i]]+=1

    for i in range(1,len(numbers)):
        numbers[i]+=numbers[i-1]

    long=len(tab)-1

    while long>=0:
        taB[numbers[tab[long]]-1]=tab[long]
        numbers[tab[long]]-=1
        long-=1

    return taB


def shellsort(tab):
    n=len(tab)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = tab[i]
            j = i
            while j >= gap and tab[j - gap] > temp:
                tab[j] = tab[j - gap]
                j -= gap
            tab[j] = temp
        gap //= 2

    return (tab)


def choose(tab):
    print ("Jakim sortowaniem chcesz posortować tablicę?\n1.Quicksort\n2.Mergesort\n3.Heapsort\n4.Countingsort\n5.Shellsort")
    chooser=int(input())
    print(chooser)
    if (chooser == 1):
        print ("Wybrano Quicksort!")
        tab = quicksort (tab)
        print ("Posortowana tablica: ")
        return tab
    else:
        if (chooser == 2):
            print ("Wybrano Mergesort!")
            tab = mergesort (tab)
            print ("Posortowana tablica: ")
            return tab
        else:
            if (chooser == 3):
                print ("Wybrano Heapsort!")
                tab = heapsort (tab)
                print ("Posortowana tablica: ")
                return tab
            else:
                if (chooser == 4):
                    print ("Wybrano Countingsort!")
                    tab = countingsort (tab)
                    print ("Posortowana tablica: ")
                    return tab
                else:
                    if (chooser == 5):
                        print ("Wybrano Shellsort!")
                        tab = shellsort (tab)
                        print ("Posortowana tablica: ")
                        return tab
                    else:
                        print ("Wybrano złą liczbę!")
                        choose(tab)


print("Proszę podać rozmiar tablicy która będzie wpisywana")
size=int(input())
tab = []
for i in range(size):
    print("Proszę Podać "+str(i)+" element tablicy")
    tab.append(int(input()))

print("Nieposortowana tablica: "+str(tab))
print(choose(tab))