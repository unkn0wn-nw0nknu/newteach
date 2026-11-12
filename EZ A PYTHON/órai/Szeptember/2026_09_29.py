# 1. Számlálás visszafelé (visszaszamlalas) Írj programot, amely egy újévi visszaszámlálást szimulál: írja ki a számokat 10-től 1-ig csökkenő sorrendben, majd a végén jelenítse meg a „Boldog új évet!” feliratot! 
for i in range(10, 0, -1):
    print(i)
print("Boldog új évet!")   

# 2.Kétpontos dobások (kosarlabda) Egy kosaras minden edzésen 15 dobást kísérel meg. Szimuláld le véletlenszámokkal (0: kimaradt, 1: sikeres) a dobásokat, tárold el egy listában, majd írd ki, hány sikeres dobása volt! 
import random
dobasok = [random.randint(0, 1) for _ in range(15)]
print("Dobások:", dobasok)
print(f"Sikeres dobások száma: {dobasok.count(1)}")   

# 3. Heti zsebpénz (zsebpenz) Kérd be a felhasználótól egymás után a hét 7 napján kapott vagy költött összegeket, mentsd el egy listába, majd határozd meg a hét végén megmaradt egyenleget (sum)! 
zsebpenzek = []
for nap in range(7):
    osszeg = int(input(f"{nap + 1}. nap zsebpénze (pénz +, költés -): "))
    zsebpenzek.append(osszeg)
print("Egyenleg a hét végén:", sum(zsebpenzek))   

# 4. Heti hőmérsékletek (homerseklet_alap)  Hozz létre egy 7 elemű listát a hét mért napi középhőmérsékleteivel (10 és 25 °C közötti egész számok). Határozd meg és írd ki a hét legmelegebb napjának hőmérsékletét (max)!
homersekletek = [15, 18, 22, 25, 20, 14, 12]
print("Heti hőmérsékletek:", homersekletek)
print(f"A legmelegebb nap hőmérséklete: {max(homersekletek)} °C")   

# 5. Kockadobás szimuláció (kocka_statisztika) Dobj egy szabályos dobókockával 20 alkalommal véletlenszerűen (1–6). A dobásokat fűzd egy listába, majd írd ki, hányszor sikerült 6-ost dobni!
import random
dobasok = [random.randint(1, 6) for _ in range(20)]
print("Dobások:", dobasok)
print(f"Hányszor 6-ost dobtál: {dobasok.count(6)}")   

#6.PIN-kód generátor (pinkod) Generálj egy 4 számjegyből álló véletlenszerű PIN-kódot úgy, hogy a számjegyeket (0–9) egyenként egy listába teszed, majd kiírod őket egy sorban, egymás mellé!
import random
pin = []
for i in range(4):
    pin.append(random.randint(0, 9))
print("PIN-kód:", pin)
for jegy in pin:
    print(jegy)
print()   

# 7. Bevásárlólista bekérése (bevasarlolista) Kérj be a felhasználótól 5 terméket for ciklussal, tedd őket egy listába, majd írasd ki sorszámozva (1-től 5-ig) a képernyőre!
termek = []
for i in range(5):
    termek.append(input(f"{i + 1}. termék: "))
print("\nBevásárlólista:")
for i, t in enumerate(termek, 1):
    print(f"{i}. {t}")   

# 8. Pozitív bemenet ellenőrzése (pozitiv_szam) Kérj be a felhasználótól egy pozitív egész számot while ciklussal! Addig ismételd a bekérést, amíg a felhasználó valóban 0-nál nagyobb értéket nem ad meg! 
szam = 0
while szam <= 0:
    szam = int(input("Adj meg egy pozitív egész számot: "))
print("A megadott szám:", szam)   

# 9. Kávéautomata visszajáró (penzbedobas) Egy kávé ára 350 Ft. A program kérjen be pénzérméket a felhasználótól addig egy while ciklussal, amíg a bedobott összeg el nem éri vagy meg nem haladja a 350 Ft-ot. A végén írja ki a visszajáró összegét! 
ar = 350
osszeg = 0
while osszeg < ar:
    erme = int(input(f"Bedobott érme (még {ar - osszeg} Ft kell): "))
    osszeg += erme
print(f"Visszajáró: {osszeg - ar} Ft")   


# 10. Lépésszámláló átlag (lepesszamlalo) Generálj egy 7 napos hétre napi lépésszámokat (3000 és 12 000 között). Számold ki és írd ki a heti átlagos lépésszámot (len és sum segítségével)!
import random
lepesekek = [random.randint(3000, 12000) for _ in range(7)]
print("Napi lépésszámok:", lepesekek)
print(f"Heti átlagos lépésszám: {sum(lepesekek) / len(lepesekek):.0f}") 


# 11. Páros villamosjáratok (villamos_szures) Adott egy lista a belvárosi járatok számaival: [2, 4, 19, 47, 49, 56, 62]. Készíts egy új listát, amely csak a páros járatszámokat tartalmazza!
jaratok = [2, 4, 19, 47, 49, 56, 62]
paros_jaratok = []
for jarat in jaratok:
    if jarat % 2 == 0:
        paros_jaratok.append(jarat)

