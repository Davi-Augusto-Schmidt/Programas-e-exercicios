num = int(input("Digite um numero: "))
i=1
while i + (i+1) + (i+2) < num:
    i = i + 1

if i + (i+1) + (i+2)  == num:
    print("É um numero perfeito")
else:
    print("Não é um numero perfeito")
