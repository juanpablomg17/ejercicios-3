def ejercicio10():
    numeros = []
    numeros2 = []
    


    n = int(input("digite el tope de la lista"))
    if (n > 0):
        for i in range(n):
            i = int(input("dame un número: "))
            numeros.append(i)
    
        listaP = numeros
        print(f"la lista ingresada fue: {listaP}")

        numeros.pop(-1)

        j = int(input("digite el tope de la otra lista: "))
        numeros2 = numeros
    
        for i in range(j):
            i = int(input("dame otro número: "))
            numeros2.append(i)

 
        print(f"la nueva lista fue: {numeros2}")

    else:
        print("la cantidad introducida, debe ser mayor que cero")

    #hola mundo
   

def validar():
    correcto = False
    while (not correcto):
        try:
            ejercicio10()
            correcto = True


        except:
            print("Error, el dato debe ser de tipo numérico (entero)")
   
 

validar()