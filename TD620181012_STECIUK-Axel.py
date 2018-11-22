#TD6
#Somme de 2 dés à n faces
from random import *
from math import *

def nfaces(n) :
    return(int(n*random()+1))

nbfaces=int(input("Entrez le nombre de faces : "))
print(nfaces(nbfaces))
print(nfaces(nbfaces))


#Distances
#Demandes les coordonnés de 3 points à l'utilisateur et affiche la distance entre ces points
def distance(x1, y1, x2, y2) :
    return(sqrt((x2-x1)**+(y2-y1)**))

Ax = int(input("Coordonnées point A en ordonnée : "))
Ay = int(input("Coordonnées point A en obscisse : "))
Bx = int(input("Coordonnées point B en ordonnée : "))
By = int(input("Coordonnées point B en abscisse : "))
Cx = int(input("Coordonnées point C en ordonnée : "))
Cy = int(input("Coordonnées point C en abscisse : "))
AB=distance(Ax, Ay, Bx, By)
BC=distance(Bx, By, Cx, Cy)
AC=distance(Ax, Ay, Cx, Cy)
print("AB",AB)
print("BC",BC)
print("AC",AC)
