from functools import reduce


def passar_a_numero(llista):
   return reduce(lambda x, y: x * 10 + y, llista)


llista = [3, 4, 1, 5]
print(passar_a_numero(llista))


passar_a_numero(llista)