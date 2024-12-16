"""
Definir una funció elimina_duplicats() 
que donada una llista ens retorni una nova llista sense elements duplicats.
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

def elimina_duplicats(l):
    s = set(l)
    return list(s)

#programa principal
l=llegir_llista()
r=elimina_duplicats(l)
print("La llista {} queda així {}".format(l,r))
