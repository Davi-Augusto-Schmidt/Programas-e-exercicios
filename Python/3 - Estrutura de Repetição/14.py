imp = 0
par = 0
for i in range (10):
    x = float(input("Digite um numero: "))
    if x%2 == 0:
        par = par + 1
    else:
        imp = imp + 1
print(par," pares e ",imp," impares.")
