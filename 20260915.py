#7. feladat

#pitagorasz tétel: a**2 + b**2 = c**2

import math

a = float(input("Add meg az egyik befogót: "))
b = float(input("Add meg a másik befogót: "))
c = math.sqrt(a**2+b**2)
print(f"Az átfogó {c:2f} cm")

#8. Feladat
#Programunk kérje be a megtett út hosszát és az eltelt időt, és számítsa ki az átlagsebességet!
# s = megtett út
# v = sebesség
# t = idő

# v = s/t

s = float(input("Add meg a megtett útat (m): "))
t = float(input("Add meg az eltelt időt (s): "))
print(f"Az átlagsebesség: {s/t} m/s")

# 9. Feladat
# Programunk kérje be egy autó fogyasztását (literben 100 km-en), a benzin literenkénti árát és a megteendő út hosszát, majd számítsa ki az útiköltséget!

fogyasztas = float(input("Add meg az autó fogyasztását (l/100km): "))
b_ar = float(input("Add meg a benzin literenkénti árát: "))
ut = float(input("Add meg a megteendő útat (m): "))

uzemanyag = ut*(fogyasztas/100)

print(f"Az úti költség: {uzemanyag*b_ar} Ft")

#10. Feladat
# Kérjük be a felhasználó tömegét kg-ban és magasságát cm-ben, majd számítsuk ki és írjuk a képernyőre a felhasználó testtömegindexét az alábbi képlet alapján! TTI= tö𝒎𝒆𝒈 * ma𝒈𝒂𝒔𝒔á𝒈𝟐 Figyelj rá, hogy a képletben a magasság méterben megadott értékével kell számolni! 

m = float(input("Add meg a tömeged (kg): "))
h = float(input("Add meg a magasságod (m): "))
TTI = m/h**2
print(f"A testtömegindexed {TTI}")

# 11. Feladat
# Zöldséges standunkon háromféle terméket árulunk: almát, szilvát és szőlőt. A program írja ki a gyümölcs nevét és kilogrammonkénti egységárát, majd kérdezze meg, hogy mennyit szeretnénk vásárolni. A vásárolt mennyiség mellett jelenjen meg a fizetendő összeg, majd a végösszeget is adjuk meg!
alma = 1990
szilva = 3000
szolo = 9000

am = float(input("Hány kg almát akarsz venni? (1990 Ft/kg) "))
szim = float(input("Hány kg szilvát akarsz venni? (3000 Ft/kg) "))
szom = float(input("Hány kg szőlőt akarsz venni? (9000 Ft/kg) "))

print(f"Összesen {am*alma} Ft az alma, {szilva*szim} a szilva és {szom*szolo} a szőlő, így összesen {alma*am+szilva*szim+szom*szolo} Ft.")


# 12. Feladat
# Programunk kérje be egy hordó és egy kancsó térfogatát literekben mérve egész számként! Szeretnénk tudni, hogy hány teli kancsó mérhető ki a hordóból, mennyi víz marad a hordóban a  teli kancsók kimerése után. Mennyi a hordó és a kancsó térfogatának hányadosa?
hordo = int(input("Add meg a hordó térfogatát (l): "))
kancso = int(input("Add meg a kancsó térfogatát (l): "))

marado_viz = hordo%kancso
print(f"A hordóban {marado_viz} l víz maradt.")

# 13. Feladat
# A bankjegyautomatából az ügyfél legfeljebb 300 000 Ft-ot vehet föl, 1 000, 5 000 és 10 000 Ft-os címletekben. A program kérjen be egy ezerrel osztható összeget, majd határozza meg, hogy egy beolvasott összeget milyen címletekben kell kifizetni, ha a lehető legkevesebb bankjegyet akarjuk felhasználni.
max = 300000
cimletek = [1000, 5000, 10000]

összeg = int(input("Add meg az 1000-rel osztható felvetendő összeget: "))

if összeg > max or összeg % 1000 != 0 or összeg <= 0:
    print("HIBA: Több mint 300000 Ft vagy az összeg nem osztható 1000-rel")
    összeg()
else:
    pass

db_10000 = összeg // 10000
összeg %= 10000
db_5000 = összeg // 5000
összeg %= 5000
db_1000 = összeg // 1000

print(f"10 000 Ft: {db_10000} db")
print(f"5 000 Ft: {db_5000} db")
print(f"1 000 Ft: {db_1000} db")

# 14. feladat
# Programunk kérje be egy eszköz másodpercekben mért üzemidejét! Eredményként adja meg …nap …óra …másodperc formában az üzemidőt!
uzemido = int(input("Adja meg az üzemidőt másodpercben: "))

nap = 0
ora = 0

if uzemido >= 86400:
    nap = uzemido // 86400
    uzemido = uzemido % 86400

if uzemido >= 3600:
    ora = uzemido // 3600
    uzemido = uzemido % 3600

print(f"{nap} nap {ora} óra {uzemido} másodperc")   
