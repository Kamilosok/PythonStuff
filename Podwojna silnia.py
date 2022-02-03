def silnia2(a):
    if a<3:
        return a
    else:
        return silnia2(a-2)*a
print(silnia2(4))