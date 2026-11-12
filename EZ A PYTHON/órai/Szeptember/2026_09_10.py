print("Hello Világ >:)")

#változók

#string
nev = "Veronika"
print(type(nev)) #type() visszaadja a var tipusát

#integer/int
eletkor = 16
print(type(eletkor))  #type() visszaadja a var tipusát

#float
tomeg = 67.6767676767676767676767676767676767676767
print(type(tomeg))  #type() visszaadja a var tipusát
print(tomeg)

#boolean
szeretek_programozni = True
print(type(szeretek_programozni))

#char (string)
betu = "a"
print(type(betu))

#szöveg bekérés felhasználótól
nev = input("Mi a neved? ")
print(f"Helló, {nev}!")

if nev == "": #csak HA entert nyomtál
    print("HIBA: Nem adtad meg a neved")
else:
    print(f"Helló, {nev}!")

eletkor = int(input("Hány éves vagy? ")) #kell egy int() az input köré
print(f"{nev} a nevem és {eletkor} éves vagyok")

#KOMMENTELÉS: jelöld ki a sorokat, és CTRL + C + K egyszerre
#operátorok
#egymásba ágyazott elágazások
if eletkor > 0: #ha az életkor kisebb mint 0, azaz -1, -2... stb, az nem jó
    if eletkor > 18: #HA NAGYOBB ( > ), mint 18
        print("Felnőtt vagyok")

    elif eletkor == 18:
        print("Pont 18 éves vagyok")

    else: #ha nem nagyobb és nem egyenlő akkor kisebb
        print("Nem vagyok felnőtt még!")

else:
    print("HIBA: Nem lehet negativ az életkorod")