import math

# 7. feladat
# Írjunk programot a Pitagorasz-tétel alkalmazására! A program kérje be egy derékszögű háromszög két befogóját, és számítsa ki az átfogó hosszát!
a = float(input("Add meg az egyik befogót: "))
b = float(input("Add meg a másik befogót: "))
c = math.sqrt(a**2 + b**2)
print(f"Az átfogó: {c} cm")

# 8. feladat
# Programunk kérje be a megtett út hosszát és az eltelt időt, és számítsa ki az átlagsebességet!
s = float(input("Add meg a megtett utat (m): "))
t = float(input("Add meg az eltelt időt (s): "))
print(f"Az átlagsebesség: {s/t} m/s")

# 9. feladat
# Programunk kérje be egy autó fogyasztását (literben 100 km-en), a benzin literenkénti árát és a megteendő út hosszát, majd számítsa ki az útiköltséget! 
fogyasztas = float(input("Add meg az autó fogyasztását (l/100km): "))
b_ar = float(input("Add meg a benzin literenkénti árát: "))
ut = float(input("Add meg a megteendő utat (km): "))
uzemanyag = ut * (fogyasztas / 100)
print(f"Az úti költség: {uzemanyag * b_ar} Ft")

# 10. feladat
# Kérjük be a felhasználó tömegét kg-ban és magasságát cm-ben, majd számítsuk ki és írjuk a képernyőre a felhasználó testtömegindexét az alábbi képlet alapján! TTI= tö𝒎𝒆𝒈 * m𝒂𝒈𝒂𝒔𝒔á𝒈**𝟐 Figyelj rá, hogy a képletben a magasság méterben megadott értékével kell számolni! 
m = float(input("Add meg a tömeged (kg): "))
h_cm = float(input("Add meg a magasságod (cm): "))
h_m = h_cm / 100
TTI = m / (h_m**2)
print(f"A testtömegindexed: {TTI}")

# 11. feladat
# Zöldséges standunkon háromféle terméket árulunk: almát, szilvát és szőlőt. A program írja ki a gyümölcs nevét és kilogrammonkénti egységárát, majd kérdezze meg, hogy mennyit szeretnénk vásárolni. A vásárolt mennyiség mellett jelenjen meg a fizetendő összeg, majd a végösszeget is adjuk meg!
alma = 1990
szilva = 3000
szolo = 9000

print("Zöldséges árak:")
print(f"Alma: {alma} Ft/kg")
print(f"Szilva: {szilva} Ft/kg")
print(f"Szőlő: {szolo} Ft/kg")

am = float(input("Hány kg almát szeretnél venni? "))
szim = float(input("Hány kg szilvát szeretnél venni? "))
szom = float(input("Hány kg szőlőt szeretnél venni? "))

alma_osszeg = am * alma
szilva_osszeg = szim * szilva
szolo_osszeg = szom * szolo
vegosszeg = alma_osszeg + szilva_osszeg + szolo_osszeg

print(f"Alma: {alma_osszeg} Ft, Szilva: {szilva_osszeg} Ft, Szőlő: {szolo_osszeg} Ft")
print(f"A fizetendő végösszeg: {vegosszeg} Ft")

# 12. feladat
#  Programunk kérje be egy hordó és egy kancsó térfogatát literekben mérve egész számként! Szeretnénk tudni, hogy hány teli kancsó mérhető ki a hordóból, mennyi víz marad a hordóban a teli kancsók kimerése után. Mennyi a hordó és a kancsó térfogatának hányadosa?
hordo = int(input("Add meg a hordó térfogatát (l): "))
kancso = int(input("Add meg a kancsó térfogatát (l): "))

teli_kancso = hordo // kancso
marado_viz = hordo % kancso
hanyados = hordo / kancso

print(f"Teli kancsók száma: {teli_kancso}")
print(f"A hordóban maradt víz: {marado_viz} l")
print(f"A térfogatok hányadosa: {hanyados}")

