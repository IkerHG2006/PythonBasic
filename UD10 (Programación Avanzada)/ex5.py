def lista_a_diccionario(lista):
    return {valor: indice for indice, valor in enumerate(lista)}

resultado2 = lista_a_diccionario(['casa', 'cotxe', 'cadira', 'taula'])
print(resultado2)