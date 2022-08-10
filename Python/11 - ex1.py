x = int(input("Coloque um numero de 1 a 7 e veja qual dia da semana é: "))
verifica = False
if x == 1:
    print("Domingo")
    verifica = True
if x == 2:
    print("Segunda")
    verifica = True
if x == 3:
    print("Terça")
    verifica = True
if x == 4:
    print("Quarta")
    verifica = True
if x == 5:
    print("Quinta")
    verifica = True
if x == 6:
    print("Sexta")
    verifica = True
if x == 7:
    print("Sabado")
    verifica = True

if verifica != True:
    print("Dia invalido")
    
