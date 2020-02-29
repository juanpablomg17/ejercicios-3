def SolicitarCadenas():
    n = int(input("digite la cantidad de palabras que desea ingresar: "))
    if n > 0:     
        cadenas = []

        for i in range(n):
            i = input("digite una palabra: ")
            adenas.append(i)

     
        palabra = input("digite la palabra que desea solicitar: ")
    
        print(f"la cantidad de veces que aparece la palabra: {palabra} en la lista es: {cadenas.count(palabra)}")
    else:
        print("debe introducir una cantidad positiva")

       

def validar():
    correcto = False
    while (not correcto):
        try:
            SolicitarCadenas()
            correcto = True



        except ValueError:
            print("Error, debe introducir un valor numérico")



validar()
        
