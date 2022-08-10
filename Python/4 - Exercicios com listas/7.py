lista = []
soma = 0
mult = 1
for i in range(1,6):
    x = int(input("Digite um número: "))
    soma += x
    mult *= x
    lista.append(x)
print("A soma dos números é de %i"%soma)
print("A multiplicação dos números é de %i"%mult)
print("")
print("E os numeros são")
print(lista)
