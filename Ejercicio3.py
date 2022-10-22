import sys      #Importo la librería sys para utilizar el try.

def pedir_peso():
    try:
        peso=float(input("Indique su peso en Kg\n"))
        while peso<=0:
            peso=float(input("Indique su peso en Kg\n"))
    except:
        pass
    else:
        return peso
"""Defino una función pedir peso, que va a guardar en una variable de tipo float el peso introducido por teclado, y lo va a 
preguntar mientras se menor o igual que 0"""

def pedir_altura():
    try:
        altura=float(input("Indique su altura en metros\n"))
        while altura<=0:
            altura=float(input("Indique su altura en metros\n"))
    except:
        pass
    else:
        return altura
"""Ahora creo otra función que va a leer por teclado la altura, que guardará en una variable de tipo float y que preguntará mientras 
sea menor o igual que 0"""

def IMC(peso, estatura):
    Imc=peso/pow(estatura,2)
    return Imc
"""Defino por último la función IMC que mediante los parámetros de entrada peso y altura, realizará el calculo del índice de masa 
corporal"""

def main():
    peso=pedir_peso()
    altura=pedir_altura()
    imc=IMC(peso,altura)

    if imc<18.50:
        print ("Bajo peso: imc < 18.5\n IMC={}".format(imc))
    elif imc<25.00:
        print ("Normal: imc>=18.5 and imc<25\nI MC={}".format(imc))
    elif imc<30.00:
        print ("Sobrepeso: imc>=25 and imc<30\n IMC{}".format(imc))
    else:
        print ("Obesidad: >=30\n IMC={}".format(imc))
main()
"""Mediante la función principal llamo a las otras funciones pedir_peso y pedir_estatura, que me devuelven dos valores que guardo
en dos variable peso y altura. Al llamar a la función IMC le paso esas dos variables que utiliza para el calculo. Después, devuelve
el índice de masa corporal que guardo en la variable imc. Dependiendo de que valor sea se imprimirá por pantalla si tiene un peso
por debajo de lo recomendable, por encima o si es normal"""