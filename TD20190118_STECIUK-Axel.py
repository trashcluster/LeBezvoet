# cadavre exquis
from random import *

def A():
    return int(5*random());

lieu=['chez lui','à paris','sur un pont','sur la banquise','à la maison blanche']
nom=['Benjamin','Paul','Olivier','Marianne','trump']
verbe=['mange','asseoit','peint','prend','dirige']
adverbe=['rapidement','lentement','jamais','calmement','gentillement']
mot=['lapin','mouette','mug','voiture','pays']
adjectif=['bleu','long','noble','parleur','noir']
nombre=int(10*random())
print(lieu[A()],nom[A()],verbe[A()],adverbe[A()],nombre,mot[A()],adjectif[A()])

#Maximum
#tabl=[]
#maxCount=int(0)
#maxNumA=int(0)
#maxNum=int(0)
#for i in range(8):
#    x=int(input("Entre un nombre : "))
#    tabl.append(x)
#for i in tabl :
#    maxNumA = maxNum
#    if maxNum < tabl[i] :
#        maxNum=tabl[i]
#        maxCount=1
#    if maxNumA == maxNum :
#        maxCount+=1
#print("Maximum :", maxNum,"Nombre d'occurences :", maxCount)

# loto
def tirer():
    num=int()
    global tirage
    tirage=[]
    num=int(49*random()+1)
    tirage.append(num)
    for i in range(4) :
        while num in tirage :
            num=int(49*random()+1)
        tirage.append(num)
        return tirage

loto=[]
juste=int()
for i in range(5) :
    x=int(input("Entre un numero : "))
    loto.append(x)
for j in range(10) :
    tirer()
    print(loto, tirage)
    if loto == tirage :
        juste+=1
print("Nombre de fois où votre tirage est passé : ",juste)
