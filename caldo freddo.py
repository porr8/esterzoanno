"""data una lista di 20 elementi di temperature randomiche nell'intervallo -20, 40,
caclcolare il numero di elementi sopra lo 0, sotto lo 0 e stampare a video la scritta
freddo estremo se le temperature sotto lo 0 superano quelle sopra, caldo estremo nell'altro caso"""

listatempe=[]
import random
for i in range(0,20):
    listatempe.append(random.randint(-20,40))
sopz=0
sotz=0
for i in range(0,20):
    if listatempe[i]>0:
        sopz=sopz+1
    else:
        sotz=sotz+1
        
if sotz>sopz:
    print("freddo estremo")
elif sopz>sotz:
    print("caldo estremo")
else:
    print("temperatura nella norma")
