from random import *
#Fonction qui sors un tableau de n longueur avec des caractères ascii miniscules
def _rantab(n) :
    a=[]
    for i in range(n) :
        a.append(chr(int(26*random()+97)))
    return a

def _ranstr(n) :
    a=''
    for i in range(n) :
        a+=(chr(int(26*random()+97)))
    return a
#1 affiche une page (2500 caractères)
print(_rantab(2500))

#2.1 affiche un tome (1000 pages) et cherche le mot bts
#page=[]
#for i in range(1000):
#    check=(_rantab(2500))
#    for j in range(len(check)):
#        if check[j] == 'b':
#            if check[j+1] == 't':
#                if check[j+2] == 's':
#                    check[j]='B'
#                    check[j+1]='T'
#                    check[j+2]='S'
#                    page.append(i)
#    print(check, page)

#3 cherche mon nom (AXEL) dans tout les tomes qu'il faudra pour le trouver
page=[]
all=0
noms=['abdillah','ines','loic','rayene','kilian','maxime','thomas','erwann','luc','oceane','romuald','evann','gaetan','mathieu','alexis','lucas','yanis','vivien','damien','nadir','thibault','tristan','margaux','justin','hugo','dylan','axel','alicia','guillaume','joel']
noms2=[]
tome=0
while all < len(noms):
    tome+=1
    for i in range(1000):
        check=(_ranstr(2500))
        for k in range(len(noms)):
            if noms[k] in check :
                #page.append(i)
                if len(noms[k]) == 6 :
                    print ('Waouh !')
                elif len(noms[k]) == 7 :
                    print ('Incroyable !')
                elif len(noms[k]) == 8 :
                    print ('Miracle !')
                    print('trouvé', noms[k])
                if noms[k] not in noms2:
                    noms2.append(noms[k])
                    all+=1
                    page.append(tome)
                    page.append(i)
                    print(noms2)
                    print('trouvé', all, '/', len(noms), '    tome, pages : ',page)

#4 cherche le nom des élèves dans un tome
