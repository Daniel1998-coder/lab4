import sys
dane=sys.stdin.readline()
plik=open("dane2.txt","w+")
plik.write(dane)
with open("dane2.txt", "r") as plik:
    for linia in plik:
        print(linia,end="")
plik.close()

