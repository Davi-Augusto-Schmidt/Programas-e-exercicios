print("Programa que resolve equação de 2º grau")
a = float(input("Digite o valor de a: "))
if a == 0:
    print("Zero é um valor invalido, programa encerrado")
elif a != 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b**2) - (4*a*c)
    r1 =(-b + (delta**(1/2)))/(2*a)
    r2 =(-b - (delta**(1/2)))/(2*a)
    if delta < 0:
        print("A conta não possui raizes reais")
    elif delta == 0:
        print("A conta tem apenas uma raiz real")
        print("A unica raiz real é %f"%r1)
    elif delta > 0:
        print("A conta tem  2 raizes real")
        print("Que são %f e %f"%(r1,r2))
