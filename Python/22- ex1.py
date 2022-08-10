num = int(input("Digite o numero de temperaturas registradas: "))

soma = maior = menor = float(input("Digite a temperatura 1: "))

for i in range(2,num+1):
    temp = float(input("Digite a temperatura %i:"%i))
    
    if temp > maior:
        maior = temp
        
    if temp <  menor:
        menor = temp
        
    soma = soma + temp
    
print("A maior temperatura é: %.2fºC"%maior)
print("A menor temperatura é: %.2fºC"%menor)
print("A média das temperaturas é: %.2f ºC"%(soma/num))
