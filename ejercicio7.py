def ejercicio7():
    cadenas = []
    primeracadena = []

    n = int(input("Digite el tamaño o limte de su cadena: "))
    if n > 0:

        for i in range(n):
            i = input("dame una cadena: ")
            primeracadena.append(i)

        print("\n")
        a = input("Digite un caracter")

        for i in primeracadena:
            cadenas.append(a)
            cadenas.append(i)
        print(
            f"La lista original es: {primeracadena} \n La segunda lista es: {cadenas}")

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
