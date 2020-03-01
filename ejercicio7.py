def ejercicio7:
    cadenas = []
    n = int(input("Digite el tamaño o limte de su cadena: "))

    for i in range(n):
        i = input("dame una palabra: ")
        cadenas.append(i)

    print("\n")
    print("ya haz termiando de llenar la primera lista \n ahora, prosigue en llenar la segunda ")
    
    con = 0 
    for j in cadenas:
        
        j = input("dame una palabra")
        cadenas.insert(con,j)
        con = con +1
    
    print(cadenas)


ejercicio7()




    

