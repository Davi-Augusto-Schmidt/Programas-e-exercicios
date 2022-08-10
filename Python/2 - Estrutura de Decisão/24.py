x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))
z= int(input("Digite (1) para impar ou par ,digite(2) para saber se é positivo ou negativo ou digite (3) para saber se e inteiro ou decimal: "))

i = 0
if z == 1:
    if x > 0:
        i = x%2
        if i == 0:
            print("O primeiro é Par")
        if i != 0:
            print("O primeiro é Impar")

    if y > 0:
        i = y%2
        if i == 0:
            print("O segundo é Par")
        if i != 0:
            print("O segundo é Impar")

if z == 2:
    if x%1==0:
        print("O primeiro é Inteiro")

    if x%1!=0:
        print("O primeiro é Decimal")

    if y%1==0:
        print("O segundo é Inteiro")

    if y%1!=0:
        print("O segundo é Decimal")

if z == 3:
    if x > 0:
        print("O primeiro é positivo")
    if x < 0:
        print("O primeiro é negativo")
    if y > 0:
        print("O segundo é positivo")
    if y < 0:
        print("O segundo é negativo")


