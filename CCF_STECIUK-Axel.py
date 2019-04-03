# 5
# Fonction sommeChiffre

def sommeChiffre(chaine):
    n=len(chaine)
    somme=0
    for i in range(n):
        a=int(chaine[i])
        somme=somme+a
    return somme

#Test de la fonction : somme = 45
print("somme : ", sommeChiffre([1,2,3,4,5,6,7,8,9]))


#6
#fonction etape1
def etape1(chaine):
    n=len(chaine)
    chainebis=[]
    for i in range(15):
        if i%2==0 :
            a = chaine[i]*2
            if a>9 :
                a = a-9
        else :
            a = chaine[i]
        chainebis.append(a)
    return chainebis


#test de la Fonction
print("etape1 : ",etape1([4,9,7,0,1,2,3,4,5,6,7,8,9,0,1]))

#def algo de luhn
def luhn(chaine):
    luhn=10-(sommeChiffre(chaine)%10)
    return luhn

#test algo de luhn
print("luhn : ", luhn(etape1([4,9,7,0,1,2,3,4,5,6,7,8,9,0,1])))

#fonction pour entrer un numer de carte
def carte(n):
    carte=[]
    for i in range(n):
        x=int(input("entre le numero de la carte : "))
        carte.append(x)
    return(carte)

#print("luhn : ", luhn(etape1(carte(16))))

crt=carte(16)
res=luhn(etape1(crt))
if res[-1] != crt[-1]:
    print("le numer ode carte saisi n'est pas bon")
    print(crt)
    print(res)
