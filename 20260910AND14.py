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

if nev == "":
    print("HIBA: Nem adtad meg a neved")
else:
    print(f"Helló, {nev}!")
