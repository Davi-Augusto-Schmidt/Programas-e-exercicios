x = 1
ma = 0
mb = 2.5
mg = 0
mm = 200
mda = 0
mdp = 0
cma = x
cmb = x
cmg = x
cmm = x
k = 0
while True:
    x = int(input("Digite o seu código da Academia: "))
    if x == 0:
        break
    a = float(input("Digite a sua altura em metros: "))
    p = float(input("Digite o seu peso em kg: "))
    k = k + 1
    mda += a
    mdp += p
    if a > ma:
        ma = a
        cma = x
    if a < mb:
        mb = a
        cmb = x
    if p > mg:
        mg =  p
        cmg = x
    if p < mm:
        mm = p
        cmm = x

print("O código do cliente mais alto é %i e ele(a) tem %g m"%(cma,ma))
print("O código do cliente mais baixo é %i e ele(a) tem %g m"%(cmb,mb))
print("O código do cliente mais pesado é %i e ele(a) tem %g kg"%(cmg,mg))
print("O código do cliente mais magro é %i e ele(a) tem %g kg"%(cmm,mm))
print("A média de altura é de %g"%(mda/k))
print("A média de peso é de %g"%(mdp/k))
