vetor = []
s = 0
for i in range (1,11):
    x = int(input("Digite um número: "))
    vetor.append(x)
    s += x * x
print("A soma dos quadrados do vetor é de %i"%s)
print("E o a lista dos vetores é")
print(vetor)
