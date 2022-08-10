x = float(input("Numero de moedas de cinco centavos: "))
y = float(input("Numero de moedas de dez centavos: "))
z = float(input("Numero de moedas de vinte e cinco centavos: "))
w = float(input("Numero de moedas de cinquenta centavos: "))
r = float(input("Numero de moedas de um real: "))

c =(x*5)+(y*10)+(z*25)+(w*50)+(r*100)

p = c/100

print ("O todal de dinheiro em reais é:",p )
