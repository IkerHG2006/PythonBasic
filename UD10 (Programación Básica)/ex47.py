"""
Definir una funció elements_parells() que donada una llista de paraules, 
només ens mostri les que estan en la posició parell. Prova-la
"""

def llegir_llista():
    # Prec: llista buida i llegeix del teclat paraules
    # Post: Retorna la llista llegida de paraules, la llista acaba en trobar un punt
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def elements_parells(l):
    print(l[::2])

#Programa principal

l= llegir_llista()
elements_parells(l)
