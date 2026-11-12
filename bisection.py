import numpy as np
import matplotlib.pyplot as plt
 
def bisection(f,a,b,e):
    fa = f(a)
    if f(a)*f(b)>= 0:
        print ("not possible")
    while (b-a)/2 > e:
        c = a+ (b-a)/2
        fc= f(c) 
        if fc== 0:
            return (c)
        if np.sign(fa) != np.sign(fc):
            b=c 
        else :
            a=c
    return (a+b)/2

print (lambda x: (x-1)**3,0.99,1.01,1e-10)    
