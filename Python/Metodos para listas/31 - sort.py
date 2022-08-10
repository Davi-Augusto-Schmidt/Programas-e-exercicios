import random
lista = []
c = 10
while c != 0:
    c = c - 1
    a = random.randrange(0,1000)
    lista.append(a)

print("lista aleatoria")
print(lista)
print("lista em ordem")
lista.sort()
print(lista)
