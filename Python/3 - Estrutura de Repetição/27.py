print("Programa que calcula a média de alunos por turma")
n = int(input("Digite a quantidade de turmas: "))
s = 0
for i in range(n):
    alunos = int(input("Digite a quantidade de alunos dessa turma: "))
    if alunos > 40:
        print("A turma não pode ter mais de 40 alunos")
        print("Digite novamente a quantidade de alunos")
        alunos = int(input("Digite a quantidade de alunos dessa turma: "))
        
    s += alunos
m = s/n 
print("A média de alunos por turma é de:%i"%m)
