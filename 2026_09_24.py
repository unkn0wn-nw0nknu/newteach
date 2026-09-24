# 26. feladat
# Kérjük be egy diák matematika év végi jegyét numerikus formában, és írjuk ki azt szövegesen (elégtelen, elégséges, közepes, jó, jeles). Amennyiben a beírt érdemjegy nem 1..5 közötti szám, úgy a hibás adat kiírás jelenjen meg.

jegy = int(input("Add meg az év végi matek jegyed (1-5): "))

if jegy == 5:
    print("Jeles")
elif jegy == 4:
    print("Jó")
elif jegy == 3:
    print("Közepes")
elif jegy == 2:
    print("Közepes")
elif jegy == 1:
    print("Közepes")
else:
    print("HIBA: 1 és 5 közötti egész számot adj meg!")

# 27. feladat
# Kérjük be egy nap sorszámát (1..7) numerikus formában, és írjuk ki a nap megnevezését a képernyőre (hétfő, kedd, ..., vasárnap). Amennyiben a beírt sorszám nem 1..7 közötti szám, úgy a hibás adat kiírás jelenjen meg. 

napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
nap = int(input("Add meg az egyik nap sorszámát (1-7): "))

if nap == 1:
    print(napok[0])
elif nap == 2:
    print(napok[1])
elif nap == 3:
    print(napok[2])
elif nap == 4:
    print(napok[3])
elif nap == 5:
    print(napok[4])
elif nap == 6:
    print(napok[5])
elif nap == 7:
    print(napok[6])
else:
    print("HIBA: 1 és 7 közötti egész számot adj meg!")

# 28. Feladat
# Kérjük be egy hónap sorszámát (1..12) numerikus formában, és írjuk ki a hónap megnevezését a képernyőre (január, ..., december). Amennyiben a beírt sorszám nem 1..12 közötti szám, úgy a hibás adat kiírás jelenjen meg.
honapok = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
honap = int(input("Add meg az egyik hónap sorszámát (1-12): "))
if honap == 1:
    print(honapok[0])
elif honap == 2:
    print(honapok[1])
elif honap == 3:
    print(honapok[2])
elif honap == 4:
    print(honapok[3])
elif honap == 5:
    print(honapok[4])
elif honap == 6:
    print(honapok[5])
elif honap == 7:
    print(honapok[6])
elif honap == 8: 
    print(honapok[7])
elif honap == 9:
    print(honapok[8])
elif honap == 10:
    print(honapok[9])
elif honap == 12:
    print(honapok[11])
else:
    print("HIBA: 1 és 12 közötti egész számot adj meg!")

# 29. Feladat
# Kérjük be egy áru egységárát (Ft), a vásárlandó mennyiséget (db), és hogy mennyi pénz van nálunk (Ft). Adjuk meg, hogy meg tudjuk-e vásárolni a kívánt darabszámot, és ez esetben mennyi pénzünk maradna a vásárlás után. Ha nincs elég pénzünk, akkor azt adjuk meg, hány darab termék megvásárlására lenne csak elég a pénzünk. 

alma = 1982
mennyiseg = int(input("Hány kg almát akarsz? (Egységára 1982 Ft/kg): "))
penz = int(input("Mennyi pénzed van? "))

if penz > (mennyiseg*alma):
    print(f"Meg tudod venni, és még {penz-(alma*mennyiseg)} pénzed marad, vegyél még almát!")
else:
    print(f"Sajnos nincs elég pénzed a kivánt mennyiséghez. A pénzed {penz/alma} kg almára lenne elég, dolgozz még és vegyél almát!")

# 30. feladat
# Adott évről döntsük el, hogy szökőév-e! (Szökőévek a következők: minden néggyel osztható év, kivéve a százzal is oszthatókat. Szökőévek viszont a 400-zal osztható évek. Vagyis a százasra végződő évek közül csak azok szökőévek, amelyek 400-zal is oszthatók.)
ev = int(input("Add meg a jelenlegi évet: "))

if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
    print("Szökőév!")
else:
    print("EZ nem szökőév!")

# 31. feladat
# Generáljunk háromjegyű véletlenszámot!
import random

harom_jegyuek = random.randint(100, 999)
print(harom_jegyuek)   

# 31. feladat
# Programunk adjon meg véletlenszerűen egy 0 és 25 közötti egész számot, illetve egy 0 és 25 közötti tizedestörtet!

import random
null25 = random.randint(0, 25)
tortnull25 = random.uniform(0, 25)
print(null25)
print(tortnull25)

