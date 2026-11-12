# 26. Két lista összehasonlítása – Közös hobbik (kozos_elemek) 
# Adott két tanuló hobbijainak listája (pl. ["foci", "rajz", "olvasás", "zene"] és 
# ["zene", "túra", "foci", "úszás"]). Ciklussal keresd meg és gyűjtsd ki egy 
# harmadik listába azokat a tevékenységeket, amelyek mindkettejük 
# listájában megtalálhatók!

A = ["foci", "rajz", "olvasás", "zene"]
B = ["zene", "túra", "foci", "úszás"]

közös_elemek = list(set(A) & set(B))

print(közös_elemek)

print("-"*25)
# 27. Raktárkészlet riasztás (raktarkeszlet) 
# Egy üzlet termékneveit egy termekek, darabszámait pedig egy azonos 
# hosszúságú darabszamok listában tároljuk párhuzamosan. Írasd ki 
# indexelés segítségével azoknak a termékeknek a nevét, amelyekből 5-nél 
# kevesebb van készleten (kritikus szint)!

termekek = ["Réka", "Csokis süti", "Asztal (ami nem szék)", "Pöttyös labda", "Limitált kiadású Bogyó és Babóca DVD"]
darabszam = [1, 10, 3, 7, 2]

for termekek, darabszam in zip(termekek, darabszam):
    if darabszam < 5:
        print("SOS! Kritikus mennyiség! Venni kell még: ")
        print(termekek)

print("-"*25)
# 28. Közösségi média aktivitás (inaktiv_felhasznalok) 
# Egy fórumon rögzítették a tagok belépési napjainak számát az elmúlt 
# hónapban. Készíts egy programot, amely megkeresi a listában az első 
# olyan felhasználót (indexével együtt), aki egyetlen napot sem volt aktív 
# (értéke 0)! A keresést találat esetén azonnal állítsd le (break)!

tagok = ["Józsi_01", "Józsi_02", "Józsi_03"]
aktivitas = [0, 2, 10]

for tagok, aktivitas in zip(tagok, aktivitas):
    if aktivitas == 0:
        print("Az Illumináti-média leglustább felhasználója:")
        print(tagok)

print("-"*25)

# 29. Monotonitás vizsgálat: Emelkedő túraútvonal (tura_szint) 
# Egy túrázó egy óránként rögzített tengerszint feletti magasságokat egy 
# listában tárolja (pl. [200, 245, 310, 415, 520]). Írj programot, amely eldönti 
# egy logikai változóval és ciklussal, hogy a túrázó végig folyamatosan 
# emelkedett-e (minden mérési pont magasabb-e, mint az előző)!

tura_szint = [200, 245, 310, 415, 520]

folyamatosan_emelkedik = True

for i in range(1, len(tura_szint)):
    if tura_szint[i] <= tura_szint[i - 1]:
        folyamatosan_emelkedik = False
        break

if folyamatosan_emelkedik:
    print("A túrázó végig folyamatosan emelkedett.")
else:
    print("A túrázó NEM emelkedett végig folyamatosan.") 

print("-"*25) 

# 30. Rulett szimuláció (rulett_nulla) 
# Szimulálj európai rulettet (számok 0 és 36 között). Pörgess addig egy while 
# ciklussal, amíg ki nem pörög a zöld 0-s! A végén írd ki, összesen hány 
# pörgetésre volt szükség, és a pörgetések hány százaléka volt piros/fekete 
# (nem nulla)!

import random

piros = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
fekete = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

porgetesek = 0
piros_db = 0
fekete_db = 0

while True:
    szam = random.randint(0, 36)
    porgetesek += 1

    if szam == 0:
        print("ZÖLD!!!!")
        break
    elif szam in piros:
        piros_db += 1
    else:
        fekete_db += 1

print(f"Összes pörgetés: {porgetesek}")
print(f"Piros: {piros_db}  |  Fekete: {fekete_db}")
print(f"Piros + fekete (nem nulla) aránya: {(piros_db + fekete_db) / porgetesek * 100:.1f}%")   

print("-"*25)

# 31. Szélsőérték eltávolítása (sportolo_pontszam) 
# Egy műugró 7 bírótól kapott pontszámot (1.0 és 10.0 között, 
# tizedesjegyekkel). A szabályok szerint a legkisebb és a legnagyobb 
# pontszámot kiejtik. Töröld ki a listából a minimumot és a maximumot, 
# majd a maradék 5 pontszámból számolj átlagot!

import random

eredmeny = []
for i in range(7):
    eredmeny.append(random.uniform(1.0, 10.0)) #
    
print(eredmeny)

eredmeny.remove(max(eredmeny))
eredmeny.remove(min(eredmeny))

pontszam = sum(eredmeny) / 5
print(pontszam)   

print()

print("-"*25)

