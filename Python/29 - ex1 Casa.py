par = []
impar = []
x = 0
while x != -1:
    x = int(input("Digite um número(-1 para parar o programa): "))
    if x%2 == 0:
        par.append(x)
    else:
        impar.append(x)
print("Os números pares são:")
print(par)
