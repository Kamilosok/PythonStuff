import time
def ile_wieza(n):
    print("Ilość miejsc na które może się przemieścić wieża=",end='')
    return(2*(n-1))


def ile_goniec(n,x,y):
    print("Ilość miejsc na które może się przemieścić goniec=",end='')
    return (min(x-1,y-1)+min(x-1,n-y)+min(n-x,n-y)+min(n-x,y-1))


def ile_krol(n,x,y):
    print("Ilość miejsc na które może się przemieścić król=", end='')
    if n>1:
        if (x==1 or x==n) and (y==1 or y==n):
            return 3
        elif (x==1 or x==n) or (y==1 or y==n):
            return 5
        else:
            return 8
    else:
        return 0


def ile_skoczek(n,x,y):
    l=0
    print ("Ilość miejsc na które może się przemieścić skoczek=", end='')
    if n>2:
        if x+2<n and y+1<n:
            l+=1
        if x+2<n and y-1>0:
            l+=1
        if y+2<n and x+1<n:
            l+=1
        if y+2<n and x-1>0:
            l+=1
        if x-2<n and y+1<n:
            l+=1
        if x-2<n and y-1>0:
            l += 1
        if y-2<n and x+1<n:
            l+=1
        if y-2<n and x-1>0:
            l+=1
        return l
    else:
        return 0


def ile_pionek(n,y):
    print ("Ilość miejsc na które może się przemieścić pionek=", end='')
    if n<2 or y==n:
        return 0
    if y!=1 or n==2:
        return 1
    if y==1 and n>2:
        return 2
def ile_hetman(n,x,y):
    print ("Ilość miejsc na które może się przemieścić hetman=", end='')
    return (2*(n-1))+(min(x-1,y-1)+min(x-1,n-y)+min(n-x,n-y)+min(n-x,y-1))




n=0
x=0
y=0
while n<=0:
    try:
        n=int (input("Podaj wymiar planszy, liczbę większą od 0: "))
    except ValueError:
        print("Zła wartość!")

while x<=0 or x>n:
    try:
        x=int (input("Podaj pozycję x, znajdującą się na planszy: "))
    except ValueError:
        print("Zła wartość!")

while y<=0 or y>n:
    try:
        y=int (input("Podaj pozycję y, znajdującą się na planszy: "))
    except ValueError:
        print("Zła wartość!")
for i in range (10):
    print(i)
print(ile_wieza(n))
print(ile_goniec(n,x,y))
print(ile_hetman(n,x,y))
print(ile_krol(n,x,y))
print(ile_skoczek(n,x,y))
print(ile_pionek(n,y))
time.sleep(4)