n = int(input("Digite o valor de n: "))
f = 1
for fator in range (2,n+1):
    f *= fator

print("%i! é igual a %i"%(n, f))
