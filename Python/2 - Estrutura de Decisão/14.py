x = int(input("Digite a nota do primeiro Bimestre: "))
y = int(input("Digite a nota do segundo Bimestre: "))
m = (x+y)/2

if  9 < m < 10:
    print("Nota A sua média é de: ",m," APROVADO")
    
elif  (7+1/2) < m < 9:
    print("Nota B sua média é de: ",m," APROVADO")
    
elif  6 < m < (7+1/2):
    print("Nota C sua média é de: ",m," APROVADO")
    
elif  4 < m < 6:
    print("Nota D sua média é de: ",m," REPROVADO")
    
elif  0 < m < 4:
    print("Nota E sua média é de: ",m," REPROVADO")
    
else:
    print("Nota invalida")
