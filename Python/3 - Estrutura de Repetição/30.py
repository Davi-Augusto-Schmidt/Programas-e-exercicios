print("Tabela de preços da panificadora")
pao = 0.18
vf = 0
for i in range(1,51):
    vf = pao * i
    print("O preço de %i pães é de %.2f"%(i,vf))
    
