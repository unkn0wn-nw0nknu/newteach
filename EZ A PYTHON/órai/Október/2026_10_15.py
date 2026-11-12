#1. feladat

kiadasok = [3400, 1250, 8900, 450, 6200]

osszeg = sum(kiadasok)

print(f"Végösszeg: {osszeg} Ft")

print(20*"-")
#2. feladat

pontok = [45, 78, 92, 33, 60, 85]

sikeres = 0

for jegy in pontok:
    if jegy >= 60:
        sikeres += 1

print(f"Sikeres dolgozatok: {sikeres} db")

print(20*"-")
#3. feladat

szam = int(input("Adj meg egy pozitív egész számot: "))

for i in range(1, 11):
    print(f"{szam} * {i} = {szam * i}")

print(20*"-")
#4. feladat

jelszo = "titok123"

jelszo_input = str(input("Kérem a jelszót: "))

while True:
    jelszo_input = str(input("Kérem a jelszót: "))
    if jelszo != jelszo_input:
        print("Hibás jelszó!")
    else:
        print("Sikeres bejelentkezés!")
        break

print(20*"-")
#5. feladat

homersekletek = [12, -3, 0, -5, 8, -1, 4]

legalacsonyabb = min(homersekletek)

print(f"Legalacsonyabb hőmérséklet: {legalacsonyabb} °C")

print(20*"-")
#6. feladat

szamok = []

for i in range(5):
    szam = int(input("Adjon meg egy számot: "))
    szamok.append(szam)

print(szamok)

print(20*"-")
#7. feladat

szamok = [10, 15, 22, 33, 40, 55, 60]

parosok = []

for szam in szamok:
    if (szam%2) == 0:
        parosok.append(szam)

print(parosok)

print(20*"-")
#8. feladat

nevek = ["Kata", "Bence", "Anna", "Dániel", "Csilla"]

keresett = "Anna"

talalt_idx = -1
for i in range(len(nevek)):
    if nevek[i] == keresett:
        talalt_idx = i
        break

if keresett in nevek:
    pozicio = nevek.index(keresett)
    print(f"{keresett} indexe: {pozicio}")

print(20*"-")
#9. feladat

arak = [4500, 12000, 28000, 9500, 31000]

print(f"Legdrágább termék: {max(arak)} Ft")

print(20*"-")
#10. feladat

osszeg = 0

while True:
    szam = int(input("Szám: "))
    if szam == 0:
        break
    osszeg += szam
print(f"A beírt számok összege: {osszeg}")   

print(20*"-")
#11. feladat

kodok = [102, 305, 404, 500, 200]

for kod in kodok:
    if kod == 404:
        print("A 404-es kód szerepel a listában!")
        break
    else:
        print("Nem 404!")

print(20*"-")
#12. feladat

jegyek = [5, 4, 3, 5, 5, 2, 4] 

if len(jegyek) > 0:
    atlag = sum(jegyek) / len(jegyek)
    print(f"Átlag: {atlag:.2f}")
else:
    print("Üres lista!")

print(20*"-")
#13. feladat

n = int(input("Adjon meg egy számot: "))

fakt = 1
for i in range(1, n + 1):
    fakt *= i

print(f"{n} faktoriálisa: {fakt}")   

print(20*"-")
#14. feladat

szavak = ["fa", "programozas", "asztal", "auto", "szamitogep"] 

legnagyobb = szavak[0]
for szo in szavak:
    if len(legnagyobb) < len(szo):
        legnagyobb = szo

print(legnagyobb)

print(20*"-")
#15. feladat

tavolsagok = [12.5, 8.0, 15.2, 21.0, 5.5]

hosszu_turak = []

for tav in tavolsagok:
    if tav > 10:
        hosszu_turak.append(tav)

print(f"Hosszú túrák: {hosszu_turak}")

print(60*"-")

#16. feladat

pontszamok = [45, 80, 65, 90, 70, 50] 
atlagon_felul = []

if len(pontszamok) > 0:
    atlag = sum(pontszamok) / len(pontszamok)
    print(f"Átlag: {atlag:.2f}")
else:
    print("Üres lista!")

for pont in pontok: 
    if pont > atlag:
        atlagon_felul.append(pont)

print(atlagon_felul)

print(20*"-")
#17. feladat

csoport_a = [101, 105, 108, 112, 120]
csoport_b = [103, 105, 110, 112, 125]

kozos = []

for a in csoport_a:
    for b in csoport_b:
        if a == b:
            kozos.append(a)

print(f"Közös azonosítók: {kozos}")   

print(20*"-")
#18. feladat

n = int(input("Méret: "))

negyzet = []

for i in range(n):
    for j in range(n):
        print("*")
    print()   

#19. feladat

bevetel_matrix = [ [12000, 15000], [18000, 21000], [9000, 11000] ]

print(sum(bevetel_matrix))