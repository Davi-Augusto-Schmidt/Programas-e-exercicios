print("Calculadora de média semestrais")
x = int(input("Nota do primeiro Bimestre: "))
y = int(input("Nota do segundo bimestre: "))
n = (x+y)/2
if n == 10:
    print("Aprovado com distinção!")
elif n > 7:
    print ("Aprovado")
else:
    print("Reprovado")