# 13. feladat
#  A bankjegyautomatából az ügyfél legfeljebb 300 000 Ft-ot vehet föl, 1 000, 5 000 és 10 000 Ft-os címletekben. A program kérjen be egy ezerrel osztható összeget, majd határozza meg, hogy egy beolvasott összeget milyen címletekben kell kifizetni, ha a lehető legkevesebb bankjegyet akarjuk felhasználni.
osszeg = int(input("Add meg a felvenni kívánt összeget (1000-rel osztható, max 300 000): "))

if osszeg > 300000 or osszeg % 1000 != 0 or osszeg <= 0:
    print("HIBA: Hibás összeget adott meg!")
else:
    db_10000 = osszeg // 10000
    maradék = osszeg % 10000
    
    db_5000 = maradék // 5000
    maradék = maradék % 5000
    
    db_1000 = maradék // 1000
    
    print(f"10 000 Ft: {db_10000} db")
    print(f"5 000 Ft: {db_5000} db")
    print(f"1 000 Ft: {db_1000} db")

# 14. feladat
#  Programunk kérje be egy eszköz másodpercekben mért üzemidejét! Eredményként adja meg …nap …óra …másodperc formában az üzemidőt!
uzemido = int(input("Adja meg az üzemidőt másodpercben: "))

nap = uzemido // 86400
maradek = uzemido % 86400

ora = maradek // 3600
maradek = maradek % 3600

perc = maradek // 60
masodperc = maradek % 60

print(f"{nap} nap {ora} óra {perc} perc {masodperc} másodperc")

# 15. feladat
#  Írjunk programot, amely kiszámítja egy autóval megtett útra fizetett költségtérítést! A program kérje be a megtett út hosszát km-ben, az autó fogyasztását 100 km-en literben valamint az üzemanyag árát és ezek ismeretében számítsa ki az üzemanyagköltséget. A megtett útra, a fogyasztásra , és az üzemanyag árára is fogadjon el tört számokat is. [Az üzemanyagköltség kiszámítására használd az alábbi képletet: üzemanyagköltség=(út*fogyasztás*üzemanyag ár)/100 ] A költségtérítés összege 100 km-nél nem hosszabb út esetén maga az üzemanyagköltség, ennél hosszabb út esetén az üzemanyagköltséghez hozzáadják a megtett út 25-szörösét és így kapjuk meg a költségtérítést. A program címe "Utazási költségtérítés" legyen és minta szerinti formában írja ki az adatokat!
print("Utazási költségtérítés")
ut = float(input("Add meg a megtett út hosszát (km): "))
fogyasztas = float(input("Add meg a fogyasztást (l/100km): "))
ar = float(input("Add meg az üzemanyag árát (Ft/l): "))

uzemanyagkoltseg = (ut * fogyasztas * ar) / 100

if ut <= 100:
    koltsegterites = uzemanyagkoltseg
else:
    koltsegterites = uzemanyagkoltseg + (ut * 25)

print(f"A fizetendő költségtérítés: {koltsegterites} Ft")

# 16. feladat
# Kérjük be a külső hőmérsékletet, és írassuk ki, ha fagy odakint!
homerseklet = float(input("Add meg a külső hőmérsékletet (°C): "))
if homerseklet < 0:
    print("Fagy odakint!")

# 17. feladat
#  Kérdezzük meg a felhasználótól, hogy szeret-e programozni, ha igen, akkor írassunk ki, hogy „Még sokra viszed az életben!”, majd köszönjön el a program (Viszontlátásra!)
valasz = input("Szeretsz programozni? (igen/nem): ")
if valasz == "igen":
    print("Még sokra viszed az életben!")
print("Viszontlátásra!")

