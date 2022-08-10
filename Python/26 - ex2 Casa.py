vetori = []
vetorp = []
for i in range(1,21,1):
    num = int(input("Digite o %iº numero: "%i))
    if num%2==0:
        vetorp.append(num)
    else:
        vetori.append(num)
print("Os numeros pares são: ",vetorp)
print("Os numeros impares são: ",vetori)
    
