print("Calculadora de reajuste salarial")
salario = int(input("Digite o seu salario: "))

if salario <= 280:
    print("Seu Salario antes do reajuste",salario)
    x = (salario*20)/100
    print("Seu percentual de aumento é 20%")
    print("O seu aumento é de: ",x)
    print("Seu novo salario sera de: ",x + salario)
    
elif  salario < 280 or salario < 700  :
    print("Seu Salario antes do reajuste",salario)
    x = (salario*15)/100
    print("Seu percentual de aumento é 15%")
    print("O seu aumento é de: ",x)
    print("Seu novo salario sera de: ",x + salario)

elif  salario < 700 or salario < 1500 :
    print("Seu Salario antes do reajuste",salario)
    x = (salario*10)/100
    print("Seu percentual de aumento é 10%")
    print("O seu aumento é de: ",x)
    print("Seu novo salario sera de: ",x + salario)


elif salario > 1500 :
    print("Seu Salario antes do reajuste",salario)
    x = (salario*5)/100
    print("Seu percentual de aumento é 5%")
    print("O seu aumento é de: ",x)
    print("Seu novo salario sera de: ",x + salario)
    
else:
    print("Valor invalido")
