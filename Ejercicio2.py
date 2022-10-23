import sys  #Importo la librería sys para utilizar el try.

def lee_numero():
    try:
        numero = float (input("Escriba un numero\n"))
    except:
        pass
    else:
        return numero
#La función lee_numero unicamente lee un numero de tipo float por teclado y lo devuelve a la función principal.

def mayor(num1, num2, num3):
    if num3>num1 and num3>num2:
        return num3
    elif num2>num1:
        return num2
    else:
        return num1
#La función mayor a partir de 3 parámetros de entrada que son 3 números, devuelve cual de esos numeros es mayor.

def main():
    numero1=lee_numero()
    numero2=lee_numero()
    numero3=lee_numero()
    numero_mayor = mayor(numero1, numero2, numero3)
    print("El numero mayor es el {}\n".format(numero_mayor))
main()
"""Desde la función principal llamamos 3 veces a lle_numero y cada vez que llamamos a la función nos devolverá un valor que
guardaremos en 3 variables distintas. Luego mandaremos estos valores a la función mayor como parámetros, esta nos devolverá cual
de ellos es el mayor"""