x = int(input("Digite um lado do triangulo: "))
y = int(input("Digite outro lado do triangulo: "))
z = int(input("Digite mais um lado do triangulo: "))

if x == y == z:
    print("triangulo equilatero")
elif x == y != z:
    print("triangulo Isósceles")
elif x == z != y:
    print("triangulo Isósceles")
elif y == z != x:
    print("triangulo Isósceles")
else :
    print("Triangulo escaleno")
