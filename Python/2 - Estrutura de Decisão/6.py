x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
z = int(input("Digite mais um numero: "))
if x > y > z:
    print ("O maior numero é ",x)
elif y > x > z:
    print ("O maior numero é ",y)
else:
    print("O maior numero é ",z)
