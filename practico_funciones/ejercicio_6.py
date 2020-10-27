#
palabra=input("ingrese una frase:")

tam=len(palabra)
aux=tam-1

contador=0

for i in range(0,tam,1):
    print("palabra i:",palabra[i])
    print("palabra aux",palabra[aux])

    if(palabra[i]==palabra[aux]):
        print("son iguales")
        contador=contador+1
    else:
        print("no son iguales")

        aux=aux-1

if(contador==tam):
    print("es un palindromo")
else:
    print("false")
