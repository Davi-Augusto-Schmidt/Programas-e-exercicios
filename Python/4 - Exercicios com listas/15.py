lista = []
listaaux = []
listaam = []
lista7 = []
k = 0
x = 0
while x != -1:
    x = int(input("Digite um numero: "))
    if x != -1: 
        lista.append(x)
        listaaux.append(x)
        k += 1
print("")
print("Você depositou %i números"%k)
print("E esses foram os números")
print(lista)
listaaux.reverse()
print("E esses foram os números postados na ordem inversa")
print(listaaux)
print("E essa é a soma dos números")
print(sum(lista))
print("E essa é a média dos números")
m = (sum(lista)/k)
print(m)

for i in lista:
    if i > m:
        listaam.append(i)
    if i < 7:
        lista7.append(i)
print("Os numeros acima da média")
print(listaam)
print("E a quantidade de numeros menores que 7 é de: ",(len(lista7)))
