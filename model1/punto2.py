invertido = []

def inversion(lista):

    consonantes = ["b","c","d","f","g","h","j","k","l","m","ñ","p","q","r","s","t","v","w","x","y","z"]

    frase = [pal.split(" ")]

   

    for i in range(0, len(frase)):

        if frase[i][-1] not in consonantes:

            #print("Su palabra termina con una vocal, por ende no se invertirá su orden.")

            invertido.append(frase[i])

        else:

            #print("Su palabra termina con una consonante, por ende se invertirá su orden.")

            inve22rtido.append(frase[i][::-1])

    return invertido

temp = []

pal = input("Ingrese la frase que desee: ")

 

for i in range(0, len(pal)):

    temp.append(pal[i])

inversion(temp)

print(invertido)