print("Páros járatszámok:", paros_jaratok)   

# 12. Ötöslottó számhúzás egyszerűen (lottosorsolas) Generálj 5 darab véletlenszámot 1 és 90 között egy listába. (Itt még nem kötelező vizsgálni, hogy van-e köztük egyforma.) Írasd ki a számokat növekvő sorrendbe rendezve!
import random
lotto = [random.randint(1, 90) for _ in range(5)]
lotto.sort()
print("Lottószámok:", lotto)   

# 13. Jelszó megerősítés (jelszo_ellenorzes) Kérj be egy jelszót a felhasználótól, majd kérd meg, hogy gépelje be újra a megerősítéshez. Addig kérd újra a megerősítést while ciklussal, amíg a két szöveg pontosan meg nem egyezik!
jelszo = input("Adj meg egy jelszót: ")
megerosit = input("Gépeled be újra a jelszót: ")
while megerosit != jelszo:
    print("A jelszavak nem egyeznek meg!")
    megerosit = input("Gépeled be újra a jelszót: ")
print("A jelszó sikeresen megerősítve!")   

# 14. Tantárgyi átlag (jegyek_atlaga) Kérj be a felhasználótól 1 és 5 közötti érdemjegyeket addig, amíg 0-t nem ír be (végjel). A jegyeket mentsd el egy listába, és a végén jelenítsd meg a tantárgy átlagát!
jegyek = []
while True:
    jegy = int(input("Érdemjegy (1-5, 0 = vég): "))
    if jegy == 0:
        break
    jegyek.append(jegy)

print(f"Jegyek: {jegyek}")
print(f"Tantárgy átlaga: {sum(jegyek) / len(jegyek):.2f}")   

# 15. Hétvégi fagy (fagyos_napok) Generálj 14 napra téli hőmérsékleti adatokat (-10 és 8 °C között). Számold meg és írd ki, hány olyan nap volt, amikor fagyott (0 °C alatti hőmérséklet)!
import random

homersekletek = [random.randint(-10, 8) for _ in range(14)]

fagyos = 0
for h in homersekletek:
    if h < 0:
        fagyos += 1

print("Napi hőmérsékletek:", homersekletek)
print(f"Fagyos napok száma: {fagyos}")   

# 16. Névsor keresés (nevkereses) Tölts fel egy listát 6 osztálytárs nevével. Kérj be egy keresett nevet, és az in vagy egy for ciklus segítségével döntsd el, hogy szerepel-e a névsorban!
nevek = ["Anna", "Bence", "Csilla", "Dávid", "Emese", "Ferenc"]
keresett = input("Keresett név: ")
if keresett in nevek:
    print(f"A(z) {keresett} szerepel a névsorban!")
else:
    print(f"A(z) {keresett} NEM szerepel a névsorban!")   

# 17. Fej vagy írás széria (fejvagyiras) Dobj fel egy virtuális érmét 10-szer (0: Fej, 1: Írás). Írd ki a dobások sorrendjét, majd a végén összesítsd, hogy a Fej vagy az Írás fordult-e elő többször!
import random
dobasok = [random.randint(0, 1) for _ in range(10)]
print("Dobások:", dobasok)
fej = dobasok.count(0)
iras = dobasok.count(1)
print(f"Fej: {fej}, Írás: {iras}")
if fej > iras:
    print("A Fej fordult elő többször!")
elif iras > fej:
    print("Az Írás fordult elő többször!")
else:
    print("Egyenlő arányban fordultak elő!")   

# 18. Gyorshajtók listája (gyorshajtas) Egy 50 km/h-s zónában a traffipax a következő sebességeket rögzítette: [48, 55, 62, 50, 45, 71, 52]. Válogasd ki egy új listába a megengedett sebességet túllépő értékeket!
sebessegek = [48, 55, 62, 50, 45, 71, 52]
korlimit = 50
gyorshaitok = []
for s in sebessegek:
    if s > korlimit:
        gyorshaitok.append(s)
print("Gyorshajtók:", gyorshaitok)   

#19. Kuponkód generálás (kuponkod) Készíts egy programot, amely előállít egy 6 tagú számsort véletlenszámokból (1–9 között), és összekapcsolja őket egyetlen kuponkódszöveggé (pl.: 5-2-9-1-4-8)!
import random

kupon = [str(random.randint(1, 9)) for _ in range(6)]
kod = "-".join(kupon)
print("Kuponkód:", kod)   


 # 20. Megtakarítás növekedése (malacpersely) Egy diák 5 000 Ft-tal kezdi a hónapot, és mindennap 200 Ft-ot tesz a perselyébe. Ciklus segítségével számold ki és írasd ki napról napra az egyenlegét a 30 napos hónap során!
egyenleg = 5000
for nap in range(1, 31):
    egyenleg += 200
    print(f"{nap}. nap: {egyenleg} Ft")   

# 21. Egyedi ötöslottó sorsolás (egyedi_lotto) Generálj 5 darab lottószámot 1 és 90 között úgy, hogy nem lehet köztük ismétlődés! Használj while ciklust a generáláshoz, és csak akkor fűzd az új számot a listához, ha még nem szerepel benne!
import random
lotto = []
while len(lotto) < 5:
    szam = random.randint(1, 90)
    if szam not in lotto:
        lotto.append(szam)
