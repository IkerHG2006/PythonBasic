def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

resultado16 = division_segura(10, 0)
print(resultado16)