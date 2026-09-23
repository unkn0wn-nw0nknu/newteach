barataim = ["A", "B", "C"]
#egy tömb elemszáma 0-tól a végtelenig lehet
print(barataim[-1])
print(barataim[0]) #sorszámozás 0-tól kezdődik, output: E
print(barataim[1])
print(barataim[2])
#print(barataim[3]) #List item out of range,a tömbnél többedik elemet akarjuk = hiba

ures_tomb = []
print(ures_tomb)

#tömbök kiiratása
print(barataim)

# Feladat: Hozz létre egy tömnöt a kedvenc videójátékok/sorozatok/hobbi dolgokról 4-6 elem

kedvenceim = ["Kakaós palacsinta", "Rizskoch", "Trappista sajt", "Csokis keksz", "Sztracsatella fagyi"]
print(f"Nekem {len(kedvenceim)} kedvenc kajám van.") #len (length) kiirja mennyi elem van egy tömbben.

#for ciklus
#for <változó név> in <tömb>
for kaja in kedvenceim:
    print(kaja)

#range
#egész szám, 0-tól kezdi 
#elszámolunk 5-ig
#range(6) gyakorlatilag egy tömb [0,1,2,3,4,5]
for szam in range(6):
    print(szam)

# for szam in range(6000000):
#     print(szam)

#A rangenak nem csak vég értéke van, hanem meg lehet adni, honnan kezdődjön
for eletkor in range(0, 99):
    if eletkor < 18:
        print("Kiskorúak nem léphetnek be! >:)")
    else:
        print("Felnőtt vagy! Bemehetsz! :D")
        break #kilép a ciklusból

#a range()-nek van egy harmadik paramétere: lépésköz, mennyivel növekedjen az érték 1 helyett
#pl. felsorolom az összes 3-mal osztható számot 0-300-ig
for szam in range(0, 301, 3):
    print(szam*3)

    #írjuk ki: 1*3 = 3
    # 2*3 = 6
