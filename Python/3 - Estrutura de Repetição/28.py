print("Calculadora de valor")
c = int(input("Digite a quantidade de cds que possui: "))
s = 0
for i in range (c):
    v = float(input("Digite o valor do item: "))
    s += v
print("O valor da coleção é de: %.2f"%s)
