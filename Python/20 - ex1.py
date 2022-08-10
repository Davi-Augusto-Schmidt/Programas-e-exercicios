n = float(input("Digite um valor para n: "))
s = 0.0
i = 1
while n != 0:
    s = s + i/n
    i = i + 1
    n = n - 1

print("A soma vale:",s)
