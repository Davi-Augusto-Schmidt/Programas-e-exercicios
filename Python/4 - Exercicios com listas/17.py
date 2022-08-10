nome = "Ninguem"
while len(nome) != 0: 
    nome = input("Digite o nome do atleta: ")
    print("")
    if len(nome)>0: 
        saltos = []
        lista = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
        for i in range(5):
            saltos.append(float(input(f"Digite o tamanho do {lista[i]} salto em metros: ")))
        print("")
        print("Atleta: ",nome)
        print("Saltos: ",saltos)
        print("Média dos saltos: ",(sum(saltos))/5)
