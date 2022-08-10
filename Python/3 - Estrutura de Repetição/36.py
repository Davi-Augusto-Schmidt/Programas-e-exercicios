td = int(input("Montar a tabuada de: "))
cp = int(input("Começar por: "))
te = int(input("Terminar em: "))
for i in range(cp,te+1,1):
    print(td,"X",i,"=",td*i)
