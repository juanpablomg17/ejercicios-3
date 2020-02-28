
def funcion1(cadena,letra):
   
    lista_cadena = list(cadena) 
    contador =0
    for i in lista_cadena:
        if (i == letra[0]):
             contador = contador + 1 
    print(f"La cantidad de veces que se repite la letra {letra[0]} es {contador}")


# def validar():
#     correcto = False
#     while (not correcto):
#         try: 
#              cadena = input("digite una cadena: ")
#              letra = input("digite la letra que desea consultar: ")
#              funcion1(cadena,letra)

#              correcto = True




#         except ValueError:
#             print("Debe digitar primera una cadena y despues un caracter de esa cadena")




def metodo2():
    
    cadena = input("digite la cadena: ")
    letra = input("digite la letra que desea consultar: ")
    print(f"La cantidad de veces que se repite la letra {letra} {cadena.count(letra)}")


metodo2()






        





