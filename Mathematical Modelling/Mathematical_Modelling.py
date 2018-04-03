import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time
import math
from sympy import *

def topic ():
    print("Metody Modelowania Matematycznego - Projekt")
    print("Temat nr 7")
    print("Bartlomiej Borzyszkowski")
    print("Jan Michalik", '\n')

def userdefine ():
    print ("Podaj dodatnie wartosci dla opornikow, kondensatorow i sily elektromotorycznej")
    R1,R2,C1,C2=-1,-1,-1,-1
    try:
        while(R1<0):
            R1=float(input("R1: "))
        while(R2<0):
            R2=float(input("R2: "))
        while(C1<0):
            C1=float(input("C1: "))
        while (C2<0):
            C2=float(input("C2: "))
        U=float(input("U: "))
    except:
        print ("Podano bledna wartosc.")
        time.sleep(5)
        exit(0)
    print ("Wpisane wartosci są poprawne.")
    return  R1, R2, C1, C2, U

def sinus (x1,x2):
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def triangle (x1,x2):
    t = np.linspace(0, 1, 500)
    triangle = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
    plt.plot(t, triangle)
    plt.show()

def square (x1,x2):
    t = np.linspace(0, 1, 500, endpoint=False)
    plt.plot(t, signal.square(2 * np.pi * 5 * t))
    plt.ylim(-2, 2)
    plt.show()

def main ():
    topic()
    R1,R2,C1,C2,U = userdefine()
    x1,x2 = calculations(R1,R2,C1,C2,U)
    sinus(x1,x2)
    triangle(x1,x2)
    square(x1,x2)

def calculations (R1,R2,C1,C2,U):

    print()
    print("Calculations: ")
    
    Ra=1 #przykladowe na razie
    Rb=1 #przykladowe na razie
    a=1 #przykladowe na razie
     
    t = time.time() #time
    print ("time: ", t)

    I3=1 #przykladowe na razie
    I2=2 #przykladowe na razie

    R1=Ra+Rb*math.exp(-a*t)
    print("R1: ", R1)
    t = Symbol('t')
    
    x1=(1/C1)*integrate(I3,t) #1/C1* całka z I3 po dt, gdzie I3 to prąd plycący przez C1
    x2=(1/C2)*integrate(I2,t) # x2= #1/C2* całka z I2 po dt, gdzie I2 to prąd płynący przez R2 i C2

    print("Calka x1: ", x1)
    print("Calka x2: ", x2)

    return x1, x2

main()




