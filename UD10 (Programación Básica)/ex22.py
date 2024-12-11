"""
Definir una funció crear_repetits() que agafi un número enter i un caràcter i 
retorni el caràcter multiplicat pel número enter. Ex: crear_repetits(5, “a”), retorni “aaaaa”
"""

def crear_repetits(n,c):
    return c*n

#Programa principal
a= input("Introdueixi un caràcter: ")
b= int(input("Introdueixi el número de vegades que vol repetir el caràcter anterior: "))
print("El caràcter {} repetit {}-vegades és {}".format(a,b,crear_repetits(b,a)))
