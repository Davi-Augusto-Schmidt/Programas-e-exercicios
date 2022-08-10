print("Calculadora de assalto governamental")
x = int(input("Quanto Ganha por hora: "))
y = int(input("Quantidade horas trabalhadas: "))
s = x*y
ir = (s*11)/100
inss = (s*8)/100
sin = (s*5)/100
sl = s - ir - inss - sin
print ("Salario Bruto: R$", s)
print ("")
print ("Imposto de Renda: R$", ir)
print ("")
print ("INSS: R$",inss)
print ("")
print ("Sindicato: R$",sin)
print ("")
print ("Salario liquido: R$",sl)
