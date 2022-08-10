n = int(input("Digite N: "))
i = int(input("Digite I: "))
j = int(input("Digite J: "))
c = n
s = 0
while c != 0:
    
    if s % i == 0 or s % j == 0:
        print(s)
    else:
        c = c + 1
    
        
    s = s + 1
    c = c -1
