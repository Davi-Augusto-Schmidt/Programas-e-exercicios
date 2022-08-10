total = 0
j = 0
k = 0
l = 0
m = 0 
branco = 0
nulo = 0
x = 1
while x != 0:
    x = int(input("1 - Jose/ 2- Kevin/ 3- Marcio/ 4- Leandro / 5- Nulo / 6- Em branco: "))
    total = total + 1
    if x == 1:
        j = j + 1
    if x == 2:
        k = k + 1
    if x == 3:
        m = m + 1
    if x == 4:
        l = l + 1
    if x == 5:
        nulo = nulo + 1 
    if x == 6:
        branco = branco + 1
    else:
        nulo = nulo + 1

print("Candidato Jose com %i votos"%j)
print("Candidato Kevin com %i votos"%k)
print("Candidato Marcio com %i votos"%m)
print("Candidato Leandro com %i votos"%l)
print("Quantidade de votos em branco é de %i"%branco)
print("Quantidade de votos nulos é de %i"%nulo)
pn = (100*nulo)/total
pb = (100*branco)/total
print("A porcentagem de votos nulos é de %i"%pn)
print("A porcentagem de votos em branco é de %i"%pb)
