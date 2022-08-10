import math

print("Calculadora de Baskara")
a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if a == 0 or b == 0 or c == 0:
    print("Programa encerrado")
    
delta = (b**2)-(4*a*c)
    
if delta < 0:
    print("A equação não possui raizes reais")
    
elif delta == 0:
    print("A equação  possui 1 raiz real")
    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
    print("Raiz 1 = " , raiz1)
elif delta > 0:
    print("A equação possui 2 raizes reais")
    
    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
    raiz2 = (-b - math.sqrt(delta) ) / (2*a)
    
    print("Raiz 1 = ",raiz1,",Raiz 2 = ",raiz2)
 
