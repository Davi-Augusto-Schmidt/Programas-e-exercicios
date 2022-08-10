print("Digite numeros positivos e menores que 16")
x = int(input("Digite um numero e eu o darei seu fatorial: "))
c = x
y = x - 1
if x > 16 or x < 0:
    print("Numero invalido")
else:
    while c != 1:
        x = x * y
        y = y - 1
        c = c - 1
print(x)
