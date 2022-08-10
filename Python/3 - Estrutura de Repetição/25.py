print("Programa da terceira idade")
n = int(input("Quantas pessoas tem sua turma: "))
s = 0
for i in range(n):
    idade = int(input("Digite sua idade: "))
    s += idade

m = s/n
if m < 18:
    print("A média de pessoas são menores de idade")
elif m > 18 and m < 50:
    print("A média de pessoas são adultas")
    
else:
    print("A média de pessoas é idosa")
