
con1 = 0
con2 = 0
con3 = 0
con4 = 0
con5 = 0

def cantidadVocales(cadena):

    lista_cadena = list(cadena)
    

    for i in lista_cadena:
        if ((i ==  'a') or i ==  'A'   ):
            con1 = con1 + 1
        if ((i ==  'e') or i ==  'E'   ):
            con2 = con2 + 1
        if ((i ==  'i') or (i ==  'I'   ):
            con3 = con3 + 1

        if ((i ==  'o') or i ==  'O'   ):
            con4 = con4 + 1
        if ((i ==  'u') or i ==  'U'   ):
            con5 = con5 + 1

    print(f"la cantidad de (a) que hay en la cadena es de: {con1}")
    print(f"la cantidad de (e) que hay en la cadena es de: {con2}")
    print(f"la cantidad de (i) que hay en la cadena es de: {con3}")
    print(f"la cantidad de (o) que hay en la cadena es de: {con4}")
    print(f"la cantidad de (u) que hay en la cadena es de: {con5}")


def validar():
    correcto = False
    while(not correcto):
        try:
            cadena = input("Digite una cadena: ")
            cantidadVocales(cadena)
            correcto = True


        except ValueError:
            print("Debe ingresar una cadena")


def metodo2():
    cadena = input("digite la cadena")
    con1 = cadena.count("A") + cadena.count("a")
    print(con1)



metodo2()






