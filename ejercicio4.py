
def lista():

    datos= []
    unico=[]
    repetidos=[]
   
    n = int(input("de qué tamaño desea su lista de números? "))

    for i in range(n):
        valor = int(input("dame un numero: "))
        datos.append(valor)

    for i in datos:
        if i not in unico:
            unico.append(i)
        else:
            if i not in repetidos:
                repetidos.append(i)
            
    for i in unico:
        if i in repetidos:
            unico.remove(i)

    print(f"repetidos: {repetidos}")
    print(f"unico: {unico}")

lista()


