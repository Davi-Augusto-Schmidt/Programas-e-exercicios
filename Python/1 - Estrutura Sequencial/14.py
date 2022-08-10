print("Quanto é a multa que joão deve pagar?")
p = int(input("Quantos quilos tu pegou de peixe João? "))
if p < 50:
    print("Não tem multa para pagar")
else:
    p= p-50
    m = p*4
    print("O valor da multa é R$",m)
