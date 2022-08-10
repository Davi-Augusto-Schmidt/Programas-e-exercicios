x = int(input("Digite (1)File duplo (2)Alcatra (3)Picanha: "))
y = float(input("Quantos quilos quer comprar dessa carne: "))
z = int(input("Tem cartão Tabajara? (1)Sim (2)Não: "))
pr = 0
d = 0
v = 0
pf = 0
if z == 1:
    if x == 1:
        pr = (4.9*y)
        d = (5*pr)/100
        pf = pr - d
        print("Comprou ", y ," quilos de File duplo pelo valor de  ",pr)
        print("MAS voce tem o cartão tabajara e vai ganhar 5% de desconto, seu desconto foi de R$ ",d)
        print("Então ira pagar R$ ",pf)
    if x == 2:
        pr = (5.9*y)
        d = (5*pr)/100
        pf = pr - d
        print("Comprou ", y ," quilos de Alcatra pelo valor de  ",pr)
        print("MAS voce tem o cartão tabajara e vai ganhar 5% de desconto, seu desconto foi de R$ ",d)
        print("Então ira pagar R$ ",pf)
    if x == 3:
        pr = (6.9*y)
        d = (5*pr)/100
        pf = pr - d
        print("Comprou ", y ," quilos de Picanha pelo valor de  ",pr)
        print("MAS voce tem o cartão tabajara e vai ganhar 5% de desconto, seu desconto foi de R$ ",d)
        print("Então ira pagar R$ ",pf)

if z == 2:
    if x == 1:
        pr = (4.9*y)
        print("Comprou ", y ," quilos de File duplo pelo valor de R$",pr)
        
    if x == 2:
        pr = (5.9*y)
        print("Comprou ", y ," quilos de Alcatra pelo valor de R$",pr)
        
    if x == 3:
        pr = (6.9*y)
        print("Comprou ", y ," quilos de Picanha pelo valor de  ",pr)

