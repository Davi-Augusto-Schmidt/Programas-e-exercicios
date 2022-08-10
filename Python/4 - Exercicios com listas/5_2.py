par = []
impar = []
for i in range(1,21):
    num = int(input("Digite um número: "))
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
print("")
print("Os números pares são")
print(par)
print("")
print("Os numeros impares são")
print(impar)
