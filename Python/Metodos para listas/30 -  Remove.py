lista = []
aux = []
n = int(input("Digite o numero de elementos da lista: "))
for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1,n)))
    lista.append(elemento)
    aux.append(elemento)
print(lista)

for ele in aux:
    aparições = lista.count(ele)
    for i in range(aparições-1):
        lista.remove(ele)
print(lista)
