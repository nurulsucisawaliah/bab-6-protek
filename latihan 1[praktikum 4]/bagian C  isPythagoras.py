def isPythagoras(a,b,c):
    if((a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (a*a) + (b*b)):
        print(True)
    
    else:
        print(False)
isPythagoras(8,6,10)
