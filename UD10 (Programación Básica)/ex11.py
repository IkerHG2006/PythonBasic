def invertir(cadena):
    return cadena[::-1]

def es_palindrom(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == invertir(cadena)

print(es_palindrom("radar"))
print(es_palindrom("Hola"))
print(es_palindrom("A man a plan a canal Panama")) 