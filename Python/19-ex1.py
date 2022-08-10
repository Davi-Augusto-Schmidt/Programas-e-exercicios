print("Programa que verifica triangulo retangulo")
lado1=int(input("Digite o primeiro lado: "))
lado2=int(input("Digite o segundo lado: "))
lado3=int(input("Digite terceiro: "))
if lado1**2 + lado2**2 == lado3**2 or lado3**2 + lado1**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2:
    print("É um triangulo retangulo")
else:
    print("O triangulo não é retangulo")
