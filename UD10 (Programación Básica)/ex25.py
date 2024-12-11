"""
Definir una funció gran_llista() que donada una llista de número ens retorni el més gran. 
Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10.
"""

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
def gran_llista(l):
    return max(l)
#Programa principal
a = llegir_llista()
print("El major de la llista {} és {}".format(a, gran_llista(a)))