#32. Családi költségvetés – túllépés keresése (koltsegvetes_stop) A program kérje be a napi vásárlások összegeit mindaddig, amíg a havi keretet (150 000 Ft) el nem éri az összeg. Amikor túllépi, írja ki, pontosan melyik tétel okozta a túllépést, és mennyivel haladta meg a limitet! 
keret = 150000
osszeg = 0
nap = 1

while osszeg <= keret:
    vasarlas = int(input(f"{nap}. napi vásárlás összege (Ft): "))
    osszeg += vasarlas
    if osszeg > keret:
        print(f"A(z) {nap}. napi vásárlás ({vasarlas} Ft) okozta a túllépést!")
        print(f"A túllépés mértéke: {osszeg - keret} Ft")
        break
    nap += 1   

print("-"*25)

#33. Leghosszabb fagymentes időszak (max_sorozat) Generálj 30 napra téli középhőmérsékleteket (-5 és 10 °C között). Keresd meg a leghosszabb olyan egymást követő napokból álló időszakot (szériát), amikor a hőmérséklet végig fagypont felett maradt (> 0 °C)! Írd ki a leghosszabb fagymentes szakasz hosszát napokban! 
import random
random.seed(42)
homersekletek = [round(random.uniform(-5, 10), 1) for _ in range(30)]
leghosszabb = 0
aktualis = 0
for h in homersekletek:
    if h > 0:
        aktualis += 1
        leghosszabb = max(leghosszabb, aktualis)
    else:
        aktualis = 0
print(f"A leghosszabb fagymentes időszak: {leghosszabb} nap")   


print("-"*25)


#34. Dublikátumok szűrése saját algoritmussal (egyedi_lista) Adott egy 20 elemű lista véletlenszerű számokkal 1 és 15 között (amelyben garantáltan lesznek ismétlődések). Hozz létre egy új listát, amely az eredeti lista elemeit tartalmazza úgy, hogy minden szám csak pontosan egyszer szerepel benne (ne használj beépített set-et, oldd meg ciklussal és feltétellel)!
import random
eredeti = [random.randint(1, 15) for _ in range(20)]
print("Eredeti lista:", eredeti)
unikum = []
for elem in eredeti:
    if elem not in unikum:
        unikum.append(elem)
print("Szűrt lista:  ", unikum)
print(f"\nEredeti hossz: {len(eredeti)}, szűrt hossz: {len(unikum)}")   


print("-"*25)

#35. Két dobókocka eloszlása (kocka_összeg_eloszlas) Dobj 1000 alkalommal egyszerre két kockával, és add össze a dobott pontokat (az összeg 2 és 12 között lehet). Számold meg egy listában, hogy az egyes lehetséges összegek hányszor fordultak elő, majd írasd ki az előfordulások gyakoriságát! Melyik összeg fordult elő a legtöbbször?
import random

gyakorisag = [0] * 13  # index 0 és 1 nem használt
for _ in range(1000):
    osszeg = random.randint(1, 6) + random.randint(1, 6)
    gyakorisag[osszeg] += 1
print("Összeg | Előfordulás | Százalék")
print("-" * 35)
for osszeg in range(2, 13):
    db = gyakorisag[osszeg]
    print(f"  {osszeg:2d}   |     {db:4d}    |  {db / 1000 * 100:.1f}%")
leggyakoribb = max(range(2, 13), key=lambda x: gyakorisag[x])
print(f"\nA legtöbbször előforduló összeg: {leggyakoribb} "
      f"({gyakorisag[leggyakoribb]} alkalommal)")   

print("-"*25)

#36. Pénztárgép címletkifizetés több tétellel (cimlet_kalkulator) A vásárlóknak a 13. feladathoz hasonlóan a legkevesebb bankjeggyel kell visszaadni a visszajárót. Adott a címletek listája csökkenő sorrendben: [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]. Egy bekért visszajáró összegre számold ki egy for vagy while ciklussal, hogy melyik címletből hány darabot kell kiadni!
cimletek = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
osszeg = int(input("Visszajáró összeg (Ft): "))
maradek = osszeg
print(f"\nAz {osszeg} Ft visszajáró:")
for cimlet in cimletek:
    db = maradek // cimlet
    if db > 0:
        print(f"  {db} db × {cimlet} Ft")
    maradek -= db * cimlet
if maradek > 0:
    print(f"  (nem fizethető ki: {maradek} Ft)")   

print("-"*25)

#37. Buborékrendezés lépésről lépésre (rendezes_szimulacio) Generálj egy 10 elemű listát kétjegyű véletlen egész számokból. Rendezd a listát növekvő sorrendbe beépített sort() nélkül, egymásba ágyazott ciklusokkal (szomszédos elemek cseréjével). Írasd ki a listát a rendezés előtt és után is! 
import random
lista = [random.randint(10, 99) for _ in range(10)]
print("Rendezés előtt:", lista)
n = len(lista)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print("Rendezés után:", lista)   

print("-"*25)

