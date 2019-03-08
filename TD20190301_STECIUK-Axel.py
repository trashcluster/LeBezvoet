from random import *
#Tri par selection
#rantab génère un tableau de n entiers de 0 à m
def rantab(n,m):
    a=[]
    for i in range(n):
        a.append(int(m*random()))
    return a

#selectri effectue un tri par selection
def selectri(L):
    for i in range(len(L)):
        for j in range(i,len(L)):
            if(L[i]>L[j]):
                L[i],L[j]=L[j],L[i]
        #print(L)
    return L

#insertri effectue un tri par insertion
def insertri(L):
    for i in range(1,len(L)):
        k=L[i]
        j=i-1
        while j>=0 and k<L[j]:
            L[j+1]=L[j]
            j-=1
        L[j+1]=k
        #print(L)
    return(L)


#1.1
#[1, 10, 8, 3, 6, 1, 4, 10, 9, 8]
#[1, 1, 10, 8, 6, 3, 4, 10, 9, 8]
#[1, 1, 3, 10, 8, 6, 4, 10, 9, 8]
#[1, 1, 3, 4, 10, 8, 6, 10, 9, 8]
#[1, 1, 3, 4, 6, 10, 8, 10, 9, 8]
#[1, 1, 3, 4, 6, 8, 10, 10, 9, 8]
#[1, 1, 3, 4, 6, 8, 8, 10, 10, 9]
#[1, 1, 3, 4, 6, 8, 8, 9, 10, 10]
#[1, 1, 3, 4, 6, 8, 8, 9, 10, 10]
#[1, 1, 3, 4, 6, 8, 8, 9, 10, 10]

#1.2
L=[1,10,8,3,6,1,4,10,9,8]
print (selectri(L))
x=rantab(25,98)
print(x)
print(selectri(x))

#2.1
#[1, 10, 8, 3, 6, 1, 4, 10, 9, 8]
#[1, 8, 10, 3, 6, 1, 4, 10, 9, 8]
#[1, 3, 8, 10, 6, 1, 4, 10, 9, 8]
#[1, 3, 6, 8, 10, 1, 4, 10, 9, 8]
#[1, 1, 3, 6, 8, 10, 4, 10, 9, 8]
#[1, 1, 3, 4, 6, 8, 10, 10, 9, 8]
#[1, 1, 3, 4, 6, 8, 10, 10, 9, 8]
#[1, 1, 3, 4, 6, 8, 9, 10, 10, 8]
#[1, 1, 3, 4, 6, 8, 8, 9, 10, 10]
#[1, 1, 3, 4, 6, 8, 8, 9, 10, 10]

#2.2
L=[1,10,8,3,6,1,4,10,9,8]
print (insertri(L))
x=rantab(25,98)
print(x)
print(insertri(x))
