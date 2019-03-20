# TP 08/03/2019

# Créer une matrice 4*4 avec des entiers de 0 à 9*
from random import *

def INIT():
    matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            matrix[i][j]=int(9*random())
    return matrix

print(INIT())


#Produit matriciel
def matrixprod(m1,m2):
    n = len(m1); p = len(m1[0]);  q = len(m1[0])
    return [[sum([m1[i][k]*m2[k][j] for k in range(p)]) for j in range(q)] for i in range(n)]

ma=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
mb=[[2,4,6],[8,10,12],[14,16,18]]
print(matrixprod(ma,mb))
