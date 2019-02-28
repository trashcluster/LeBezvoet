from random import *
#Fonction qui sors un tableau de n longueur avec des caractères ascii miniscules
def _rantab(n) :
    a=[]
    for i in range(n) :
        a.append(chr(int(26*random()+ 97)))
    return a
#1 affiche une page (2500 caractères)
print(_rantab(2500))

#2 affiche un tome (1000 pages)
for i in range(1000):
    print(_rantab(2500))
