tempsemestral1 = []
tempsemestral2 = []
mes = []
s = 0
for i in range(1,13):
    temperatura = float(input("Digite a temperatura do média do mês %i: "%i))
    s += temperatura
    if i <= 6:
        tempsemestral1.append(temperatura)
    else:
        tempsemestral2.append(temperatura)
    mes.append(i)
    
print("1 - Janeiro, 2 - Fevereiro, 3 - Março, 4 - Abril, 5 - Maio, 6 - Junho")
print(tempsemestral1)
print("7 - Julho, 8 - Agosto, 9 - Setembro, 10 - Outubro, 11 - Novembro, 12 - Dezembro")
print(tempsemestral2)
print("A média de temperatura anual é de: %g"%(s/12))
