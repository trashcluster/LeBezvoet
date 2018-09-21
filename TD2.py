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
x = input()
