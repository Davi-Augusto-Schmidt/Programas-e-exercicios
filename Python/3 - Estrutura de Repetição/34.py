n = int(input("Digite um numero: "))
x = 1
c = 0
d = 1
e = 0
for i in range(1,n):
    print(i)
    for j in range (x):
        print(j)
        if x%d == 0:
            c = c + 1
        
        else:
            e = e + 1
        
    d = d + 1
    x = x + 1
    if c <= 2:
        print("%i é primo"%x)
