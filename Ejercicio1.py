import math  #Importo la librería math para utilizar el número pi y la función pow de su librería.
import sys   #Importo la librería sys para utilizar el try.

def introducir_radio():
    try:
        numero= float (input("Introduzca el radio\n"))
        while numero<=0:
            numero= float (input("Introduzca el radio\n"))
    except:
        pass
    else:
        return numero
#Defino una función introducir_radio para leer por pantalla el radio de la circunferencia, lo pido hasta que sea mayor que 0.

def area_circulo(radio):
    area=math.pi*pow(radio,2)
    return area
"""La función area_circulo, calcula el area del círculo, el único parámetro de entrada es el radio. La función pow permite elevar 
un valor al número que se desee."""

def main():
    radio=introducir_radio()
    area=area_circulo(radio)
    print (area)
main()
"""Desde la función main "función principal" llamo a la función introducir_radio, guardo lo que devuelve en la variable radio, que
va a ser el parámetro de entrada en la función area_circulo. Como esta última función nos a va a devolver algo, definimos una 
variable para llamarla, de esta manera nos guardará en esa variable lo que devuelva la función. Por último, mostramos por pantalla 
el valor del area"""


