#vertical : écrir un programme qui prend un mot en entrée et le réécrit verticalement

a = input("entre un mot à écrir verticalement : ")
b = 0
for i in a :
    print(a[b])
    b+=1

#palindrome : teste et affiche une chaine si c'est un palindrome
a = input("entre un mot à tester : ")
b = True
for i in range(len(a)) :
    if a[i] != a[-i-1] :
        b = False
if b == True :
    print(a, "est un palindrome")
else :
    print(a,"n'est pas un palindrome")

# Roue de la fortune : entre un mot, le cacher, le faire deviner en affichant les espaces, les apostrophes et des underscore à la place des lettres cachés
print("Joueur 1")
mot = input("Entre un mot à faire deviner au joueur 2 : ")
devinetemp = []
for i in range(80) :
    print("**************************************************************")
for i in range(len(mot)) :
    if mot[i].isalpha() :
        devinetemp.append('_')
    else :
        devinetemp.append(mot[i])
devine = ''.join(devinetemp)
print("Joueur 2")
while '_' in devine :
    x = input("Entre une lettre ou propose un mot : ")
    if x in mot :
        
