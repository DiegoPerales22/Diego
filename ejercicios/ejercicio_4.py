ax= int(input("ingrese un numero para el punto ax: "))
ay= int(input("ingrese un numero para el punto ay: "))
bx= int(input("ingrese un numero para el punto bx: "))
by= int(input("ingrese un numero para el punto by: "))
cx= int(input("ingrese un numero para el punto cx: "))
cy= int(input("ingrese un numero para el punto cy: "))
import math
base= bx-ax
altura= cy-ay
hipotenusa= math.sqrt((altura*altura+base*base))
area= base*altura/2
perimetro= (base*base + altura*altura + hipotenusa*hipotenusa)
print(hipotenusa)
print("el perimetro es : ",perimetro)
print("el area es:", area)