lotto.sort()
print("Lottószámok:", lotto)   

# 22. Számkitaláló játék barkochba stílusban (barkochba) A gép gondoljon egy egész számra 1 és 100 között. A felhasználó próbálja kitalálni: a program minden tipp után mondja meg, hogy a gondolt szám kisebb vagy nagyobb-e! A játék akkor ér véget, ha eltalálta; írja ki a szükséges próbálkozások számát is!

import random
gondolt = random.randint(1, 100)
probalkozas = 0
print("Gondoltam egy számot 1 és 100 között!")
while True:
    tipp = int(input("Tipp: "))
    probalkozas += 1

    if tipp < gondolt:
        print("Nagyobb!")
    elif tipp > gondolt:
        print("Kisebb!")
    else:
        print(f"Eltaláltad! {probalkozas} próbálkozás volt szükséges.")
        break   

# 23. Családi villanyszámla analízis (aramfogyasztas) Adott 12 hónap kWh-ban mért villanyfogyasztása egy listában. Keresd meg a legkisebb és a legnagyobb fogyasztású hónap sorszámát (1–12), valamint számold ki az éves átlagot!

fogyasztas = [320, 280, 250, 200, 150, 120, 110, 130, 180, 220, 290, 350]
min_idx = 0
max_idx = 0
for i in range(1, 12):
    if fogyasztas[i] < fogyasztas[min_idx]:
        min_idx = i
    if fogyasztas[i] > fogyasztas[max_idx]:
        max_idx = i
print(f"Legkisebb fogyasztás: {min_idx + 1}. hónap ({fogyasztas[min_idx]} kWh)")
print(f"Legnagyobb fogyasztás: {max_idx + 1}. hónap ({fogyasztas[max_idx]} kWh)")
print(f"Éves átlag: {sum(fogyasztas) / len(fogyasztas):.1f} kWh")   


# 24. Banki egyenleg és fedezet (bankautomata_szimulacio) 
# A számlaegyenleg kezdetben 50 000 Ft. A felhasználó addig vehet fel pénzt 
# (vagy adhat meg negatív összeget befizetésként), amíg a 0 értéket nem 
# adja meg, vagy le nem fogy a számlája. Ha többet kérne, mint a meglévő 
# egyenleg, a program utasítsa el a tranzakciót és írjon hibaüzenetet!

egyenleg = 50000

while egyenleg > 0:
    osszeg = int(input("Adja meg a befizetendő (+) / felvételi (−) összeget (0 a kilépéshez): "))

    if osszeg == 0:
        break

    if osszeg > 0:
        # Befizetés
        egyenleg += osszeg
        print(f"Befizetés sikeres! Új egyenleg: {egyenleg} Ft")
    else:
        # Felvétel
        kivenni = abs(osszeg)
        if kivenni > egyenleg:
            print(f"HIBA: Nem elegendő fedezet! Kérte: {kivenni} Ft, egyenleg: {egyenleg} Ft")
        else:
            egyenleg -= kivenni
            print(f"Felvétel sikeres! Új egyenleg: {egyenleg} Ft")

print(f"Számlaegyenleg: {egyenleg} Ft")

# 25. Dolgozatok statisztikája (osztalyzat_statisztika) 
# Generálj egy 25 fős osztály dolgozatpontszámait (0–100 pont). A 23. feladat 
# ponthatárai (elégtelen: 0–42, elégséges: 43–57, közepes: 58–72, jó: 73–87, 
# jeles: 88–100) alapján határozd meg, melyik érdemjegyből hány darab 
# született, és írd ki az eredményt! 

pontok = [random.randint(0, 100) for _ in range(25)]

def ertekelo(pont):
    if pont <= 42:
        return "elégtelen"
    elif pont <= 57:
        return "elégséges"
    elif pont <= 72:
        return "közepes"
    elif pont <= 87:
        return "jó"
    else:
        return "jeles"

eredmeny = {}
for pont in pontok:
    jegy = ertekelo(pont)
    eredmeny[jegy] = eredmeny.get(jegy, 0) + 1

for jegy in ["elégtelen", "elégséges", "közepes", "jó", "jeles"]:
    darab = eredmeny.get(jegy, 0)
    print(f"{jegy:<12}: {darab} db")

print(f" Összesen:{sum(eredmeny.values())} db")

# 26. Két lista összehasonlítása – Közös hobbik (kozos_elemek) 
# Adott két tanuló hobbijainak listája (pl. ["foci", "rajz", "olvasás", "zene"] és 
# ["zene", "túra", "foci", "úszás"]). Ciklussal keresd meg és gyűjtsd ki egy 
# harmadik listába azokat a tevékenységeket, amelyek mindkettejük 
# listájában megtalálhatók!

A = ["foci", "rajz", "olvasás", "zene"]
B = ["zene", "túra", "foci", "úszás"]

közös_elemek = list(set(A) and set(B))

print(közös_elemek)
