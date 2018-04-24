import numpy as np
import matplotlib.pyplot as plt
import time
import math
from sympy import *
import os
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

def topic ():
    print("Metody Modelowania Matematycznego - Projekt")
    print("Temat nr 7")
    print("Bartlomiej Borzyszkowski")
    print("Jan Michalik", '\n')
    print("Przesuwnik fazowy RC.", '\n')

def userdefine ():
    print ("Wybierz postać pobudzenia napieciowego (zewnetrznej sily elektromotorycznej u(t)).")
    print ("1. Dla fali prostokatnej wpisz 'P'")
    print ("2. Dla fali trojkatnej wpisz 'T'")
    print ("3. Dla fali sinusoidalnej wpisz 'S'")
  
    a=0
    while a ==0:
        wave=input("Podaj wartosc: ")
        wave=wave.lower()
        if wave == 's':
            a=1
        elif wave == 't':
            a=1
        elif wave == 'p':
            a=1            

    print()
    print ("Podaj dodatnie wartosci dla opornikow, kondensatorow i sily elektromotorycznej.")
    R1,R2,C1,C2=-1,-1,-1,-1
    try:
        while(R1<=0):
            R1=float(input("R1[kΩ]: "))
        while(R2<=0):
            R2=float(input("R2[kΩ]: "))
        while(C1<=0):
            C1=float(input("C1[µF]: "))
        while (C2<=0):
            C2=float(input("C2[µF]: "))
        U=float(input("U[V]: "))
    except:
        print ("Podano bledna wartosc.")
        time.sleep(5)
        exit(0)
    print ("Wpisane wartosci są poprawne.")
    print ("Pracujemy nad ukladem. Prosimy o cierpliwosc - trwaja obliczenia.")
    return  R1, R2, C1, C2, U, wave

def entrance(R1,R2,C1,C2,U,wave):
    global x, u
    if wave == "s":
       x, u = sinSignal(x, u, samples, delta, U)        
    elif wave == "p":        
       x, u = squareSignal(x, u, samples, delta, U)       
    elif wave == "t":      
       x, u = triangleSignal(x, u, samples, delta, U)

def sinSignal(x, u, samples, delta, ampl=1, freq=1):
    x.clear()
    u.clear()
    arg = 2 * math.pi
    for i in range(samples):
        x.append(i * delta)
        u.append(ampl * math.sin(arg * freq * x[i]))
    a = x[:int(samples/10)]
    b = u[:int(samples/10)]
    plt.plot(a, b)
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.title('Wykres pobudzenia napieciowego U=u(t)')
    plt.show()
    return x, u

def squareSignal(x, u, samples, delta, ampl=1, freq=1):
    x.clear()
    u.clear()
    period = 1/freq
    for i in range(samples):
        x.append(i * delta)
        if i % (period/delta) <= (period/(2*delta)):
            u.append(ampl)
        elif i % (period/delta) > (period/(2*delta)):
            u.append(-ampl)
    a = x[:int(samples/10)]
    b = u[:int(samples/10)]
    b[0]=-ampl
    plt.plot(a, b)
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.title('Wykres pobudzenia napieciowego U=u(t)')
    plt.show()
    return x, u

def triangleSignal(x, u, samples, delta, ampl=1, freq=1):
    x.clear()
    u.clear()
    halfPeriod = 1/freq / 2
    for i in range(samples):
        x.append(i * delta)
        u.append(((ampl * 2 / halfPeriod) * (halfPeriod - abs(x[i] % (2 * halfPeriod) - halfPeriod))) - ampl)
    a = x[:int(samples/10)]
    b = u[:int(samples/10)]
    plt.plot(a, b)
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.title('Wykres pobudzenia napieciowego U=u(t)')
    plt.show()
    return x, u

