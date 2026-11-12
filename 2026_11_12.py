#1. feladat
class Dolgozo:
    def __init__(self, fajl_sor):
        darabok = fajl_sor.strip().split(";")
        self.nev = darabok[0]
        self.reszleg = darabok[1]
        self.fizetes = int(darabok[2])
        self.belepes_eve = int(darabok[3])

#2. feladat PRO TIPP: A fájl legelején érdemes létrehozni
dolgozok_lista = []
with open("dolgozok.txt", "r", encoding="utf-8") as fajl:
    fajl.readline() #fejléc átugrása
    for fajl_sor in fajl:
        dolgozo = Dolgozo(fajl_sor)
        #példányosításra
        dolgozok_lista.append(dolgozo) #hozzáadjuk azt objektumot a listához
        #professzionálisoknak
        #dolgozo = Dolgozo(fajl.readline())

#3. feladat
print(f"3. feladat: {len(dolgozok_lista)} munkatárs van a cégnél")

#4. feladat
osszeg = 0
for dolgozo in dolgozok_lista:
    osszeg += dolgozo.fizetes
atlag = osszeg / len(dolgozok_lista)
print(f"4. feladat: A dolgozók átlag keresete: {round(osszeg,1)} Ft")

#5. feladat
max = dolgozok_lista[0] #az első dolgozót tartjuk először a legmagasabb fizetésűnek
for dolgozo in dolgozok_lista:
    if dolgozo.fizetes > max.fizetes:
        max = dolgozo #akárhányszor nagyobb egy másik dolgozónak a fizetése, mint a maxnak, akkor felülírjuk
print(f"A legjobban fizetett dolgozó:")
print(f"\tNév: {max.nev}")
print(f"\tReszleg: {max.reszleg}")
print(f"\tFizetes: {max.fizetes}")

#6. feladat
min = dolgozok_lista[0]
for dolgozo in dolgozok_lista:
    if dolgozo.fizetes < min.fizetes:
        min = dolgozo
print(f"A legrosszabbul fizetett dolgozo:")
print(f"\tNev: {min.nev}")
print(f"\tBelépési éve: {min.belepes_eve}")
