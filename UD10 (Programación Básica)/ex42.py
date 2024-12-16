"""
Definir una funció index_paraula() on donada una llista ordenada de paraules, 
ens retorni l’índex on es troba una paraula determinada 
o -1 en cas que no hi sigui
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

def index_paraula(l, paraula):
    if paraula not in l:
        return -1
    else:
        for i,e in enumerate(l):
            if e==paraula:
                return i

#Programa principal
l= llegir_llista()
p = input("Dir quina paraula de la llista vols cercar: ")
n=index_paraula(l,p)
if n>=0:
    print("La paraula {} està en la posició {}".format(p, n+1))
else:
    print("La paraula no està dins la llista")
