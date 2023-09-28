cantpag = int(input("Cantidad de paginas: "))
cantcop = int(input("Cantidad de copias: "))
inter = []
for i in range(1, cantcop + 1):
    for j in range(1 , cantpag + 1):
        inter.append(j)
print(inter)
inter.sort()
print(inter)
