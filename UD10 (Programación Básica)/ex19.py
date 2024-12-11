def comptar_majuscules(cadena):
    count = 0
    for c in cadena:
        if 'A' <= c <= 'Z':
            count += 1
    return count