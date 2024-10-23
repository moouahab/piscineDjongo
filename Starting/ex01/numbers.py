if __name__ == '__main__':
	with open("numbers.txt", "r") as f:
		contener = f.readline()  # Lit une seule ligne
		contener = contener.replace(',', '\n')  # Remplace '\n' par une virgule
		print(contener, end='')  # Affiche la ligne modifiée
