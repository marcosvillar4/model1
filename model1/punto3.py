import random

def rancart():
    numact = random.choice([1,2,3,4,5,6,7,10,11,12])
    paloact = random.choice(["Espada","Baston","Oro","Copa"])

    temp = [numact, paloact]

    return temp





#______________________________________________________________

cantj = 0
cartlist = []
arraycartas = []
check = False

while check != True:
    
    cantj = int(input("Cantidad de jugadores (2 - 6): "))
    
    if cantj >= 2 and cantj <= 6:
        check = True

check = False

for i in range(0, cantj):
    
    arrayjugador = []
    
    for i in range(0, 3):
        check = False 
        while check != True:
            
            temp = rancart()
            
            
            if temp in cartlist:
                check = False
            
            else:
                cartlist.append(temp)
                arrayjugador.append(temp)
                check = True
    
    arraycartas.append(arrayjugador)

for i in range (0, len(arraycartas)):
    
    print(f"Cartas jugardor {i + 1}: {arraycartas[i]}")