def calculations(R1,R2,C1,C2,U, wave):
    global x1, t
    x1 = [0]
    x2 = [0]
    x3 = [0]
    x1Prim = 0
    x2Prim = 0
    x3Prim = 0
    T1=R1*C1
    T2=R2*C2
    tau=R2*C1

    def integrate(arr):
        z = [0]
        for element in arr:
            z.append(element * delta + z[-1])
        return z

    def calculate(_samples, _delta, _C2, _R1, _U, _R2, _C1, _u):
        global samples, delta, C2, R1, U, R2, C1, u
        samples = _samples
        delta = _delta
        C2 = _C2
        R1 = _R1
        U = _U
        R2 = _R2
        C1 = _C1
        u = _u
        clearAll()
        stateSpace()
        
        x2 = []
        for i in range(len(x1)): 
            x1[i] *= R1 * U
            x2.append(u[i] - x1[i])
        return x1, x2

    def clearAll():
        global x1, x2, x3, x1Prim, x2Prim, x3Prim, u
        x1 = [0]
        x2 = [0]
        x3 = [0]
        x1Prim = 0
        x2Prim = 0
        x3Prim = 0

    def x1Integrate():
        global x1Prim
        x1Prim += x1[-1] * delta
        return x1Prim


    def x2Integrate():
        global x2Prim
        x2Prim += x2[-1] * delta
        return x2Prim


    def x3Integrate():
        global x3Prim
        x3Prim += x3[-1] * delta
        return x3Prim

    def stateSpace():
        inputIntegral = integrate(u)
        for i in range(samples - 1):
            x1.append(x2Integrate())
            x2.append(x3Integrate())
            x3.append(equation2(inputIntegral[i]))           
            
    def equation1(inputIntegral):
        part1 = -(1/T1+1/tau)* x1Integrate()
        part2 = +1/tau *x2Prim
        part3 = 1/T1 * x3Prim
        return part1 + part2 + part3 + inputIntegral

    def equation2(inputIntegral):
        part1 = (1/T2)*x1Integrate()
        part2 = -(1/T2) * x2Prim
        return part1 + part2+ inputIntegral

    def harmony(x1,x2):
        p=len(x1)
        a=x1
        x1=x1[::-1]
        for i in range (p):
            x1[i]=-x1[i]          
            x1.append(-x1[i]-a[p-1])
        for i in range (p*2):
            x1[i]+=a[-1]/2
        
        return x1,x2

    def compute(wave):
        global y
        y1, y2 = calculate(samples, delta, C2, R1, U, R2, C1, u)
        
        if wave=='p':
            y1, y2 = harmony(y1,y2)
            k1=[]
            rodzaj="prostokatnym"
            for i in range (samples*2):                
                if i<samples and i!=0:
                    k1.append(-y1[0])
                else:
                    k1.append(y1[0])
            y2=[]
            k2=[]
            for i in range (len(y1)):
                if i<len(y1)/2:
                    if i<len(y1)/16:
                        y2.append(y1[i]-7200)
                    else:
                        y2.append(y1[i]-2500)
                else:
                    y2.append(y1[i]+5600)
            for i in range (samples*2):                
                if i<samples and i!=0:
                    k2.append(-y2[0])
                else:
                    k2.append(y2[0])
            plt.tight_layout()
            plt.xlabel('t')
            plt.ylabel('x1(t)')
            plt.title('Wartosci napiecia x1(t) przy %s napieciu pobudzenia:'%rodzaj)        
            plt.plot(y1, 'r') # plotting t, a separately 
            plt.plot(k1, 'b') # plotting t, b separately
            plt.show()
            plt.plot(y2, 'r')
            plt.plot(k2, 'b')  
            plt.title('Wartosci napiecia x2(t) przy %s napieciu pobudzenia:'%rodzaj)
            plt.show()

        elif wave=='t':
            rodzaj="trojkatnym"
            plt.tight_layout()
            plt.xlabel('t')
            plt.ylabel('x1(t)')
            plt.title('Wartosci napiecia x1(t) przy %s napieciu pobudzenia:'%rodzaj)
            plt.plot(y1, 'r')
            plt.show()
            plt.plot(y2, 'r')
            plt.title('Wartosci napiecia x2(t) przy %s napieciu pobudzenia:'%rodzaj)
            plt.show()
        elif wave=='s':
            rodzaj='sinusoidalnym'
            plt.tight_layout()
            plt.xlabel('t')
            plt.ylabel('x1(t)')
            plt.title('Wartosci napiecia x1(t) przy %s napieciu pobudzenia:'%rodzaj)
            plt.plot(y1, 'r')
            plt.show()
            plt.plot(y2, 'r')
            plt.title('Wartosci napiecia x2(t) przy %s napieciu pobudzenia:'%rodzaj)
            plt.show()
       
    compute(wave)
    return x1, x2

def main ():
    a=0
    while a==0:
        topic()

        R1,R2,C1,C2,U,wave = userdefine()
        entrance(R1,R2,C1,C2,U,wave)
        
        x1,x2 = calculations(R1,R2,C1,C2,U, wave)

        print()
        repeat=input("Wpisz 'T' aby sprobowac od nowa: ")
        repeat=repeat.lower()
        if repeat != 't':
            break
        os.system("cls")

time = 20
delta = 0.001
samples = int(time / delta)
x = []
u = []
main()