x = float(input("Quantos Kg de Maças quer comprar? "))
y = float(input("Quantos Kg de Morango quer comprar? "))
z = x+y
vr = (x*1.8)+(y*2.5)
if z > 8 or vr > 25:
    d = (10*vr)/100
    vr = vr - d
    print("Voce comprou mais de 8 quilos de fruta ou um valor acima de R$ 25 e ganhou 10% de desconto")
    print("Voce ganhou,", d ," reais de desconto pagando no final R$ ",vr)

else:
    print("O valor da sua compra é R$ ",vr )
