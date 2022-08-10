print("copy")
a = []
for i in range(1,6):
    x = int(input("Digite um numero:"))
    a.append(x)

print("lista criada")
print(a)
p = int(input("Desejaria fazer uma copia?(1)sim ou (2)não "))
if p == 1:
    b = a.copy()
else:
    print("Okay")

print("A lista A é: ",a)

if p == 1:
    print("A lista B é:",b)
