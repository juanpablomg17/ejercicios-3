def serieFibonacci():
    numerosfibonacci = []

    n = int(input("digite el tope o tamaño de su lista"))

    a = 0
    b = 1
    c = 1
    p = 2
    valorar_primo = False

    for i in range(n):

        c = a + b
        a = b
        b = c
        numerosfibonacci.append(a)

    print(
        f"Los primeros {n} numeros de la serie fibonacci son: {numerosfibonacci}")


def Nprimos():
    primos = []
    dato = int(input("digite el tope o tamaño de su lista"))
    j = 2
    while j < dato:
        creciente = 2
        esprimo = True
        while esprimo and creciente < j:
            if j % creciente == 0:
                esprimo = False
            else:
                creciente = creciente + 1
            if esprimo:
                primos.append(j)
        j = j + 1

    print(f"Los primeros {dato} numeros primos son: {primos}")


def correr():
    
   correcto = False
   while(not correcto):
       try:
            print("Menú. \n 1. imprimir una lista de la serie fibonacci hasta n numeros \n 2. imprimir una lista de n numeros primos ")
            op = int(input(""))

            if (op == 1):
                serieFibonacci()
            if (op ==2):
                Nprimos()
            else:
                 print("Opción inválida")
            
            correcto = True
       except ValueError:
          print("Error, la cantidad ingresada debe ser de tipo numética")


correr()