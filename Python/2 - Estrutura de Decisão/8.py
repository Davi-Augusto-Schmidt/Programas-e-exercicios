x = int(input("Valor do primeiro produto: "))
y = int(input("Valor do segundo produto: "))
z = int(input("Valor do terceiro produto: "))

if x<y<z:
    print("O primeiro é mais barato")
    
elif y<x<z:
    print("O segundo é mais barato")
    
else:
    print("O terceiro é mais barato")
