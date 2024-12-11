"""
Definir una funció crear_punts() que agafi una llista de números i 
que pinti per pantalla tants punts com el valor de cada número de la llista. 
Entre els elements de la llista, hi ha dhaver un salt de línia. 
Ex: crear_punts([2,3,4]) mostri per pantalla el següent:
..
...
....

"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l
def crear_punts(l):
    s="."
    for e in l:
        print("{} \n".format(s*e))
        s="."
#Programa principal
a = llegir_llista()
crear_punts(a)
