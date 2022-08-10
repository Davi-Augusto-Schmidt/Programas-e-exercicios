print("O metodo clear limpa a lista")
lista = []
for i in range(1,6):
    x = int(input("Digite um numero inteiro a ser acrescentado na lista: "))
    lista.append(x)

print("Essa é sua lista")
print(lista)
p = int(input("Quer limpar a lista?(1)sim ou (2)Não"))
if p == 1:
    lista.clear()
    print("Sua lista esta limpa ;-;")
    print(lista)
else:
    print("ainda bem que não limpou a lista")
