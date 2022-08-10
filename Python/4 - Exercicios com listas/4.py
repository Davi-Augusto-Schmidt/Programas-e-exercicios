consoante = []
vogal = []
c = 0
for i in range(1,11):
    x = str(input("Digite uma letra: "))
    if len(x)>= 2:
        print("Eu disse uma letra")
        break
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vogal.append(x)
    else:
        consoante.append(x)
        c = c + 1
print("O número de consoantes é de %i"%c)
print("E as consoantes são")
print(consoante)
