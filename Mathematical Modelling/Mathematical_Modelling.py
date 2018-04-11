import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time
import math
from sympy import *
import os
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi
import pygame

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
            #sinus()
        elif wave == 't':
            a=1
            #triangle()
        elif wave == 'p':
            a=1
            #square()

    print()
    print ("Podaj dodatnie wartosci dla opornikow, kondensatorow i sily elektromotorycznej.")
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
    return  R1, R2, C1, C2, U, wave

def sinus (x, u, number, freq=1, ampl=1):
    t = [0,1,2,3,4,5,6,7,8,9,10]
    x.clear()
    t.clear()
    halfPeriod = 1/freq / 2
    fig = figure(1)
    ax1 = fig.add_subplot(211)
    ax1.grid(True)
    arg = (2 * math.pi) / 1000
    for i in range(2000):
        x.append(arg * i)
        t.append(ampl * math.sin(arg * freq * i))
    ax1.plot(x, t)

    t.clear()
    u.clear()
    ax2 = fig.add_subplot(212)
    arg = (2 * math.pi) / 1000
    for i in range(2000):
        u.append(arg * i)
        t.append(ampl * math.sin(arg * freq * i))
    ax2.plot(u, t)
    ax2.grid(True)
    ax2.set_ylabel('napiecie')
    ax2.set_xlabel('czas')
    ax1.set_ylabel('napiecie')
    ax1.set_xlabel('czas')
    if number==1:
        ax1.set_title('Biezace wartosci napiecia x1(t)')
    elif number==2:
        ax1.set_title('Biezace wartosci napiecia x2(t)')
    ax2.set_title('Wykres zewnetrznej sily elektomotorycznej U=u(t)')
    plt.tight_layout()
    show()

def triangle (x, u,number, freq=1, ampl=1):
    t = [0,1,2,3,4,5,6,7,8,9,10]
    x.clear()
    t.clear()
    halfPeriod = 1/freq / 2
    fig = figure(1)
    ax1 = fig.add_subplot(211)
    ax1.grid(True)
    for i in range(2000 * freq):
        x.append(i/(1000 * freq))
        t.append(((ampl * 2 / halfPeriod) * (halfPeriod - abs(x[i] % (2 * halfPeriod) - halfPeriod))) - ampl)
    ax1.plot(x, t)

    t.clear()
    u.clear()
    ax2 = fig.add_subplot(212)
    for i in range(2000 * freq):
        u.append(i/(1000 * freq))
        t.append(((ampl * 2 / halfPeriod) * (halfPeriod - abs(x[i] % (2 * halfPeriod) - halfPeriod))) - ampl)
    ax2.plot(u, t)
    ax2.grid(True)
    ax2.set_ylabel('napiecie')
    ax2.set_xlabel('czas')
    ax1.set_ylabel('napiecie')
    ax1.set_xlabel('czas')
    if number==1:
        ax1.set_title('Biezace wartosci napiecia x1(t)')
    elif number==2:
        ax1.set_title('Biezace wartosci napiecia x2(t)')
    ax2.set_title('Wykres zewnetrznej sily elektomotorycznej U=u(t)')
    plt.tight_layout()
    show()

def square (x, u,number, freq=1, ampl=1):
    t = [0,1,2,3,4,5,6,7,8,9,10]
    x.clear()
    t.clear()
    halfPeriod = 1/freq / 2
    fig = figure(1)
    ax1 = fig.add_subplot(211)
    ax1.grid(True)
    for i in range(2000 * freq):
        x.append(i/(1000 * freq))
        if i % 1000 <= 500:
            t.append(ampl)
        elif i % 1000 > 500:
            t.append(-ampl)
    ax1.plot(x, t)

    t.clear()
    u.clear()
    ax2 = fig.add_subplot(212)
    for i in range(2000 * freq):
        u.append(i/(1000 * freq))
        if i % 1000 <= 500:
            t.append(ampl)
        elif i % 1000 > 500:
            t.append(-ampl)
    ax2.plot(u, t)
    ax2.grid(True)
    ax2.set_ylabel('napiecie')
    ax2.set_xlabel('czas')
    ax1.set_ylabel('napiecie')
    ax1.set_xlabel('czas')
    if number==1:
        ax1.set_title('Biezace wartosci napiecia x1(t)')
    elif number==2:
        ax1.set_title('Biezace wartosci napiecia x2(t)')
    ax2.set_title('Wykres zewnetrznej sily elektomotorycznej U=u(t)')
    plt.tight_layout()
    show()

def main ():
    a=0
    while a==0:
        topic()
        R1,R2,C1,C2,U,wave = userdefine()
        x1,x2 = calculations(R1,R2,C1,C2,U)
        graphs(x1,x2,U,wave)
        print()
        repeat=input("Wpisz 'T' aby sprobowac od nowa: ")
        repeat=repeat.lower()
        if repeat != 't':
            break
        os.system("cls")
     
def calculations (R1,R2,C1,C2,U):

    print()
    print("Calculations: ")
    
    x = Symbol('x')
    #t = Symbol('t')
    tau = Symbol('tau')

    T1=R1*C1
    T2=R2*C2
    tau=R2*C1

    x1=[]
    x2=[]

    #macierze z modelu stanu
    ax1 = np.array([-(1/T1+1/tau), 1/tau])
    ax2 = np.array([[1/T2,-1/T2]])
    bx1 = np.array([1/T1])


    t=pygame.time.get_ticks()
    for i in range (10):
        x1.append(math.exp( ax1*t )*'x1(0)'*integrate(math.exp( ax1*(t-tau))*bx1*'u(tau)', (tau, 0, t)))
        x2.append(math.exp(ax2*t)*'x2(0)')
        #pygame.time.Clock.tick()
        print(t)
        t+=1

    x1a=x2a=1
    return x1a, x2a

def graphs(x1,x2,U,wave):
    print()
    print("Napiecia na kondensatorach prezentuja sie nastepujaco: ")
    print("(wykresy w nowych oknach)")
    time.sleep(2)

    x1=[1,2,3,4,5]
    x2=[1,2,3,4,5]
    U=[2,3,4,5,2,3,4,5]
    number=1
    if wave == 's':
        sinus(x1,U,number)
        number+=1
        sinus(x2,U,number)
    elif wave == 't':
        triangle(x1,U,number)
        number+=1
        triangle(x2,U,number)
    elif wave == 'p':
        square(x1,U,number)
        number+=1
        square(x2,U,number)

main()
