"""
Escriu un programa que ens indiqui tots els números primers entre 1 i 100 
i ens digui quants n’hi ha
"""

# for i in range(1,101):
#     if i%2!=0:



#     print(i)

"""def primers(max):
    print(1)
    for i in range(2, max+1):
        primer = True
        for j in range(2,i):
            if (i%j == 0):
                primer = False
        if primer:
            print(i)

primers(100)"""

for num in range(2, 101):
        primer = True
        for i in range(2,num):
                if num % i == 0:
                    primer = False
                    break
        if primer:
            print(num)