"""
Escriure un programa que sumi tots els números entre dos números donats, ambdós inclosos.
x=int(input("Escriu el menor: "))
y=int(input("Escriu el major: "))
suma=0
for i in range(x,y+1,1):
    suma+=i
print(suma)
"""

x=int(input("Escriu el menor: "))
y=int(input("Escriu el major: "))
suma=0
for i in range(x,y+1,1):
    if i%2==0:
        suma+=i
print(suma)