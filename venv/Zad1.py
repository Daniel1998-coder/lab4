from random import seed
from random import randint
seed(0)
plik =open("dane.txt", "w+")
for _ in range(6):
    value =randint(0,30)
    plik.write(str(value * 2,))
plik.close()