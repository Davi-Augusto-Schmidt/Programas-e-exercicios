x = float(input("Digite sua divida: "))
k = 10
y = x
print(" 1 de parcela com juros de 0 porcento no valor de ",x)
for i in range(1,13):
    if i%3 == 0:
        j = (y * k)/100
        vj = y + j 
        print(" %g de parcelas com juros de %g porcento no valor de %g.3 "%(i,k,vj))
        k = k + 5
