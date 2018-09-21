from random import *
#1A
#Nombre au hasard entre 1 et 6
print (int(6*random()+1))

#1B
#Affiche 5 lettres de l'alphabet en majuscule aleatoirement
for i in range(5):
    print (chr(int(25*random()+65)))

#2A
#Converti des secondes en hh:mm:ss
j = int(input("Entrez le nombre de secondes : "))
#k = l = int(0)
#while j >= 60:
#    j/60=j
#    k = k+1
#    while k >= 60:
#        k/60=k
#        l = l+1
#print (j + ":" + k + ":" + l)
h = j/3600
m = (j-(3600*h))/60
s = j%60
print(int(h),":",int(m),":",s)

#2B
#Deniers vers Deniers,Sous,Livres
init = int(input("Entre le nombre de denieers : "))
livres = init/240
#sous = (init-240*livres)/12
sous = init%20
deniers = init%12
print(int(livres)," Livres ",int(sous)," Sous ",int(deniers)," Deniers")
input()
