n = str(input("Digite seu nome: "))
while ( len(n) <=  3 ):
	n=str(input("Digite um nome valido(Maior que 3 caracteres): "))
	
i = int(input("Digite sua idade: "))
while i>150 or i<0:
    i = int(input("Digite uma idade valida: "))

s = int(input("Digite seu salario: "))
while s < 0 :
    s = int(input("Digite um salario valido: "))
    
sx = str(input("Digite seu sexo (m) ou (f): "))
while sx != 'm' and sx != 'f':
   sx = str(input("Digite um sexo valido: "))

ec = str(input("Digite seu estado Civil(s,c,v ou d)): "))
while ec != "s" and ec != "c" and ec != "v" and ec != "d" :
    ec = str(input("Digite um estado Civil valido(s,c,v ou d)): "))
    
print("Nome:%s"%n)
print("Idade:%i"%i)
print("Salario:%i"%s)
print("Sexo:%s"%sx)
print("Estado Civil:%s"%ec)
