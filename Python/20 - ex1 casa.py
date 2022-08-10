h = float(input("Digite a sua altura: "))
s = int(input("Digite o seu sexo (1)para feminino ou (2)para masculino: "))

if s == 1:
    pf = (62.1*h)-44.7
    pr = float(input("Digite seu peso: "))
    if pf == pr:
        print("Você tem o peso ideal")
    if pf < pr:
        print("Você esta acima do peso")
        print("Peso ideal é %f"%pf)
    else:
        print("Você esta abaixo do peso")
        print("Peso ideal é %f"%pf)
elif s == 2:
    pm = (72.7*h)- 58
    pr = float(input("Digite seu peso: "))
    if pm == pr:
        print("Você tem o peso ideal")
    if pm < pr:
        print("Você esta acima do peso")
        print("Peso ideal é %f"%pm)
    else:
        print("Você esta abaixo do peso")
        print("Peso ideal é %f"%pm)
