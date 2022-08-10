import random

l1 = []
l2 = []
l3 = []
l4 = []
for i in range(1,31):
    x = random.randint(1,100)
    if i%3 == 0:
        l4.append(x)
        l3.append(x)
    elif i%2 == 0:
        l2.append(x)
        l3.append(x)
    else:
        l1.append(x)
        l3.append(x)
        
print("Lista 1")        
print(l1)
print("Tamanho da lista 1") 
print(len(l1))
print("Lista 2") 
print(l2)
print("Tamanho da lista 2")
print(len(l2))
print("Lista 3") 
print(l4)
print("Tamanho da lista 3")
print(len(l4))
print("Lista intercalada")
print(l3)
print(len(l3))
