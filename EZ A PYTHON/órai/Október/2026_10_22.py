class Kutya:
    def __init__(self, _nev, _fajta, _nem, _szor_szine):
        self.nev = _nev
        self.fajta = _fajta
        self.nem = _nem
        self.szor_szine = _szor_szine

    #viselkedés/metódus
    def ugat(self):
        print("vau vau")

#példányosítás
kutyi = Kutya("Joghurt", "Keverék", "kisfiú", "Fehér-vajszínű")
for i in range(13): 
    kutyi.ugat()
#alosztály
class FranciaBulldog(Kutya): 
    #megkapja a kutya osztály metódusait és tulajdonságát
    def __init__(self, _nev, _fajta, _nem, _szor_szine, 
                 _eletkor, _miket_csinal, _suly):
        #a felső def initbe írjuk az új tulajdonságokat
        #nem a super initbe
        super().__init__(_nev, _fajta, _nem, _szor_szine)
        #itt soroljuk fel az új tulajdonságokat
        #tulajdonság = property
        #property = prop
        self.eletkor = _eletkor
        self.miket_csinal = _miket_csinal
        self.suly = _suly

    def ugat(self): #felülírom a kutya ugat() metódusát
        print("Woof woof")

    #még egy
    def megetet(self, kaja_mennyiseg):
        if (kaja_mennyiseg < 50): #ha kevesebb mint 50g
            print("Kösz a jutalmat >:(")
        else:
            print("Kösz hogy nem hagytál éhezni >:((((")

#példányosítás - inicializálás
#franciabulldog létrehozása
XI_Anjou_Bela_diktator = FranciaBulldog("XI. Anjou Béla Diktátor", "Francia Bulldog", "kislány", "tarka", 3, 
                                        ["eszik", "uralkodik", "mindenkit a szolgájává tesz"], 300)
XI_Anjou_Bela_diktator.ugat()
mennyi_kajat_adjak = int(input(f"Hány nanogramm kaját kapjon {XI_Anjou_Bela_diktator.nev}? "))
XI_Anjou_Bela_diktator.megetet(mennyi_kajat_adjak)