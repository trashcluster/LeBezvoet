#Barcelone=messi=Paris
#paris=mbappe=liverpool
#liverpool=salah=Juventus
#juventus=ronaldo=Barcelone

#programme transferts

barcelone = 'Ronaldo'
juventus = 'Salah'
liverpool = 'Mbappe'
paris = 'Messi'

print(barcelone,' joue à Barcelone,',juventus,' à la Juventus,',liverpool,' à Liverpool et ',paris,' à Paris.')

ajaccio = barcelone
barcelone = paris
paris = liverpool
liverpool = juventus
juventus = ajaccio

print(barcelone,' joue à Barcelone,',juventus,' à la Juventus,',liverpool,' à Liverpool et ',paris,' à Paris.')

#programme conversion_binaire_decimal
# les variables seront a,b,c,d,n
print(' ')
print('Entrez un par un les 4 chiffres de l`écriture en base 2 du nombre à convertir')
a,b,c,d = input().split()
print((a*2^3)+(b*2^2)+(c*2^1)+(d*2^0))

x=input()
