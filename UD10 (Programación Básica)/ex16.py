#Calcular la longitud d'una llista
def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a = input("Intro un número de la llista: ")
        if a!=".":
            l.append(int(a))
    return l
def longitud(l):
    i=0
    for e in l:
        i +=1
    return i
    #return len(l)

#Programa principal
x = llegir_llista()
print(longitud(x))
