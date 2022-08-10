jogadores = []
voto = 1
k = 0
while voto != 0:
    voto = int(input("Em qual jogador quer votar da camisa 1 até a 23? "))
    jogadores.append(voto)
    k += 1
    if voto == 0:
        k = k - 1 


print("O total de votos foi de %i"%k)
for i in range(1,24,1):
    print("O jogador %i recebeu %i votos"%(i,jogadores.count(i)))
    print("O jogador %i recebeu %.2f%% de votos"%(i,100*jogadores.count(i)/k))
    
