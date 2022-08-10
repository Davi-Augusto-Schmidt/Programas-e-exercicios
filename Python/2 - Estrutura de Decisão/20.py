bim1 = int(input("Digite a nota do primeiro bimestre: "))
bim2 = int(input("Digite a nota do segundo bimestre: "))
bim3 = int(input("Digite a nota do tercero bimestre: "))
nota = (bim1 + bim2 + bim3)/3

if 9 > nota >= 7:
    print("Aprovado :", nota)
elif nota == 10:
    print("Aprovado com exelencia: ", nota)
else:
    print("Reprovado", nota)
