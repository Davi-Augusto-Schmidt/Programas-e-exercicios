
salarioi = float(input("Digite o salario inicial: "))
anodeinicio = int(input("Digite o ano em que o funcionario começou a trabalhar: "))
anoat = 2022
au1= (salarioi*1.5)/100
salarioi = salarioi + au1
anodeinicio = anodeinicio + 1
print("O aumento no ano %i do funcionario foi de %.2f"%(anodeinicio,au1))
print("O valor de seu salario foi para %.2f"%salarioi)
while anodeinicio != anoat:
    anodeinicio = anodeinicio + 1
    au2 = (salarioi*3)/100
    salarioi = salarioi + au2
    print("O aumento no ano %i do funcionario foi de %.2f"%(anodeinicio,au2))
    print("O valor de seu salario foi para %.2f"%salarioi)
