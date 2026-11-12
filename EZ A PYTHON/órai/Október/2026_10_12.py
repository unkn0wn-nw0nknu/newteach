# 1. feladat

kiadasok = [4500, 12000, 3200, 8900, 15400]

osszeg = sum(kiadasok)
print(f"A heti összkiadás: {osszeg} Ft")

print(25*"-")

#2. feladat

csomagok_kg = [14.5, 22.0, 5.8, 31.2, 8.0]

ossztomeg = sum(csomagok_kg)

print(f"Össztömeg: {ossztomeg} kg")

print(25*"-")

#3. feladat

jegyek = [5, 4, 5, 3, 4, 5]

if len(jegyek) > 0:
    atlag = sum(jegyek) / len(jegyek)
    print(f"Tanulmányi átlag: {atlag:.2f}")
else:
    print("Üres lista!")

print(25*"-")

#4. feladat

meresek = [12, -4, 25, 0, 18, -2, 5]

osszeg = 0
db = 0

for m in meresek:
    if m > 0:
        osszeg += m
        db += 1

atlag = osszeg / db
print(f"Pozitív mérések átlaga: {atlag}")
  
print(25*"-")

#5. feladat

szamok = [11, 24, 35, 48, 50, 13]

osszeg = 0

for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam


print(f"A páros számok összege: {osszeg}")   

print(25*"-")

#6. feladat

homersekletek = [3, -2, 5, -4, 0, -1]

alkalmak = 0

for fok in homersekletek:
    if fok < 0:
        alkalmak += 1

print(f"Fagyos napok száma: {alkalmak} db")

print(25*"-")

#7. feladat

dolgozatok = [5, 4, 3, 5, 2, 5, 4, 5]

otosok = 0

for jegy in dolgozatok:
    if jegy == 5:
        otosok += 1

print(f"Ötösök száma: {otosok}")

print(25*"-")

#8. feladat

kodok = [5, 42, 108, 99, 3, 14, 7]

ketjegyu = 0

for szam in kodok:
    if szam >= 10 and szam <= 99:
        ketjegyu += 1

print(f"Kétjegyű számok száma: {ketjegyu} db")

print(25*"-")

#9. feladat

nevek = ["Anna", "Bence", "Attila", "Dávid", "András"] 

anevek = 0

for a in nevek:
    if a[0] == "A":
        anevek += 1

print(f"'A' betűs nevek száma: {anevek} db")

print(25*"-")

#10. feladat

pontszamok = [65, 82, 40, 95, 78]

kiemelkedo = 0

if len(pontszamok) > 0:
    atlag = sum(pontszamok) / len(pontszamok)
    
    print(f"Átlag: {atlag:.2f}")

for szam in pontszamok:
    if szam > atlag:
        kiemelkedo += 1

print(f"Átlag feletti dolgozatok: {kiemelkedo} db")

print(25*"-")

#11. feladat

alapanyagok = ["liszt", "cukor", "mogyoró", "vaj", "tojás"] 

if "mogyoró" in alapanyagok:
    print("Allergén riasztás: Található mogyoró a termékben!")   

print(25*"-")

#12. feladat

szamok = [14, 8, 22, -5, 30, 4]

for szam in szamok:
    if szam < 0:
        print("A lista tartalmaz negatív értéket.")
        break

print(25*"-")

#13. feladat

jegyek = [4, 3, 5, 1, 4, 5] 

for szam in jegyek:
    if szam == 1:
        print("Van bukott diák a csoportban.")
        break

print(25*"-")

#14. feladat

befizetesek = [5000, 10000, 8000, 25000, 12000]

for befizet in befizetesek:
    if befizet > 20000:
        print("Volt 20 000 Ft feletti befizetés.")
        break

print(25*"-")

#15. feladat

tiltott_szavak = ["admin", "root", "123456", "password"] 

for szavak in tiltott_szavak:
    if szavak == "123456":
        print("A megadott jelszó szerepel a tiltólistán.")
        break

print(25*"-")

#16. feladat

arak = [42000, 19500, 68000, 31000] 

print(f"Legolcsóbb jegy: {min(arak)} Ft")

print(25*"-")

#17. feladat

homersekletek = [14.2, 19.8, 23.5, 21.0, 17.4]

print(f"Napi csúcshőmérséklet: {max(homersekletek)} °C")

print(25*"-")

#18. feladat

pontok = [88, 42, 95, 60, 35, 78] 

print(f"Legkisebb pontszám: {min(pontok)} | Legnagyobb pontszam: {max(pontok)}")

print(25*"-")

#19. feladat

szavak = ["programozas", "python", "kod", "fejleszto", "ciklus"] 
legkisebb = szavak[0]
for szo in szavak:
    if len(legkisebb) > len(szo):
        legkisebb = szo

print(f"Legrövidebb szó: {legkisebb}")

print(25*"-")

#20. feladat

fagyok = [-12, -4, -18, -2, -8] 

print(f"A legenyhébb fagyos érték: {min(fagyok)}")

print(25*"-")

#21. feladat

futok = ["Anna", "Bence", "Csilla", "Dávid"]

keresett = "Csilla"

talalt_idx = -1

for i in range(len(futok)):
    if futok[i] == keresett:
        talalt_idx = i
        print(f"Csilla indexe a listában: {talalt_idx}")
        break

print(25*"-")

#22. feladat

minoseg = ["OK", "OK", "HIBA", "OK", "HIBA"] 

keresett = "HIBA"

talalt_idx = -1

for i in range(len(minoseg)):
    if minoseg[i] == keresett:
        talalt_idx = i
        print(f"Az első hibás alkatrész a(z) {talalt_idx}. indexen található.")
        break

print(25*"-")

#23. feladat

vonalkodok = [1014, 2045, 3099, 4120]
keresett = 9999
talalva = False

for kod in vonalkodok:
    if kod == keresett:
        talalva = True
        break

if talalva:
    print(f"A(z) {keresett} kód megtalálva!")
else:
    print("A kód nem található!")   

print(25*"-")

#24. feladat

sebessegek = [48, 52, 90, 115, 60, 130]

for i, seb in enumerate(sebessegek):
    if seb > 100:
        print(f"Első túllépés: {seb} km/h a(z) {i}. indexen.")
        break   

print(25*"-")

#25. feladat

termek_arak = [4500, 12900, 8900, 24500, 3200]

max_ar = termek_arak[0]
max_index = 0

for i, ar in enumerate(termek_arak):
    if ar > max_ar:
        max_ar = ar
        max_index = i

print(f"A legdrágább termék ára: {max_ar} Ft, indexe: {max_index}")   

print(25*"-")
