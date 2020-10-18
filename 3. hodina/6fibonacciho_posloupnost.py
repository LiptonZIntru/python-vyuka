pocet_clenu = int(input("Zadej pocet clenu posloupnosti: "))

a = 1
b = 2
print(a)
print(b)

for i in range(pocet_clenu - 2):
    a = a + b + b
    b = a - b
    a = a - b
    print(b)

