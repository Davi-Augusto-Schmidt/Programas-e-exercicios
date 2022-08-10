k = 1
p = 0
print("(1) Para sim e (2)Para não")
for i in range(5):
    if k == 1:
        x = int(input("Telefonou para a vítima? "))
        
    if k == 2:
        x = int(input("Esteve no local do crime? "))
        
    if k == 3:
        x = int(input("Mora perto da vítima? "))
        
    if k == 4:
        x = int(input("Devia para a vítima? "))
        
    if k == 5:
        x = int(input("Já trabalhou com a vítima? "))
        
    if x == 1:
        p = p + 1
            
    k += 1
    
if p == 0 or p == 1:
    print("Inocente")
if p == 2:
    print("Suspeito")
if p == 3 or p == 4:
    print("Cumplice")
if p == 5:
    print("Assassino")

print(p)
