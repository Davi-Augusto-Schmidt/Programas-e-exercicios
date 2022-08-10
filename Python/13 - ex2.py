x = int(input("Digite a base de um numero: "))
y = int(input("Digite o expoente desse numero: "))

cont = 0
prod = 1
while cont < y:
    prod = prod * x
    cont = cont + 1
print(x ,"elevado a", y ,"é igual ao" ,prod)
