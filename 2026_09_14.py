#3. feladat

fizetes = int(input("Mennyi 1 havi fizetésed forintban? "))
#1. MEGOLDÁS
eves_fizetes = fizetes*12
print(f"Az éves fizetésed: {eves_fizetes} Ft")
#2. MEGOLDÁS
print(f"Az éves fizetésem: {fizetes*12} Ft")

#4. feladat

euro = float(input("Hány forint egy euro a mai nap (pl. 365,86)? "))
mennyit_euroban = int(input("Mennyi eurót akarsz forintra váltani (pl. 100)? "))
forint = int(mennyit_euroban * euro) #pl. 100*365,86 ft
print(f"{mennyit_euroban} euró átváltva forintra az {forint} Ft")

