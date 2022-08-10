a = int(input("Digite o numero de alunos:"))
for i in range(0,a):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3)/3
    print("para o aluno %i a média é de:%f"%(i+1,media))
    if media == 10:
        print("Aprovado com distinção")
    elif 7.0 < media < 9.0:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")
