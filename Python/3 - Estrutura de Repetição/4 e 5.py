print("Quanto tempo para o pais B ter mais pessoas que o pais A")
a = float(input("Digite o numero de pessoas do pais A: "))
pa = float(input("Digite a taxa de crescimento do pais A entre 1%-100%: "))
b = float(input("Digite o numero de pessoas do pais B: "))
pb = float(input("Digite a taxa de crescimento do pais B entre 1%-100%: "))
ano = 0
if pa > pb:
    print("Taxa de B tem que ser maior que A, reinicie o programa")

while b < a:
    ano = ano +1
    a = a + (a*pa)/100
    b = b +(b*pb)/100
print(a,b,ano)
