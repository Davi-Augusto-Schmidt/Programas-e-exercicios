n = int(input("Digite o tamanho da sequencia maior que 2 por favor: "))
maior = 0
menor = 0
for i in range(n):
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
    elif num < maior:
        menor = num
print("O maior numero é %i e o menor numero é %i e a soma entre os dois é: %i"%(maior,menor,maior + menor))
    
