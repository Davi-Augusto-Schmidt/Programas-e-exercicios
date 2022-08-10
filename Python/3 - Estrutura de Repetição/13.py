x = int(input("Digite a Base: "))
y = int(input("Digite o Expoente: "))

c = y - 1
z = x
while c != 0:
    c = c - 1
    x = x*z
print(x)
