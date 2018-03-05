import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time

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

def sinus ():
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def triangle():
    t = np.linspace(0, 1, 500)
    triangle = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
    plt.plot(t, triangle)
    plt.show()

def square():
    t = np.linspace(0, 1, 500, endpoint=False)
    plt.plot(t, signal.square(2 * np.pi * 5 * t))
    plt.ylim(-2, 2)
    plt.show()

def main ():
    topic()
    R1,R2,C1,C2,U = userdefine()
    sinus()
    triangle()
    square()

main()

