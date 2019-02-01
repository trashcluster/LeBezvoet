from random import *
# Fonction qui retourne si le tableau est rangé
def _range(a) :
    b = True
    for i in range(len(a)) :
        if i+a[0] != a[i] :
            b=False
    return b

T=[3,4,5,6,7,8,9,10,6,12]
print("le tableau est-il rangé ? ", _range(T))

# fonction de tri à bulle
def _triabulle(a) :
    j=len(a)
    for i in range(len(a)) :
        j-=1
        for k in range(j) :
            if a[k] > a[k+1] :
                a[k],a[k+1] = a[k+1],a[k]
# affiche les étapes d'exécution
#                print("DEBUG :",a)
    return a

# fonction de creation de n entiers aléatoire de 0 à m
def _rantab(n,m) :
    a=[]
    for i in range(n) :
        a.append(int(m*random()))
    return a

# fonction Le lièvre et la Tortue
def _lievre(a) :
    k=0
    for i in range(len(a)) :
        pas=int((len(a)/1.3)**k)
        k+=1
        for j in range(len(a)) :
            if a[j] > a[j+pas] :
                a[j],a[j+pas] = a[j+pas],a[j]


# Affichage des résultats d'éxécution
T=_rantab(10,100)
R=_rantab(50,200)
X=[8,4,7,5,3,1,9,7,6,5]
print("Tableau généré aléatoirement :", T)
print("tableau trié :",_triabulle(T))
print("Tableau généré aléatoirement :", R)
print("tableau trié par l'algorithme du lievre et la tortue:",_lievre(R))



# Execution manuelle
# : [4, 8, 7, 5, 3, 1, 9, 7, 6, 5]
# : [4, 7, 8, 5, 3, 1, 9, 7, 6, 5]
# : [4, 7, 5, 8, 3, 1, 9, 7, 6, 5]
# : [4, 7, 5, 3, 8, 1, 9, 7, 6, 5]
# : [4, 7, 5, 3, 1, 8, 9, 7, 6, 5]
# : [4, 7, 5, 3, 1, 8, 7, 9, 6, 5]
# : [4, 7, 5, 3, 1, 8, 7, 6, 9, 5]
# : [4, 7, 5, 3, 1, 8, 7, 6, 5, 9]
# : [4, 5, 7, 3, 1, 8, 7, 6, 5, 9]
# : [4, 5, 3, 7, 1, 8, 7, 6, 5, 9]
# : [4, 5, 3, 1, 7, 8, 7, 6, 5, 9]
# : [4, 5, 3, 1, 7, 7, 8, 6, 5, 9]
# : [4, 5, 3, 1, 7, 7, 6, 8, 5, 9]
# : [4, 5, 3, 1, 7, 7, 6, 5, 8, 9]
# : [4, 3, 5, 1, 7, 7, 6, 5, 8, 9]
# : [4, 3, 1, 5, 7, 7, 6, 5, 8, 9]
# : [4, 3, 1, 5, 7, 6, 7, 5, 8, 9]
# : [4, 3, 1, 5, 7, 6, 5, 7, 8, 9]
# : [3, 4, 1, 5, 7, 6, 5, 7, 8, 9]
# : [3, 1, 4, 5, 7, 6, 5, 7, 8, 9]
# : [3, 1, 4, 5, 6, 7, 5, 7, 8, 9]
# : [3, 1, 4, 5, 6, 5, 7, 7, 8, 9]
# : [1, 3, 4, 5, 6, 5, 7, 7, 8, 9]
# : [1, 3, 4, 5, 5, 6, 7, 7, 8, 9]
