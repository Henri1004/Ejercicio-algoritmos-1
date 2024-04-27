"""El codigo tomara una lista con tre colores, rojo, verde y azul, representado con "R","V" y "A" respectivamente, y devolvera la lista ordenada con los rojos a la izquierda, los
verdes en el centro y el azul a la derecha
"""
def ordenar_colores(lista_colores):
    for i in range(len(lista_colores)):
        for j in range(len(lista_colores)-i-1):
            if lista_colores[j] == "R":
                continue

            elif lista_colores[j] == "V":
                if lista_colores[j+1] == "R":
                    lista_colores[j] = "R"
                    lista_colores[j+1] = "V"
                else:
                    continue

            elif lista_colores[j] == "A":
                if lista_colores[j+1] == "V":
                    lista_colores[j+1] = "A"
                    lista_colores[j] = "V"
                elif lista_colores[j+1] == "R":
                    lista_colores[j+1] = "A"
                    lista_colores[j] = "R"
                else:
                    continue
    return lista_colores
a = ["R","A","A","V","R","R","V","V","R","A","R","A","R","R","V","R"]
print(ordenar_colores(a))
