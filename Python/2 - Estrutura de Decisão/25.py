print("Programa Detetive")
print("Responda as perguntas com sim(1) ou não(2).")
p1=int(input("Telefonou para a vítima?"))
p2=int(input("Esteve no local do crime"))
p3=int(input("Mora perto da vítima?"))
p4=int(input("Devia para a vítima?"))
p5=int(input("Já trabalhou com a vítima?"))
ac = 0

if p1 == 1:
    ac = ac +1
if p2 == 1:
    ac = ac +1
if p3 == 1:
    ac = ac +1
if p4 == 1:
    ac = ac +1
if p5 == 1:
    ac = ac +1

if ac == 2:
    print("Cumplice")
elif ac == 3 or ac ==4:
    print("Suspeito")
elif ac == 5:
    print("Assassino")
else:
    print("Inocente")
