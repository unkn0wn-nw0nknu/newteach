barataim = ["Réka", "Réka 2.0", "Réka 3.0", "7 lábú amputált pókica"]
elso_baratom = barataim[0]
print(elso_baratom)

baratok_szama = len(barataim)

print(f"Nekem {baratok_szama} barátom van")

# for barat in barataim:
#     print(barat)

# for sorszam in range(3):
#     print(barataim[sorszam])

van_poki = False

for barat in barataim:
    if barat == "7 lábú amputált pókica":
        van_poki = True

if van_poki:
    print("Van 7 lábú amputált pókica nevű barátom :)")
else:
    print("Nincsen 7 lábú amputált pókica nevű barátom")