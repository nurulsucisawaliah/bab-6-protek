def Faktorial(n):
    FaktorialN=1
    while(n>0):
        FaktorialN=FaktorialN*n
        n -=1
    return FaktorialN

def Kombinasi(a, b):
    C = a - b
    Hasil=Faktorial(a)/(Faktorial(b)*Faktorial(C))
    print(Hasil)

def Permutasi(a, b):
    C = a - b
    Hasil=Faktorial(a)/Faktorial(C)
    print(Hasil)

x=10
y=7
Permutasi(x,y)
