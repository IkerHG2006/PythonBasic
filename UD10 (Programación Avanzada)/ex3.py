def filtrar_per_letra(llista, lletra):
   return list(filter(lambda x: x.startswith(lletra), llista))


llista_paraules = ["maria", "manta", "peu", "mà"]
print(filtrar_per_letra(llista_paraules, 'p'))