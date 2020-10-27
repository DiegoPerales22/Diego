#
n1 = int(input("ingrese el primer numero:"))
n2 = int(input("ingrese el segundo numero:"))
n3 = int(input("ingrese el tercer numero"))

if n1 > n2 and n1 > n3:
    print("el numero mayor es el primer numero. Numero:",n1)
if n1 < n2 and n2 > n3:
    print("el numero mayor es el segundo. Numero:",n2)
if n1 < n3 and n3 > n2:
    print("el numero mayor es el tercer numero. Numero",n3)
else:
    print("todo los numeros son iguales")