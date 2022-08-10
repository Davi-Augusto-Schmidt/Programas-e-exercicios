x = 0
a = 1
s = 0
nr = 0
nb = 0
notas = []
while x != -1:
    x = float(input("Digite a nota do aluno %i: "%a))
    if x > 0:
        a = a + 1
        s += x
        notas.append(x)
print("Foram lidos %i notas"%(len(notas)))
print("As notas foram")
print(notas)
print("As notas na ordem inversa")
notas.reverse()
print(notas)
print("A soma dos valores é de %g"%s)
print("A média dos valores é de %g"%(s/a))

for x in notas:
    if x < 6.9:
        nr = nr + 1
    else:
        nb = nb + 1

print("")
print("A quantidade de valores acima da média é de %i"%nb)
print("A quantidade de valores abaixo da média é de %i"%nr)
print("E boa tarde")
        
