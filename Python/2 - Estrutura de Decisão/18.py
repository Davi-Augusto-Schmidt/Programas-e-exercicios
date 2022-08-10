print("Programa verificação de data")
dia = int(input("Digite um dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
   if dia > 32:
       print("Dia inexistente")
   if ano > 2023:
       print("Ano inexitente")
   print("Dia ",dia," Mes ",mes," Ano ",ano)
if mes == 2:
    if dia > 29:
        print("Dia inexistente")
    if ano > 2023:
       print("Ano inexitente")
       
    print("Dia ",dia," Mes ",mes," Ano ",ano)
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
  
    print("Dia ",dia," Mes ",mes," Ano ",ano)
