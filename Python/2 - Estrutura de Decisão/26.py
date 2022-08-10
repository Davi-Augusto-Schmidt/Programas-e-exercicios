print("DESCONTÃO NA GASOSA")
x = float(input("Digite (1) para gasolina ou (2) para alcool: "))
y = float(input("E quantos litros vai querer: "))
v = 0
if x == 1:
    if 0 < y < 21:
        v = 2.5*y
        d = (v * 4)/100
        vf = v - d
        print("Voce abasteceu ",y," litros, com o preço de R$ ",vf," com desconto de 4% ja aplicado")
    if y > 20:
        v = 2.5*y
        d = (v * 6)/100
        vf = v - d
        print("Voce abasteceu ",y," litros, com o preço de R$ ",vf," com desconto de 6% ja aplicado")
if x == 2:
    if 0 < y < 21:
        v = 1.9*y
        d = (v * 3)/100
        vf = v - d
        print("Voce abasteceu ",y," litros, com o preço de R$ ",vf," com desconto de 3% ja aplicado")
    if y > 20:
        v = 1.9*y
        d = (v * 5)/100
        vf = v - d
        print("Voce abasteceu ",y," litros, com o preço de R$ ",vf," com desconto de 5% ja aplicado")
