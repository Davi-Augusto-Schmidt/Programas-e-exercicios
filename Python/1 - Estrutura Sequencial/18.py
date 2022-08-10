print("Calculadora para velocidade de download")
x = int(input("Tamanho do Arquivo (em MB): "))
y = int(input("Velocidade da internet(em Mbps): "))
t = x/y
tm = t / 60
print("O tempo para o download acabarr é de: ",tm,"Minutos")
