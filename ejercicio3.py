def funcion1(cadena):
    print("Imprima los dos primeros caracteres")
    list(cadena)
    print(cadena[0:2])


def funcion2(cadena):
    print("Imprima los tres primeros caracteres")
    list(cadena)
    print(cadena[0:3])

def funcion3(cadena):
    print("Imprima la cadena cada dos caracteres")
    for i in range(0,len(cadena),3):
        print(cadena[i])


def funcion4(cadena):
    
    print("Imprima la cadena en sentido inverso")
    for i in range(len(cadena)-1,-1,-1):
        print(cadena[i])


cadena = input("digita la cadena: ")


funcion1(cadena)

funcion2(cadena)

funcion3(cadena)

funcion4(cadena)
