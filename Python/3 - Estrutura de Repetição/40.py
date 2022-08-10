mei = 100000
mai = 0
meic = 0
maic = 0
mdv = 0
meat = 0
cm = 0
macm = 0
for i in range(1,6):
    x = int(input("Digite o código da cidade: "))
    nv = int(input("Numéro de veiculos de passeio na cidade: "))
    na = int(input("Numéro de acidentes de transito na cidade: "))
    mdv += nv
    
    if nv < 2000:
        meat += nv
        cm += 1
        macm += na
        
    if na > mai:
        mai = na
        maic = x
        
    if na < mei:
        mei = na
        meic = x

print("A cidade com menos acidentes é %i com %i acidentes por ano"%(meic,mei))
print("A cidade com mais acidentes é %i com %i acidentes por ano"%(maic,mai))
print("A média de veiculos nas 5 cidades é de %g por ano"%(mdv/5))
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de %g por ano"%(macm/cm))
