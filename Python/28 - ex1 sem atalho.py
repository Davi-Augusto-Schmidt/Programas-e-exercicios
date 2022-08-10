lista = []
num = int(input("Digite um número da sequencia: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequencia: "))

elemento = int(input("Digite um elemento a ser procurado: "))
cont = 0
for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1

print("O elemento %i aparece %i vezes"%(elemento,cont))
        
