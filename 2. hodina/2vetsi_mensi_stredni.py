a = input("Zadej cislo: ")
b = input("Zadej cislo: ")
c = input("Zadej cislo: ")
d = input("Zadej cislo: ")

# max cislo
max_cislo = a

if b > max_cislo:
    max_cislo = b

if c > max_cislo:
    max_cislo = c

if d > max_cislo:
    max_cislo = d

# min cislo
min_cislo = a

if b < min_cislo:
    min_cislo = b

if c < min_cislo:
    min_cislo = c

if d < min_cislo:
    min_cislo = d


print("Nejvetsi: " + str(max_cislo))
print("Nejmensi: " + str(min_cislo))
