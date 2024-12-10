def superposicio(llista1, llista2):
    return any(elem in llista1 for elem in llista2)

print(superposicio([1, 2, 3], [3, 4, 5]))
print(superposicio([1, 2, 3], [4, 5, 6]))  