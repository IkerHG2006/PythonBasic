def concatenar_listas(lista1, lista2, conector):
    return [f"{a}{conector}{b}" for a, b in zip(lista1, lista2)]

# Ejemplo
resultado1 = concatenar_listas(['sub', 'supra'], ['campión', 'campiona'], '-')
print(resultado1)