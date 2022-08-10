n = int(input("Digite um numero: "))
c = 0
for i in range(1,n+1):
    primo = True
    j = 2
    while j < i and primo:
        c = c + 1
        if i%j==0:
            primo = False
        j = j +1
    if primo == True:
        
        print(i)
print("Numero de divisões: %i"%c)
        
