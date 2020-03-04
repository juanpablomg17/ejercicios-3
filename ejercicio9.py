def ejercicio9():

    listaorigianl = []
    lista1 = []
    lista2 = []
    n = int(input("dame el tope de la lista: "))

    if n > 0: 

        for i in range(n):
            i = int(input("dame un número"))
            listaorigianl.append(i)

        for i in range(0,len(listaorigianl),1):
            if (i%2 == 0):
                lista1.append(i+1)
            else:
                lista1.append(i-1)
        print(lista1)

    else:
        print("la cantidad ingresada debe ser mayor que cero")



def validar():
    correcto = False
    while(not correcto):
        try:
            ejercicio9()
            correcto = True

        except ValueError:
            print("Error, el dato deber un número entero")


validar()
