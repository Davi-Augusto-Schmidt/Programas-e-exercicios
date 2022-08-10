x = int(input("Digite um numero: "))
i = 0

if x > 0:
    i = x%2
    if i == 0:
        print("Par")
    if i != 0:
        print("Impar")
    
