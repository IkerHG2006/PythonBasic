def contar_valores_coincidentes(lista):
    return sum(1 for indice, valor in enumerate(lista) if indice == valor)

resultado3 = contar_valores_coincidentes([0, 2, 3, 3, 4])
print(resultado3)