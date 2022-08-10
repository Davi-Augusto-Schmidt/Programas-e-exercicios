x = int(input("Digite um numero e eu o darei seu fatorial: "))
c = x
y = x - 1
while c != 1:
    x = x * y
    y = y - 1
    c = c - 1
print(x)
