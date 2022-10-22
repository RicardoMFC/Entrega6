import math 
import sys

def introducir_radio():
    try:
        numero= float (input("Introduzca el radio\n"))
        while numero<=0:
            numero= float (input("Introduzca el radio\n"))
    except:
        pass
    else:
        return numero

def area_circulo(radio):
    pi=math.pi
    area=pi*pow(radio,2)
    return area

def main():
    radio=introducir_radio()
    area=area_circulo(radio)
    print (area)
main()