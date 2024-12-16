"""
Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té qualque element 
çduplicat o no, no s’ha de modificar la llista donada. Prova-la.

"""

def llegir_llista():
    # Prec: llista buida i llegeix del teclat paraules
    # Post: Retorna la llista llegida de paraules, la llista acaba en trobar un punt
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def hi_ha_duplicats(l):
    s = set(l)
    if len(l)==len(s):
        print("No hi ha duplicats")
    else:
        print("Hi ha duplicats")

#Programa Principal
l= llegir_llista()
hi_ha_duplicats(l)
