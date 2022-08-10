idades = []
alturas = []
s = 0
k = 0
for i in range(1,6):
    idade = int(input("Digite a idade do aluno %i: "%i))
    idades.append(idade)
    altura = float(input("Digite a altura do aluno %i: "%i))
    alturas.append(altura)
    s += altura
    m = s/5
    
    

for idade in idades:
    if idade > 13 and altura < m:
            k += 1

print("A quantidade de alunos com mais que 13 anos que estão abaixo da média de altura é de %i"%k)
