import random
meu = []
megasena = list(range(1,61))

for i in range (1,7):
    x = int(input("Digite o %iº numero da sua megasena: "%i))
    meu.append(x)
    print("Sua megasena é ",meu)
    
n = int(input("Quantas vezes  quer testar sua megasena: "))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    
    
    while meu != sorteado:
        
        mega_sort = megasena.copy()

        sorteado = []
        
        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont += 1
        
    soma += cont
    
    print("Resultado do Teste %i: %i tentativas"%(i+1,cont))

soma /= n

print("Média dos resultados: ",soma)
