n = int(input("Digite o tamanho da sequencia: "))
ant = 0
prox = 0
ant = int(input("Digite o primeiro numero: "))
c = cmax = 1
n = n - 1
while n != 0:
    n = n - 1
    prox = int(input("Digite o proximo numero: "))
    if prox > ant:
        c = c + 1
    
print("Sequencia crescente é de ",c)
