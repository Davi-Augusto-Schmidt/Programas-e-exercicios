notas = []
média = 0
for i in range(1,5):
    nota = float(input("Digite a nota do %iº bimestre: "%i))
    média += nota
    notas.append(nota)
print("As notas do aluno são:")
print(notas)
print("E sua média é: %g"%(média/4))
