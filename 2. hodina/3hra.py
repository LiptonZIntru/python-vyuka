import random

a = int(input("Zadej cislo: "))

hadane_cislo = random.randint(1, 10)

'''
if a == hadane_cislo:
    print("Vyhral jsi ")
else:
    print("Prohral jsi ")
'''






































if a == hadane_cislo:
    print("Vyhral jsi ")
else:
    '''if a > hadane_cislo:
        print("Zadej mensi")
    else:
        print("Zadej vetsi")'''
    
    a = int(input("Zadej cislo: "))

    if a == hadane_cislo:
        print("Vyhral jsi ")
    else:
        '''if a > hadane_cislo:
            print("Zadej mensi")
        else:
            print("Zadej vetsi")'''

        a = int(input("Zadej cislo: "))

        if a == hadane_cislo:
            print("Vyhral jsi ")
        else:
            print("Prohral jsi ")
            print("Hadane cislo bylo: " + str(hadane_cislo))

