import random
lista = []

n = int(input("Digite o numero de lançamentos: "))
for i in range(n):
    lista.append(random.randint(1,6))
for i in range(1,7):
    print("A face %i apareceu %.2f%% vezes."%(i,100*lista.count(i)/n))
