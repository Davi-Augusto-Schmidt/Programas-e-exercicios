n = int(input("Digite o numero de empresas: "))
m = int(input("Digite o numero de meses: "))

e = 1
while e <= n:
    mes = 1
    ec = 0
    print("Empresa",e,":")
    while mes <= m:
        print("Mês", mes ,":")
        g = int(input("Digite o ganho da empresa: "))
        p = int(input("Digite o gasto da empresa: "))
        ec = ec + (g-p)
        print("")
        mes = mes + 1

    if ec == 0:
        print("Não teve lucro nem gasto")
    elif ec > 0:
        print("A empresa", e ," teve lucro de: ",ec,"R$")
    else:
        print("A empresa",e ," perdeu dinheiro:" ,ec,"R$")

    e = e + 1
    print("")
