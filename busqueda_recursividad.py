""" Buscar la posicion de un numero en una lista ordenada crecientemente"""

def buscar_obj(lista, objetivo, inicio = 0):
    if not lista:
        return -1
    medio = len(lista) //2
    valor_medio = lista[medio]
    if  valor_medio == objetivo:
        return inicio + medio
    elif valor_medio < objetivo:
        return buscar_obj(lista[medio+1:], objetivo, inicio + medio +1)
    else:
        return buscar_obj(lista[:medio], objetivo, inicio)
