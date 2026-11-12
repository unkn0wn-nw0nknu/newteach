with open("dolgozok.txt", "r", encoding="utf-8") as fajl_sorok: #képlet: with open("fajl_neve", "R", encoding="utf-8") as <valtozo_nev>:
    for fajl_sor in fajl_sorok:
        print(fajl_sor)

        darabok = fajl_sor.split(';') #ha nem irunk semmmit a zárójelbe, akkor a ; mentén szedi szét a sort egy listává

        nev = darabok[0] #első oszlop
        varos = darabok[1] #második oszlop
        reszleg =darabok[2] #harmadik oszlop

        print(darabok)