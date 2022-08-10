x = int(input("Digite um numero: "))
c = 0
d = 0
u = 0
v = x
if 0 < x <1000:
    c = v//100
    v = v/100
    v = v - c
    u = (v * 100)%10
    d = (v*10)
    dv = ((d *10)%10)/10
    dvv = d - dv
    
    print(c," centenas, ",dvv," dezenas, ",u," unidades.")
    
else:
    print("numero invalido")
    
