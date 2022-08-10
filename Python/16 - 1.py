print("POLINDROMOS SÃO FODAS")

n = int(input("Digite um numero maior que 10 e veremos se é polindromo: "))
aux = n
dig = reverso = 0
while aux != 0:
    dig = aux%10
    reveerso = reverso*10 + dig
    aux = aux//10

if reverso == n:
    print("Polindromo")
else:
    print("Não polindromo")
