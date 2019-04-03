
#TP 15/03/2019
from random import *

#Crée une matrice
def matrix (col, ligne, max) :
    arr = [[int(max*random()) for i in range(col)] for j in range(ligne)]
    return arr

#somme de matrices
def matrixsum (m1,m2) :
    mx = [[0 for i in range(len(m1))] for j in range(len(m1[0]))]
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            mx[i][j] = m1[i][j]+m2[i][j]
            #mx[i][j] = 5
    return mx

matrix1=matrix(10,10,4)
matrix2=matrix(10,10,4)
matrix3=matrixsum(matrix1,matrix2)
print(matrix1)
print(matrix2)
print(matrix3)

#triangle de pascal
def pascale(n):
    mx=[[0 for j in range(n+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==j or j==0:mx[i][j]=1
    for i in range(2,n+1):
        for j in range(1,n+1):
            if j<i:
                mx[i][j]=mx[i-1][j]+mx[i-1][j-1]
    for i in range(n+1):
        for j in range(n+1):
            if mx[i][j]!=0:
                if mx[i][j]<10:s="    "
                elif mx[i][j]<100 :s="   "
                elif mx[i][j]<1000 :s="  "
                else :s=" "

                print(mx[i][j],end=s)
        print()
print(pascale(3))
