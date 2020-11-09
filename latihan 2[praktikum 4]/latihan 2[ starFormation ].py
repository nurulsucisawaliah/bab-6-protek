#starFormation1
def starFormation1(n):
    Kolom=0
    Baris=n

    i=0
    while(i<=n):
        j=0
        while(j<Kolom):
            print('*',end='')
            j+=1
        print('')
        i+=1
        Kolom+=1
#contohsF1
starFormation1(4)
print()

#starFormation2
def starFormation2(n):
    Kolom=n
    Baris=n

    i=0
    while(i<=n):
        j=0
        while(j<Kolom):
            print('*',end='')
            j+=1
        print('')
        i+=1
        Kolom-=1
#contohsF2
starFormation2(4)
print()

#starFormation3
def starFormation3(n):
    Kolom=0
    Baris=n
    Puncak=(n+1)/2

    i=0
    while(i<=n):
        j=0
        while(j<Kolom):
            print('*',end='')
            j+=1
        print()
        i+=1
        Kolom+=1

        if(Kolom == Puncak):
            Kolom=Puncak
            Baris=Puncak

            i=0
            while(i<=n):
                j=1
                while(j<=Kolom):
                    print('*',end='')
                    j+=1
                print()
                i+=1
                Kolom-=1
#contohsF3
starFormation3(7)
print()
