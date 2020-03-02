def ejercicio9():

    listaorigianl = []
    lista1 = []
    lista2 = []
    n = int(input("dame el tope de la lista: "))

    for i in range(n):
        i = int(input("dame un número"))
        listaorigianl.append(i)

    for i in range(0,len(listaorigianl),1):
        if (i%2 == 0):
            lista1.append(i+1)
        else:
            lista1.append(i-1)
    

    print(lista1)

ejercicio9()