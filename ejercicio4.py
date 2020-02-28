
def lista():

    datos= []
    unico=[]
    repetidos=[]
    comparacion=[]

    for i in range(5):
        valor = int(input("dame un numero"))
        datos.append(valor)

    
    for i in datos:
        if i not in unico:
            unico.append(i)
        else:
            if i not in repetidos:
                repetidos.append(i)
            
            

    print(f"repetidos: {repetidos}")
    print(f"unico: {unico}")




lista()


