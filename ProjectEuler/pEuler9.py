import math as m
#Problem 9



for a in range(0,1000):
    for b in range(1,a):
        c = m.sqrt(a**2 + b**2)
        if c%1 == 0 and a+b+c==1000:
            print(f"(a,b,c)={a,b,c}")
            print(f"a*b*c={a*b*c}")
