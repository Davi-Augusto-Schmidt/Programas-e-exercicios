altura = []
idade = []

for j in range(1,6):
    a = float(input("Digite sua altura: "))
    i = int(input("Digite sua idade: "))
    altura.append(a)
    idade.append(i)
    
print("")
print("Ao contrario")
print("Alturas")
print(altura[::-1])
print("Idades")
print(idade[::-1])
