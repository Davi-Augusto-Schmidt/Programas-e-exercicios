idades = []
alturas = []
ida = []
alt = []
s = 0

import random

for i in range(30):
    x = random.randrange(130,200)
    n = x/100
    s += n
    alturas.append(n)
    y = random.randrange(10,20)
    idades.append(y)
    if y >= 13 and x < 160:
        ida.append(y)
        alt.append(n)
        
m = s /30
print("Todas as Alturas são:")
print(alturas)
print("Todas as Idades são:")
print(idades)
print("A média de altura é de: %gm"%m)
print("Temos %i alunos com a média abaixo do normal"%(len(ida)))
print("A idade e altura e dos alunos com mais de 13 anos e com a altura abaixo da média")
print(ida)
print(alt)
