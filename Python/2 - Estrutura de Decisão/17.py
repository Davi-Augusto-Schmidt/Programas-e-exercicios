print("Ver ano bissexto")
ano = int(input("Digite um ano com 4 digitos: "))

if (ano%4==0 and ano%100!=0) or (ano%400 == 0) :
    print("é bissexto")
else:
    print("Não é bissexto")
