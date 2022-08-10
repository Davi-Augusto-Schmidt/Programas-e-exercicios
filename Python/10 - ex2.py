x = int(input("Quanto dinheiro quer sacar?"))
if 10 <= x <= 600:
    cem = x//100
    cin = (x%100)//50
    dez = (x%50)//10
    cinco = (x%10)//5
    dois = (x%5)//2
    um = (x%2)//1
    print("voce tirou" ,cem,"notas de 100, mais",cin," notas de 50, mais",dez,"notas de 10 e",cinco,"notas de 5", dois,"notas de 2 e",um,"nota de 1")
    
else:
    print("Valor indisponivel")
