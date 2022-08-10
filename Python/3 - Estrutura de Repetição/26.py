print("Calculadora de eleições")
n = int(input("Digite o numero de eleitores: "))
c1 = 0
c2 = 0
c3 = 0
an = 0
for i in range(n):
    v = int(input("Quer votar em qual candidato 1, 2, 3 ou 4 para anular o voto: "))
    if v == 1:
        c1 =  c1 + 1
    elif v == 2:
        c2 = c2 + 1
    elif v == 3:
        c3 = c3 + 1
    elif v == 4:
        an = an + 1
    else:
        print("Numero invalido tente novamente")
        n = n + 1

print("A quantidade de votos para o candidato 1 é de %i"%c1)
print("A quantidade de votos para o candidato 2 é de %i"%c2)
print("A quantidade de votos para o candidato 3 é de %i"%c3)
print("")
if c1 > c2 and c1 > c3:
    print("O vencedor é o candidato 1!!!")
elif c2 > c1 and c2 > c3:
    print("O vencedor é o candidato 2!!!")
elif c3 > c1 and c3 > c2:
    print("O vencedor é o candidato 3!!!")
else:
    print("Eleição anulada")
print("")
print("A quantidade de votos anulados é de %i"%an)
