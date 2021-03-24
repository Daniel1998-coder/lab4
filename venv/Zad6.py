class Robaczek:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def idz_w_gore(self,krok):
        self.y=self.y+krok
    def idz_w_dol(self,krok):
        self.y=self.y-krok
    def idz_w_lewo(self,krok):
        self.x=self.x-krok
    def idz_w_prawo(self,krok):
        self.x=self.x+krok
    def pokaz_gdzie_jestes(self):
        print("X=",self.x,"Y=",self.y)
robaczek=Robaczek(0,0)
print(robaczek.pokaz_gdzie_jestes())
robaczek.idz_w_gore(3)
print(robaczek.pokaz_gdzie_jestes())
robaczek.idz_w_dol(5)
print(robaczek.pokaz_gdzie_jestes())
robaczek.idz_w_prawo(4)
print(robaczek.pokaz_gdzie_jestes())
robaczek.idz_w_lewo(6)
print(robaczek.pokaz_gdzie_jestes())
