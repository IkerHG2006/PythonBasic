def numeros_potenciados(potencia, cantidad=10):
    return [i**potencia for i in range(cantidad)]

resultado6_cuadrado = numeros_potenciados(2)
print(resultado6_cuadrado)

resultado6_cubo = numeros_potenciados(3)
print(resultado6_cubo)