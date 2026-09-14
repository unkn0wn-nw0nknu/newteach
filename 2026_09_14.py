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

#6. feladat

r_erteke = int(input("Add meg a kör sugarát: "))
print(f"A kör kerülete: {r_erteke * 3.14} cm")
kor_terulete = 3.14*r_erteke**2
kor_terulete = 3.14*r_erteke*r_erteke
print(f"A kör terulete: {kor_terulete} cm")
