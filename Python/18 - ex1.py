começo = int(input("Começo = "))
fim = int(input("Fim = "))
print("")
for i in range(começo, fim+1):
    print("Para o, ",i)
    for j in range(começo, fim+1):
        print("%iX%i = %i"%(i,j,i*j))

    print("")
