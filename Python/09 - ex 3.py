
mtq = int(input("Quantos metros quadrados quer pintar:"))
L = mtq//3
if mtq % 3 > 0:
        L = L + 1
        
Latas = L//18
if L % 18 > 0:
    Latas = Latas + 1
p = Latas*80
print("Voce precisa de", L ,"litros de tinta")
print("Você deve comprar",Latas,"lata(s) de tinta no valor de",p,"reais")
