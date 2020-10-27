#
palabra = input("ingrese una palabra:")

print(palabra)

tam=len(palabra)
tam=tam-1
print("indice del 0 al",tam)

palabraInvertida = ""

for indice in range(tam,-1,-1):
    palabraInvertida=palabraInvertida + palabra[indice]

print(palabraInvertida)