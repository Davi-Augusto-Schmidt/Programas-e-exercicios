n = int(input("Digite um numero de sequencias: "))

for i in range(n):
    print("Sequencia %i"%(i+1))
    num = int(input("Digite um numero:"))
    soma = 0
    while num != 0:
        if num % 2 == 0:
            soma = soma + num
        num = int(input("Digite um numero:"))

    print("A soma da sequencia %i é %i"%(i+1,soma))
