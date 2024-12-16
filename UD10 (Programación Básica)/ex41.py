"""
Definir una funció crear_llista_fitxer() on llegeixi un fitxer i transformi cada paraula 
llegida en un element de la llista. Prova-la.


"""

def crear_llista_fitxer(nom):
    l=[]
    with open(nom,"r") as f:
        for line in f:
            l.append(line[:-1])
    return l

#Programa principal
l=crear_llista_fitxer("prova1.txt")
print(l)
