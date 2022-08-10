x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
z = int(input("Digite mais um numero: "))
if x > y > z:
    print("O maior e o menor são ",x," e ",z)
elif x > z > y:
    print("O maior e o menor são ",x," e ",y)
elif y > x > z:
    print("O maior e o menor são ",y," e ",z)
elif y > z > x:
    print("O maior e o menor são ",y," e ",x)
elif z > x > y:
    print("O maior e o menor são ",z," e ",y)
else:
    print("O maior e o menor são ",z," e ",x)
