def pocet_suborov():
    while True:
        cislo = input("Zadajte počet súborov")
        try:
            return int(cislo)
        except ValueError:
            print("Nebolo zadané celé číslo!")

vstup = []
pocet = 0

with open("basnicka.txt") as subor:
    for slovo in subor:
        input += slovo.split()

for i in range(pocet_suborov()):
    pocet += 1
    if pocet == len(vstup):
        pocet -= len(vstup)
    with open(f"""slovo{pocet}""", mode="w") as subor:
        print(vstup[pocet - 1], file=subor)
