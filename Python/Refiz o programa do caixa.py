x = int(input("Digite o quanto quer sacar: "))

if 10 <= x <= 600:
    notas_cem = x//100
    notas_cin =(x%100)//50
    notas_dez = (x%50)//10
    notas_cinco = (x%10)//5
    notas_um = (x%5)//1

    print ("Você sacou",notas_cem," nota(s) de cem ,",notas_cin," nota(s) de cinquenta ,",notas_dez," nota(s) de dez , ",notas_cinco," nota(s) de cinco e ",notas_um, "nota(s) de 1")
else:
    print("Valor invalido")
