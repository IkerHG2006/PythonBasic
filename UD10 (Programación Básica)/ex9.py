def sumar_llista(llista):
    return sum(llista)

def multiplicar_llista(llista):
    resultat = 1
    for element in llista:
        resultat *= element
    return resultat

print(sumar_llista([1, 2, 3, 4]))
print(multiplicar_llista([1, 2, 3, 4]))