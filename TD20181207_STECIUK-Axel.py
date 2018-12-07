#TD du 07 Decembre 2018 9h-10h
#Suite de Syracuse
#10 premiers nombres = U 0  =  1000
#U 1  =  500
#U 2  =  250
#U 3  =  125
#U 4  =  376
#U 5  =  188
#U 6  =  94
#U 7  =  47
#U 8  =  142
#U 9  =  71
#U 10  =  214
syr=int(input("Antre un nombre à calculer : "))
u=0
umax=0
print("U",u," = ",int(syr))
while syr > 1 :
    if syr%2 == 0 :
        syr/=2
    else :
        syr=syr*3+1
    u+=1
    if umax < syr :
        umax = syr

    print(int(syr))
print("U fin =",u,"U max =",int(umax))

# Jeu de l'oie
from random import *
pos=0
plus=0
while pos!=66 :
    des=int(6*random()+1)+int'6*random()+1)
    print("Tu es sur la case",pos,"Avance de ",des," cases !")
    pos+=des
    if pos%9 == 0 :
        if pos == 63 :
            pos=pos
        else :
            pos+=des
    if pos == 58 :
        pos = 0
    if pos > 66 :
