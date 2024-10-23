def calcula_pesos(lista):
    nova_lista = []
    
    for i, (nome, peso) in enumerate(lista):
        if len(lista) == 1:
            peso_modificado = peso * 4  
        elif i == 0:
            peso_modificado = peso * 2 
        elif i == len(lista) - 1:
            peso_modificado = peso * 3  
        else:
            peso_modificado = peso + lista[i - 1][1]  
        
        nova_lista.append((nome, peso_modificado))
    
    return nova_lista

objetos = [("maça", 5), ("objeto2", 10), ("objeto3", 20)]
print(calcula_pesos(objetos))
