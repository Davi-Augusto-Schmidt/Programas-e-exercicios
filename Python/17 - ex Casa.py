e = int(input("Digite o numero de eleitores: "))
ca,cb,cc = 0, 0, 0
for i in range(e+1):
    v = int(input("Qual candidato deseja votar A(1),B(2) ou C(3)? "))
    if v == "A" or v == "a" or v == 1:
        ca = ca + 1
    elif v == "B" or v == "b" or v == 2:
        cb = cb + 1
    elif v == "C" or v == "c" or v == 3:
        cc = cc + 1
print("Candidato A recebeu %i votos"%ca)
print("Candidato B recebeu %i votos"%cb)
print("Candidato C recebeu %i votos"%cc)
