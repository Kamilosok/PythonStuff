Epsilon=0.000001
A=int(input("Proszę podać liczbę z której chcesz dostać pierwiastek kwadratowy"))
a=1
b=A
if(A>=0):
    while abs(a-b)>=Epsilon:
        a=(a+b)/2
        b=A/a
    print("Pierwiastek kwadratowy z "+ str(A) +" wynosi " + str(b))
else:
    print("Podano złą Liczbę!")