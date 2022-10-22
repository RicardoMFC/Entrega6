import sys

def lee_numero():
    try:
        numero = float (input("Escriba un numero\n"))
    except:
        pass
    else:
        return numero

def mayor(x, y, z):
    if z>x and z>y:
        return z
    elif y>x:
        return y
    
    else:
        return x

def main():
    numero1=lee_numero()
    numero2=lee_numero()
    numero3=lee_numero()
    numero_mayor = mayor(numero1, numero2, numero3)
    print(numero_mayor)
main()