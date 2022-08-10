aa = 0
ab = 200
caa = 0
cab = 0

for i in range(1,11):
    a = int(input("Digite sua altura: "))
    if a > aa:
        caa = i
        aa = a
    if a < ab:
        cab = i
        ab = a
print("O aluno(a) mais alto é o %i e ele tem %icm"%(caa,aa))
print("O aluno(a) mais baixo é o %i e ele tem %icm"%(cab,ab))
