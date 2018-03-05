import numpy as np
import matplotlib as plt

def topic ():
    print("Metody Modelowania Matematycznego - Projekt")
    print("Temat nr 7")
    print("Bartlomiej Borzyszkowski")
    print("Jan Michalik", '\n')

def userdefine ():
    print ("Podaj dodatnie wartosci dla opornikow i kondensatorow")
    R1,R2,C1,C2=-1,-1,-1,-1
    while(R1<0):
        R1=float(input("R1: "))
    while(R2<0):
        R2=float(input("R2: "))
    while(C1<0):
        C1=float(input("C1: "))
    while (C2<0):
        C2=float(input("C2: "))
    return  R1, R2, C1, C2

def main ():
    topic()
    R1,R2,C1,C2 = userdefine()
    print(R1)

main()

