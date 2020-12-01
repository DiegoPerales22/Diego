rangoinicial=int(input("ingrese un numero inicial:"))
rangofinal=int(input("ingrese un numero final:"))
vectorrango=[]
vectorpares=[]
vectorimpares=[]
suma=0
for i in range(rangoinicial,rangofinal):
    vectorrango.append(i)

for o in vectorrango:
        if o%2==0:
            vectorpares.append(o)

for x in vectorrango:
        if x%2 !=0:
            vectorimpares.append(x)

print(vectorrango)
print(vectorpares)
print(vectorimpares)
