def ejercicio7():
    cadenas = []
    primeracadena = []
    
    n = int(input("Digite el tamaño o limte de su cadena: "))
    if n > 0:

        for i in range(n):
            i = input("dame una cadena: ")
            cadenas.append(i)
            primeracadena.append(i)

        print("\n")
        print("ya haz termiando de llenar la primera lista \n ahora, prosigue en llenar la segunda ")
    
        con = 0 
        for j in range(len(cadenas)):
        
            j = input("dame una cadena: ")

            cadenas.insert(con,j)
            con = con +1
    
        print(f"La lista original es: {primeracadena} \n La segunda lista es: {cadenas}")
    
    else:
        print("el tamaño de la lista, debe ser mayor que cero ")



def ValidarEjercicio():
    correcto = False
    while (not correcto):
        try:
            ejercicio7()
            correcto = True

        except ValueError:
            print("la cantidad ingresada debe ser de tipo numérica y debe ser entera")



ValidarEjercicio()




    

