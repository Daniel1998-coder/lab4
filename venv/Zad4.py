class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jedn):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jedn=cena_jedn
    def wyswietl_produkt(self):
        print(self.nazwa_produktu,", ",self.ilosc,", ",self.jednostka_miary,", ",self.cena_jedn)
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    def ile_kosztuje(self):
        cena=self.ilosc*self.cena_jedn
        print(cena)
Czekolada=NaZakupy("Czekolada",3,"Kilogramy",5)
print(Czekolada.wyswietl_produkt())
print(Czekolada.ile_produktu())
print(Czekolada.ile_kosztuje())
