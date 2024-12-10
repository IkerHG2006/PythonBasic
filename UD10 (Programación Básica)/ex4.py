import os

# Funcions bàsiques de la calculadora
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No es pot dividir per zero."

def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num1):
    if num1 >= 0:
        return num1 ** 0.5
    else:
        return "No es pot calcular la raíz quadrada d'un número negatiu."

# Funció per canviar bases
def canviar_base(num, base_actual, base_destí):
    try:
        num_decimal = int(str(num), base_actual)
        if base_destí == 2:
            return bin(num_decimal)[2:]
        elif base_destí == 8:
            return oct(num_decimal)[2:]
        elif base_destí == 10:
            return str(num_decimal)
        elif base_destí == 16:
            return hex(num_decimal)[2:]
        else:
            return "Base no suportada."
    except ValueError:
        return "Número o base no vàlid."

# Funcions addicionals
def gran(a, b):
    return max(a, b)

def gran_de_tres(a, b, c):
    return max(a, b, c)

def longitud(obj):
    return len(obj)

def es_vocal(caracter):
    return caracter.lower() in 'aeiou'

def sumar_llista(llista):
    return sum(llista)

def multiplicar_llista(llista):
    resultat = 1
    for element in llista:
        resultat *= element
    return resultat

def invertir(cadena):
    return cadena[::-1]

def es_palindrom(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == invertir(cadena)

def superposicio(llista1, llista2):
    return any(elem in llista1 for elem in llista2)

def crear_repetits(num, caracter):
    return caracter * num

def crear_punts(llista):
    for num in llista:
        print('.' * num)

def dibuixar_imatge():
    crear_punts([5, 3, 7, 2, 6])

# Funció principal de la calculadora
def calculadora():
    print("Calculadora")

    while True:
        print("\nSelecciona una operació:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potència")
        print("6. Raíz cuadrada")
        print("7. Canvi de base")
        print("8. Funcions addicionals")
        print("9. Sortir")

        operacion = input("Introdueix el número de l'operació que vols fer: ")

        if operacion == '9':
            print("Sortint de la calculadora.")
            break

        if operacion in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Introdueix el primer número: "))
            if operacion in ['1', '2', '3', '4', '5']:
                num2 = float(input("Introdueix el segon número: "))

            if operacion == '1':
                print(f"La suma és: {sumar(num1, num2)}")
            elif operacion == '2':
                print(f"La resta és: {restar(num1, num2)}")
            elif operacion == '3':
                print(f"La multiplicació és: {multiplicar(num1, num2)}")
            elif operacion == '4':
                print(f"La divisió és: {dividir(num1, num2)}")
            elif operacion == '5':
                print(f"{num1} elevat a {num2} és: {potencia(num1, num2)}")
            elif operacion == '6':
                print(f"La raíz quadrada de {num1} és: {raiz_cuadrada(num1)}")
        elif operacion == '7':
            num = input("Introdueix el número: ")
            base_actual = int(input("Introdueix la base actual (2, 8, 10, 16): "))
            base_destí = int(input("Introdueix la base de destinació (2, 8, 10, 16): "))
            print(f"El número en base {base_destí} és: {canviar_base(num, base_actual, base_destí)}")
        elif operacion == '8':
            print("\nFuncions addicionals:")
            print("1. Trobar el major de dos números")
            print("2. Trobar el major de tres números")
            print("3. Longitud d'una cadena o llista")
            print("4. Comprovar si és vocal")
            print("5. Sumar llista")
            print("6. Multiplicar llista")
            print("7. Invertir cadena")
            print("8. Comprovar si és palíndrom")
            print("9. Comprovar superposició de dues llistes")
            print("10. Crear repetits")
            print("11. Crear punts")
            print("12. Dibuixar imatge")

            sub_op = input("Selecciona una opció: ")

            if sub_op == '1':
                a, b = map(float, input("Introdueix dos números separats per espai: ").split())
                print(f"El major és: {gran(a, b)}")
            elif sub_op == '2':
                a, b, c = map(float, input("Introdueix tres números separats per espai: ").split())
                print(f"El major és: {gran_de_tres(a, b, c)}")
            elif sub_op == '3':
                obj = input("Introdueix una cadena o una llista (separada per comes): ")
                if ',' in obj:
                    obj = obj.split(',')
                print(f"La longitud és: {longitud(obj)}")
            elif sub_op == '4':
                char = input("Introdueix un caràcter: ")
                print(f"És una vocal: {es_vocal(char)}")
            elif sub_op == '5':
                llista = list(map(float, input("Introdueix els números de la llista separats per comes: ").split(',')))
                print(f"La suma és: {sumar_llista(llista)}")
            elif sub_op == '6':
                llista = list(map(float, input("Introdueix els números de la llista separats per comes: ").split(',')))
                print(f"El producte és: {multiplicar_llista(llista)}")
            elif sub_op == '7':
                cadena = input("Introdueix una cadena: ")
                print(f"Cadena invertida: {invertir(cadena)}")
            elif sub_op == '8':
                cadena = input("Introdueix una cadena: ")
                print(f"És palíndrom: {es_palindrom(cadena)}")
            elif sub_op == '9':
                llista1 = input("Introdueix la primera llista (separada per comes): ").split(',')
                llista2 = input("Introdueix la segona llista (separada per comes): ").split(',')
                print(f"Superposició: {superposicio(llista1, llista2)}")
            elif sub_op == '10':
                num = int(input("Introdueix un número: "))
                char = input("Introdueix un caràcter: ")
                print(crear_repetits(num, char))
            elif sub_op == '11':
                llista = list(map(int, input("Introdueix els números de la llista separats per comes: ").split(',')))
                crear_punts(llista)
            elif sub_op == '12':
                dibuixar_imatge()
            else:
                print("Opció no vàlida.")
        else:
            print("Operació no vàlida.")

        input("Prem enter per continuar...")
        os.system("clear")

if __name__ == "__main__":
    calculadora()
