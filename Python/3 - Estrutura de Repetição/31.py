print("Digite 0 para parar de chamar produtos")
valor = soma = float(input("Digite o valor do produto 1: "))
n = 100       
for i in range (2,n):
    valor = float(input("Digite o valor do produto %g: "%i))
    soma += valor
    if valor == 0:
        print("Total foi de %.2f"%soma)
        din = float(input("Digite a quantidade de dinheiro pago: "))
        troco = din - soma
        print("O troco é de %.2f"%troco)
        print("Volte sempre")
        quit()
