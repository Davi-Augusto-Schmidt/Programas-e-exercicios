x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
z = int(input("Digite mais um numero: "))

if x > y > z:
    print(x,y,z)
    
elif x > z > y:
    print(x,z,y)
    
elif y > x > z:
    print(y,x,z)
    
elif y > z > x:
    print(y,z,x)
    
elif z > y > x:
    print(z,y,x)
    
else:
    print(z,x,y)
