x = int(input("Digite o primeiro numero "))
y = int(input("Digite o segundo numero "))
z = int(input("Digite o terceiro numero "))

if x > y > z:
    print(x,z)
elif x > z > y:
    print(x,y)
elif y > x > z:
    print(y,z)
elif y > z > x:
    print(y,x)
elif z > x > y:
    print(z,y)
else:
    print(z,x)
