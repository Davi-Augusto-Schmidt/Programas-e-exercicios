import random

player_vida = 500
player_sp = 100
inimigo_vida = 50

n = int(input("Quantos inimigos você vai lutar contra: "))

inimigos = []

for i in range(n):
    inimigos.append([i+1,inimigo_vida])

jogando = True

while jogando:
    print("Vida:",player_vida)
    print("Mana:",player_sp)

    atk = int(input("Deseja atacar (1) ou curar (2): "))

    if atk == 1:
        selecionado = random.choice(inimigos)
        dano = random.randint(10,20)
        print("Causou %i de dano no inimigo %i!"%(dano,selecionado[0]))
        selecionado[1] -= dano

        if selecionado[1] <= 0:
            print("Inimigo %i morreu!"%selecionado[0])
            inimigos.remove(selecionado)
    else:
        if player_sp >= 10:
            cura = random.randint(10,15)
            print("Você recebeu %i de vida!"%cura)
            player_vida += cura
        else:
            print("Sp insulficiente!")
            
    for inimigo in inimigos:
        acertou = bool(random.choice([1,1,1,0]))
        if acertou:
            dano = random.randint(1,3)
            print("Inimigo %i causou %i de dano!"%(inimigo[0],dano))
            player_vida -= dano
        else:
            print("Inimigo %i errou o ataque!"%inimigo[0])

    if player_sp < 100:
        player_sp += 3
        
    if player_sp > 100:
        player_sp = 100

    if player_vida <= 0:
        print("!!!!!!!!!!!")
        print("Você Perdeu")
        jogando = False
    if len(inimigos) == 0:
        print("Parabens você ganhou o jogo!")
        jogando = False
        
