class Auto: #class <osztalyNeve>
    def __init__(self, _marka, _tipus, _ar, _loero, _mikor_hasznalom): 
        #konstruktor, ha ez nincs, nem tudsz autót létrehozni
        self.marka = _marka
        self.tipus = _tipus
        self.loero = _loero
        self.ar = _ar       
        self.mikor_hasznalom = _mikor_hasznalom

    #viselkedés/metódus (ezek függvények btw)
    def gyorsul(self):
        print("vroom vroom")

    def fekez(self):
        print(f"A {self.marka} {self.tipus}-om lelassul")


#öröklődés - inheritance
class Teherauto(Auto): #Auto a szülőosztály, megkapja az Auto tulajdonságait.
    def __init__(self, _marka, _tipus, _ar, _loero, _mikor_hasznalom, 
                 _suly, _magassag
                 ): #adunk új tulajdonságokat
        super().__init__(_marka, _tipus, _ar, _loero, _mikor_hasznalom)

        self.suly = _suly
        self.magassag = _magassag

    #Auto gyorsul metódust felülirjuk
    def gyorsul(self):
        print("brrrr brrrrr")

    #egy új metódus
    def felpakolt_auto(self):
        print("Árú bepakolva a teher autóba.")
        print(f"Eredeti súly: {self.suly} kg")
        print(f"Pakolás utáni súly: {self.suly * 1.5} kg")


# INICIALIZÁLÁS - példányosítás
auto = Auto("Suzuki", "Swift", 2, 5000, ["munkába menet", "trdggvtgvxfcdt", "palacsinta sütéskor"])
auto.gyorsul() #kiirja, hogy vroom vroom
auto.fekez()
print(f"Az én autóm egy {auto.marka} {auto.tipus} amit {auto.mikor_hasznalom[-1]} használok.")

#létrehozunk 1 teherautót
teher_auto = Teherauto("Ford", "Transit", 200, 10000000,
                       ["szállításhoz", "költözéshez"], 1500, 2.30)
teher_auto.gyorsul()
teher_auto.felpakolt_auto()

