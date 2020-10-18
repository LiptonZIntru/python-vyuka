import random

hadane_cislo = random.randint(1, 10)

a = int(input("Zadej cislo: "))
while a != hadane_cislo:
    if a > hadane_cislo:
        print("Zadej mensi")
    else:
        print("Zadej vetsi")
    a = int(input("Zadej cislo: "))
print("Vyhral jsi")
