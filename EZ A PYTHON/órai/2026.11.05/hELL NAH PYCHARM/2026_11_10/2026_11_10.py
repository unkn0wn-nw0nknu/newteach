with open("dolgozok.txt","r", encoding="utf-8") as fajl:
    fejlec = fajl.readline() #beolvassuk az 1. sort, a fejlecet, különben problémába ütközünk.

    #végig megyünk a fejléc nélküli fájlon
    for fajlsor in fajl:
        #szét kell kapni a sorokat kisebb darabkákra, listát kreál
        darabok = fajlsor.strip().split(";")
        nev = darabok[0]
        varos = darabok[1]
        reszleg = darabok[2]
        print(nev, "-", varos, "-", reszleg)


#termekek.txt
with open("termekek.txt", "r", encoding="utf-8") as termekek:
    termekek.readline()
    for fajlsor in termekek:
        darabok = fajlsor.strip().split(";")
        termekNev = darabok[0]
        raktarKeszlet = int(darabok[1]) #átalakítjuk egész számmá
        egysegAr = float(darabok[2])

#mindenek előtt egy listát hozzunk létre
print("---diakok.txt"*15)
diakokLista = []

class Diak: #diakok.txt
    def __init__(self, _nev, _osztaly, _kor, _atlag):
        self.nev = _nev
        self.osztaly = _osztaly
        self.kor = _kor
        self.atlag = _atlag

with open("diakok.txt", "r", encoding="utf-8") as fajl:
    fejlec = fajl.readline()

    for fajlsor in fajl:
        darabok = fajlsor.strip().split(";")
        nev = darabok[0]
        osztaly = darabok[1]
        kor = int(darabok[2])
        atlag = float(darabok[3])
        diak = Diak(nev, osztaly, kor, atlag)
        diakokLista.append(diak)

for diak in diakokLista:
    print("-"*20)
    print(f"Név: {diak.nev}, Osztály: {diak.osztaly}")
    print(f"Kor: {diak.kor}, Atlag: {diak.atlag}")

#1. feladat: hány diák szerepel a fájlban?
#1. megoldás: megszámlálás tétel
hany_diak_van = 0
for diak in diakokLista:
    hany_diak_van += 1
print(f"1. feladat: {hany_diak_van} szerepel a fájlban")
#2. megoldás: beépített függvény
print(f"1. feladat: {len(diakokLista)} szerepel a fájlban")

#2. feladat: számold ki a diákok átlagosztályzatát 2 tizedesre végződve
#1. megoldás: átlagolás tétele
import numpy as np
osszeg = 0
for diak in diakokLista:
    osszeg += diak.atlag
atlag = osszeg / len(diakokLista) #22.1699999 / 5 = 4.433999
print(round(atlag, 2))
print()
#2. megoldás: 1 sor
print(f"Diákok átlaga: {np.average}")

#3. feladat: átlag alapján írjuk ki a legjobb diák adatait
#1. feladat: max kiválasztása
max = diakokLista[0]

for diak in diakokLista:
    if diak.atlag > max.atlag:
        max = diak
print(f"legjobb diák adatai: {max.nev}, {max.osztaly}, {max.kor} éves, {max.atlag}-gal")