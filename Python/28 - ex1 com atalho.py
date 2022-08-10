lista = []
num = int(input("Digite um número da sequencia: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequencia: "))

elemento = int(input("Digite um elemento a ser procurado: "))


print("O elemento %i aparece %i vezes"%(elemento,lista.count(elemento)))
        
