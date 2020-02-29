def listaDeNumeros():
    numeros = []

    n = int(input("digite la capacidad que desea que tenga su lista: "))

    if n > 0:
        for i in range(n):
            i = int(input("dame un número: "))
            numeros.append(i)
    
        suma = 0 
        producto = 1
        mayor =0
        menor =0

        for i in numeros:
            suma = suma + i
            producto = producto * i

        if i < menor: 
            menor = i
    
        print(f"la suma es: {suma}")
        print(f"el producto es: {producto}")
        print(f"el mayor es: {max(numeros)}")
        print(f"el menor es: {min(numeros)}")
    else:
        print("la capacidad de su lista, debe ser una cantidad positiva")

            

def validar():
    correcto = False
    while (not correcto):
        try:
            listaDeNumeros()
            correcto = True


        except ValueError:
            print("Error, debe introducir datos numéricos")


validar()
