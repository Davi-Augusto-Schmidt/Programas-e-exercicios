alunosap = []
malunoap = []
alunosre = []
for i in range(1,11):
    bim1 = float(input("Digite a nota do 1º bimestre do aluno %i: "%i))
    bim2 = float(input("Digite a nota do 2º bimestre do aluno %i: "%i))
    bim3 = float(input("Digite a nota do 3º bimestre do aluno %i: "%i))
    bim4 = float(input("Digite a nota do 4º bimestre do aluno %i: "%i))
    m = (bim1+bim2+bim3+bim4)/4
    if m >= 7.0:
        alunosap.append(i)
        malunoap.append(m)
        
    else:
        alunosre.append(i)
print("")
print("Alunos aprovados e suas médias")
print(alunosap)
print(malunoap)
print("")
print("Alunos reprovados")
print(alunosre)
