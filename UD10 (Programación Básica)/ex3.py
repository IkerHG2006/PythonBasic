import os


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
       return "No se puede dividir por cero."


def potencia(num1, num2):
   return num1 ** num2


def raiz_cuadrada(num1):
   if num1 >= 0:
       return num1 ** 0.5
   else:
       return "No se puede calcular la raíz cuadrada de un número negativo."


def calculadora():
   print("Calculadora")
  
   while True:
       print("\nSelecciona una operación:")
       print("1. Sumar")
       print("2. Restar")
       print("3. Multiplicar")
       print("4. Dividir")
       print("5. Potencia")
       print("6. Raíz cuadrada")
       print("7. Salir")


       operacion = input("Introduce el número de la operación que quieres hacer: ")


       if operacion == '7':
           print("Saliendo de la calculadora.")
           break


       if operacion in ['1', '2', '3', '4', '5', '6']:
           num1 = float(input("Introduce el primer número: "))
           if operacion in ['1', '2', '3', '4', '5']:
               num2 = float(input("Introduce el segundo número: "))
          
           if operacion == '1':
               resultado = sumar(num1, num2)
               print(f"La suma es: {resultado}")
           elif operacion == '2':
               resultado = restar(num1, num2)
               print(f"La resta es: {resultado}")
           elif operacion == '3':
               resultado = multiplicar(num1, num2)
               print(f"La multiplicación es: {resultado}")
           elif operacion == '4':
               resultado = dividir(num1, num2)
               print(f"La división es: {resultado}")
           elif operacion == '5':
               resultado = potencia(num1, num2)
               print(f"{num1} elevado a {num2} es: {resultado}")
           elif operacion == '6':
               resultado = raiz_cuadrada(num1)
               print(f"La raíz cuadrada de {num1} es: {resultado}")
       else:
           print("Operación no válida.")


       input("Presiona enter para continuar...")
       os.system("clear")


calculadora()