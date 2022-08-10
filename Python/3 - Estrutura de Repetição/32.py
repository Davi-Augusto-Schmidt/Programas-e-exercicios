print("Diga um numero.")
print("E eu direi seu fatorial!")
x = int(input("Digite um numero: "))
c = x
print("%i fatorial é:"%x)
while c != 1 :
    c = c -1
    x += x * (c-1)
print(x)
