print("Programa de média aritmética")
a = int(input("Digite a quantidade de alunos: "))
for i in range(a):
    b1 = float(input("Digite a nota do Primeiro Bimestre: "))
    b2 = float(input("Digite a nota do Segundo Bimestre: "))
    b3 = float(input("Digite a nota do Terceiro Bimestre: "))
    b4 = float(input("Digite a nota do Quarto Bimestre: "))
    m = (b1 + b2 + b3 + b4)/4
    print("A média do aluno %i é: %f"%(i+1,m))
    if m > 7:
        print("Aprovado")
    else:
        print("Reprovado")