#38. Időjárás havi összefoglaló jelentés (havi_meteorologia) Tölts fel egy 30 elemű listát véletlenszerű napi csapadékmennyiségekkel (0 és 35 mm között, ahol a 0 az esőmentes nap). Készíts teljes elemzést: o Hány esős nap volt? o Mennyi volt a havi összkicsapódás? o Hányadik napon esett a legtöbb eső? o Volt-e olyan eset, hogy egymás után 3 napon keresztül esett az eső? 
import random
csapadek = [random.randint(0, 35) for _ in range(30)]
print("Havi csapadékmennyiségek (mm):")
print(csapadek)
print()
eses_napok = [i for i, c in enumerate(csapadek, start=1) if c > 0]
print(f"1. Esős napok száma: {len(eses_napok)} / 30")
osszes = sum(csapadek)
print(f"2. Havi összkicsapódás: {osszes} mm")
max_nap = csapadek.index(max(csapadek)) + 1
max_ertek = max(csapadek)
print(f"3. A legtöbb eső a {max_nap}. napon esett: {max_ertek} mm")
sorozat = 0
max_sorozat = 0
van_3napos = False
for c in csapadek:
    if c > 0:
        sorozat += 1
        if sorozat >= 3:
            van_3napos = True
    else:
        sorozat = 0
    max_sorozat = max(max_sorozat, sorozat)
if van_3napos:
    print(f"4. Igen, volt 3+ egymást követő esős nap! "
          f"(Leghosszabb sorozat: {max_sorozat} nap)")
else:
    print("4. Nem volt 3 egymást követő esős nap.")   

print("-"*25)

#39. Kórházi sorszámos váróterem (sorbanallas_fifo) Szimulálj egy orvosi várótermet egy while ciklussal! A program kínáljon fel menüpontokat: 1. Új beteg érkezett (kérd be a nevét, és fűzd a lista végére); 2. Következő beteg behívása (írd ki a soron következő beteg nevét, majd távolítsd el a lista elejéről); 3. Rendelés vége (kilépés a ciklusból). Ügyelj arra, hogy ha üres a várólista, a 2-es menüpont figyelmeztető üzenetet adjon!
varolista = []
while True:
    print("\n--- Kórházi váróterem ---")
    print("1. Új beteg érkezett")
    print("2. Következő beteg behívása")
    print("3. Rendelés vége")
    valaszt = input("Válasz (1/2/3): ")
    if valaszt == "1":
        nev = input("A beteg neve: ")
        varolista.append(nev)
        print(f"  → {nev} felkerült a listára. (Soron: {len(varolista)} fő)")
    elif valaszt == "2":
        if len(varolista) == 0:
            print("  ⚠ A várólista üres, nincs következő beteg!")
        else:
            kovetkezo = varolista.pop(0)
            print(f"  → {kovetkezo} behívása! (Marad: {len(varolista)} fő)")
    elif valaszt == "3":
        print("A rendelés véget ért. Viszontlátásra!")
        break
    else:
        print("  Érvénytelen választás!")   

print("-"*25)

#40. Bérsávos bérköltség-optimalizálás (ceges_fizetesek) Egy kisvállalkozás 15 dolgozójának havi bérét generáld le 300 000 és 950 000 Ft között. o Különítsd el a dolgozókat 3 kategóriába listák segítségével (junior: 500 000 alatt, medior: 500 000–750 000, senior: 750 000 felett). o Számold ki mindhárom kategória összköltségét és átlagbérét. o Készíts formázott, táblázatos kimenetet a képernyőre, amely soronként kiírja a dolgozó sorszámát, bérét és a hozzárendelt kategóriát! 
import random
berekek = [random.randint(300000, 950000) for _ in range(15)]
junior = []   # < 500 000
medior = []   # 500 000 – 750 000
senior = []   # > 750 000
for i, ber in enumerate(berekek):
    if ber < 500000:
        junior.append((i + 1, ber))
    elif ber <= 750000:
        medior.append((i + 1, ber))
    else:
        senior.append((i + 1, ber))
print(f"{'Sorszám':<10}{'Bér (Ft)':<15}{'Kategória'}")

for i, ber in enumerate(berekek, start=1):
    if ber < 500000:
        kat = "junior"
    elif ber <= 750000:
        kat = "medior"
    else:
        kat = "senior"
    print(f"{i:<10}{ber:<15,}{kat}")
print("\n")

print("KATEGÓRIA-ÖSSZEFOGLALÓ")
print("="*25)
for nev, lista in [("Junior (< 500k)", junior),
                   ("Medior (500k–750k)", medior),
                   ("Senior (> 750k)", senior)]:
    db = len(lista)
    ossz = sum(b for _, b in lista)
    atlag = ossz // db if db > 0 else 0
    print(f"\n{nev}: {db} fő")
    print(f"  Összköltség: {ossz:,} Ft")
    print(f"  Átlagbér:    {atlag:,} Ft")
teljes_ossz = sum(berekek)
print(f"\n{'─' * 40}")
print(f"TELJES HAVI BÉRKÖLTSÉG: {teljes_ossz:,} Ft")   



print("-"*25)