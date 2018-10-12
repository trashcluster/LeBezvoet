#TD6
#Somme de 2 dés à n faces
from random import *

def nfaces(n) :
    return(int(n*random()+1))

nbfaces=int(input("Entrez le nombre de faces : "))
print(nfaces(nbfaces))
print(nfaces(nbfaces))
