#Vol vers

def vol_vers(destination, horaire) :
	print(' ')
	print('Le vol en direction de ' + destination + ' décollera à ' + horaire)
	print(' ')
	print('-----------------------------------------------------------')

vol_vers('Pekin', '9h00')
vol_vers('Paris', '16h54')
vol_vers('Istanbul', '7h39')

#Argus1

def argus1(prix) :
	remise1 = int(20)
	remise2 = int(13)
	remise3 = int(8)
	print('Prix initiale', prix)
	prix = prix-prix*remise1/100
	print("Prix au bout d'un an avec remise de ", remise1, "% : ", prix)
	prix = prix-prix*remise2/100
	print("Prix au bout de 2 ans avec remise de ", remise2, "% : ", prix)
	prix = prix-prix*remise3/100
	print("Prix au bout de 3 ans avec remise de ", remise3, "% : ", prix)
argus1(int(input("Entre le prix du vehicule")))


#Argus2

def argus1(prix, remise1, remise2, remise3) :
	print('Prix initiale', prix)
	prix = prix-prix*remise1/100
	print("Prix au bout d'un an avec remise de ", remise1, "% : ", prix)
	prix = prix-prix*remise2/100
	print("Prix au bout de 2 ans avec remise de ", remise2, "% : ", prix)
	prix = prix-prix*remise3/100
	print("Prix au bout de 3 ans avec remise de ", remise3, "% : ", prix)
argus1(input("Entre le prix du vehicule suivi des remises sur 3 ans (3 valeures)"))
