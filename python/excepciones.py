#concepto try/except

try:

    #a = 7 / 0

    b = int(input("Ingrese un numero "))

except ValueError:
    print("solo se pueden ingresar numeros")


except ZeroDivisionError:
    print("ups ocurrio un errror, el usuario intento dividir por cero")




print("adios")