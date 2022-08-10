print("Calculo de impostos do seu salario")
s = int(input("Digite seu salario por hora: "))
h = int(input("Digite a quantidade de horas trabalhadas: "))
sb = s*h

if sb < 900:
    print("Isento de imposto de renda")
    INSS=(sb*10)/100
    print("O valor do seu INSS:", INSS)
    FGTS=(sb*11)/100
    print("O valor do seu FGTS:", FGTS)
    total = INSS + FGTS
    print("O total de descontos é de: ",total)
    print("Seu Salario liquido é de: ", sb - total)
    
elif sb >= 900 and sb < 1500:
    IR =(sb*5)/100
    print("O valor do seu imposto de renda é 5%: ", IR)
    INSS=(sb*10)/100
    print("O valor do seu INSS:", INSS)
    FGTS=(sb*11)/100
    print("O valor do seu FGTS:", FGTS)
    total = INSS + FGTS + IR
    print("O total de descontos é de: ",total)
    print("Seu Salario liquido é de: ", sb - total)

elif sb >= 1500 and sb < 2500:
    IR =(sb*10)/100
    print("O valor do seu imposto de renda é 10%: ", IR)
    INSS=(sb*10)/100
    print("O valor do seu INSS:", INSS)
    FGTS=(sb*11)/100
    print("O valor do seu FGTS:", FGTS)
    total = INSS + FGTS + IR
    print("O total de descontos é de: ",total)
    print("Seu Salario liquido é de: ", sb - total)

elif sb >= 2500:
    IR =(sb*20)/100
    print("O valor do seu imposto de renda é 20%: ", IR)
    INSS=(sb*10)/100
    print("O valor do seu INSS:", INSS)
    FGTS=(sb*11)/100
    print("O valor do seu FGTS:", FGTS)
    total = INSS + FGTS + IR
    print("O total de descontos é de: ",total)
    print("Seu Salario liquido é de: ", sb - total)

else:
    print("Numero invalido")
