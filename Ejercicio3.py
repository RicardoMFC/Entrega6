import sys

def pedir_peso():
    try:
        peso=float(input("Indique su peso en Kg\n"))
        while peso<=0:
            peso=float(input("Indique su peso en Kg\n"))
    except:
        pass
    else:
        return peso

def pedir_altura():
    try:
        altura=float(input("Indique su altura en metros\n"))
        while altura<=0:
            altura=float(input("Indique su altura en metros\n"))
    except:
        pass
    else:
        return altura

def IMC(peso, estatura):
    Imc=peso/pow(estatura,2)
    return Imc

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