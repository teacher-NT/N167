import os
os.system("cls")

def salom_ber():
    print("Salom hammaga")

def func(a,b,c):
    d = a+b+c
    e = (a+b+c)/3
    f = a*b*c
    h = a-b-c
    return d, e, f, h

*n, m = func(5,6,7)
print(n, m)

