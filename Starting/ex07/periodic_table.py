def lire_elements(fichier):
    elements = []
    with open(fichier, 'r') as f:
        for ligne in f:
            nom, details = ligne.split(' = ')
            info = {}
            for detail in details.split(','):
                cle, valeur = detail.split(':')
                info[cle.strip()] = valeur.strip()
            info['nom'] = nom.strip()
            elements.append(info)
    return elements

def generer_html(elements):
	# Début du fichier HTML
	html = """
	<!DOCTYPE html>
	<html lang="fr">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Tableau périodique</title>
		<style>
			table { border-collapse: collapse; }
			td { border: 1px solid black; padding: 10px; text-align: center; vertical-align: top; }
			h4 { margin: 0; }
		</style>
	</head>
	<body>
		<h1>Tableau périodique des éléments</h1>
		<table>
	"""

	# Créer une liste pour 7 périodes (lignes), chaque ligne avec 18 colonnes (positions)
	lignes = [[] for _ in range(7)]

	# Remplir les lignes avec des éléments (selon la position)
	for element in elements:
		position = int(element['position'])
		number = int(element['number'])

		# Déterminer la période à partir du numéro atomique
		if number <= 2:
			periode = 0  # 1ère ligne
		elif number <= 10:
			periode = 1  # 2e ligne
		elif number <= 18:
			periode = 2  # 3e ligne
		elif number <= 36:
			periode = 3  # 4e ligne
		elif number <= 54:
			periode = 4  # 5e ligne
		elif number <= 86:
			periode = 5  # 6e ligne
		else:
			periode = 6  # 7e ligne

		# Ajouter l'élément à la période correspondante (lignes[periode])
		while len(lignes[periode]) < 18:
			lignes[periode].append(None)  # Initialiser les positions avec des None
			
		lignes[periode][position] = element

	# Génération des lignes HTML avec gestion des "cases vides"
	for ligne in lignes:
		html += "<tr>\n"
		for cellule in ligne:
			if cellule:
				html += f"""
				<td>
					<h4>{cellule['nom']}</h4>
					<ul>
						<li>No {cellule['number']}</li>
						<li>{cellule['small']}</li>
						<li>{cellule['molar']}</li>
						<li>Électrons: {cellule['electron']}</li>
					</ul>
				</td>
				"""
			else:
				html += "<td></td>\n"  # Case vide là où il n'y a pas d'élément
		html += "</tr>\n"

	# Fin du fichier HTML
	html += """
		</table>
	</body>
	</html>
	"""

	return html

def ecrire_html(fichier_sortie, contenu_html):
    with open(fichier_sortie, 'w') as f:
        f.write(contenu_html)

def main():
    # Lire les éléments depuis le fichier
    elements = lire_elements('periodic_table.txt')
    
    # Générer le HTML
    contenu_html = generer_html(elements)
    
    # Écrire le fichier HTML final
    ecrire_html('periodic_table.html', contenu_html)

if __name__ == "__main__":
    main()
