n = int(input("Digite um numero: "))
c = 0
k = 1
e = 0
for i in range(n):
    if n%k == 0:
        c = c + 1
        print("%i é divisivel por %i"%(n,k))
    else:
        e = e + 1
    k = k + 1
if c > 2:
    print("O numero não é primo")
else:
    print("O numero é primo")
print("A quantidade de divisões falhas é de %i"%e)
