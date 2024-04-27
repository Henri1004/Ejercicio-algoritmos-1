def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    palabra = ''.join(acentos.get(c, c) for c in palabra)
    if palabra == palabra[::-1]:
        return "Es palindromo"
    else:
        return "No palindromo"
