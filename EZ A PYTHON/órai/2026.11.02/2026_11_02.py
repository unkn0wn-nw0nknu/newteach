with open('dolgozok.txt', 'r', encoding='utf-8') as f:
    fejlec = f.readline()

    for sor in f:
        adatok = sor.strip().split(';') 

        nev = adatok[0]
        varos = adatok[1]
        reszleg = adatok[2]
        
        print(f"Dolgozó: {nev} ({varos}) - {reszleg}")   