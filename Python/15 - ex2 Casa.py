

seq = int(input("Digite o tamanho da sequencia: "))
cont = 0
soma = 0
while cont < seq:
    cont +=1
    num = int(input("Digite o {}º número: ".format(cont)))
    if num % 2 == 0:
        soma = num + soma
print("A soma dos números pares é: {}".format(soma))
