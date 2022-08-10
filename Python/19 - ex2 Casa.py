i = int(input("Digite I: "))
j = int(input("Digite J: "))
s = 1
n = 3
while n != 0:
    if i%s == 0 and j%s ==0:
        print("Divisor comum ",s)
        n = n - 1
        
    else:
        n = n + 1
    s = s + 1
