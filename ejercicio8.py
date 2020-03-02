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
    
    print(f"Los primeros {n} numeros de la serie fibonacci son: {numerosfibonacci}")
    
    
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
            print(j)
        j+= 1

        
    
    print(f"Los primeros {dato} numeros primos son: {primos}")





Nprimos()