# 18. feladat
#  Kérjünk be egy egész számot, és írassuk ki hogy az adott szám páros-e vagy sem.
szam = int(input("Adj meg egy egész számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

# 19. feladat
# Olvassunk be egy számot a billentyűzetről, és írjuk ki, hogy osztható-e 3-mal! 
szam = int(input("Adj meg egy számot: "))
if szam % 3 == 0:
    print("A szám osztható 3-mal.")
else:
    print("A szám nem osztható 3-mal.")

# 20. feladat
#Olvasson be a billentyűzetről egy számot és mondjuk meg, hogy a szám negatív, vagy pozitív vagy egyik sem!
szam = float(input("Adj meg egy számot: "))
if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám egyik sem (nulla).")

# 21. feladat
#  Két beolvasott számot írassunk ki úgy, hogy közéjük tesszük a megfelelő relációs jelet (<,>,=)!
a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")

# 22. feladat
# Egy beolvasott számról döntse el a program hogy -30 és 40 között van-e!
szam = float(input("Adj meg egy számot: "))
if szam > -30:
    if szam < 40:
        print("A szám -30 és 40 között van.")
    else:
        print("A szám nincs a megadott tartományban.")
else:
    print("A szám nincs a megadott tartományban.")

# 23. feladat
# Írjunk programot, amely értékel egy dolgozatot a rá adott pontszám alapján! Az értékelés a következő táblázat alapján történjen: Pontszám Értékelés: 0 - 42 elégtelen, 43 - 57 elégséges, 58 - 72 közepes, 73 - 87 jó, 88 - 100 jeles
pont = int(input("Add meg a dolgozat pontszámát (0-100): "))

if pont < 0:
    print("Hibás pontszám!")
elif pont > 100:
    print("Hibás pontszám!")
elif pont < 43:
    print("Értékelés: elégtelen")
elif pont < 58:
    print("Értékelés: elégséges")
elif pont < 73:
    print("Értékelés: közepes")
elif pont < 88:
    print("Értékelés: jó")
else:
    print("Értékelés: jeles")

# 24. feladat
# Írj programot, amely bekér a felhasználótól egy helységnevet, valamint ennek a helységnek a lélekszámát, és a megadott lélekszámtól függően kiírja, hogy az adott helység milyen településtípusba tartozik. (telepules) − ha a lélekszám kevesebb, mint 5000, akkor község − ha a lélekszám legalább 5000, de kevesebb, mint 20 000, akkor kisváros − ha a lélekszám legalább 20 000, de kevesebb, mint 100 000, akkor középváros − ha a lélekszám legalább 100 000, de kevesebb, mint 1 000 000, akkor nagyváros − ha a lélekszám legalább 1 000 000, akkor metropolis − ha a felhasználó 0 vagy annál kisebb számot ad meg, a program írja ki, hogy "Hibás adatbevitel"
helyseg = input("Add meg a helység nevét: ")
lelekszam = int(input("Add meg a lélekszámot: "))

if lelekszam <= 0:
    print("Hibás adatbevitel")
elif lelekszam < 5000:
    print(f"{helyseg} egy község.")
elif lelekszam < 20000:
    print(f"{helyseg} egy kisváros.")
elif lelekszam < 100000:
    print(f"{helyseg} egy középváros.")
elif lelekszam < 1000000:
    print(f"{helyseg} egy nagyváros.")
else:
    print(f"{helyseg} egy metropolis.")

# 25. feladat
#  A program kérjen be két számot, és egy műveleti jelet (+,-,/,*), majd írja ki a művelet eredményét
a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))
muvelet = input("Add meg a műveleti jelet (+, -, *, /): ")

if muvelet == "+":
    print(f"Eredmény: {a + b}")
elif muvelet == "-":
    print(f"Eredmény: {a - b}")
elif muvelet == "*":
    print(f"Eredmény: {int(a * b)}")
elif muvelet == "/":
    if b == 0:
        print("Nullával nem osztunk!")
    else:
        print(f"Eredmény: {int(a / b)}")
else:
    print("Ismeretlen műveleti jel!")