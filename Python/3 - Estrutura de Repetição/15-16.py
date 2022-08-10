print("Sequencia de fibonacci.")
fn = 0
f1 = 1
f2 = 1
print(f1)
print(f2)
for i in range(14):
    fn = f1 + f2
    print(fn)
    f2 = f1
    f1 = fn
    
