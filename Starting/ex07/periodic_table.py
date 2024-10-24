#!/bin/env python3
import sys

# Fonction pour lire le fichier des éléments
def read_file(filename):
    elements = []
    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                continue
            nom, attribue = line.split('=')
            info = {key.strip(): value.strip() for key, value in (attribute.split(':') for attribute in attribue.split(', '))}
            info['nom'] = nom.strip()
            elements.append(info)
    return elements

# Fonction pour générer le fichier HTML du tableau périodique
def generate_html(dict_periodic):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Tableau Périodique</title>
    </head>
    <body>
        <header><h1>Tableau Périodique</h1></header>
        <main>
            <section>
                <table>
    '''

    # Initialisation des 7 périodes
    lignes = [[] for _ in range(7)]

    # Remplir les lignes du tableau périodique avec les éléments
    for element in dict_periodic:
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

        # Initialiser les cases vides (positions vides) pour chaque période
        while len(lignes[periode]) < 18:
            lignes[periode].append(None)

        # Ajouter l'élément à sa position correcte
        lignes[periode][position] = element

    # Génération des lignes HTML avec gestion des cases vides
    for i, ligne in enumerate(lignes):
        # Appliquer la classe CSS pour chaque période
        html += f"<tr>\n"
        for cellule in ligne:
            if cellule:
                html += f"""
                <td class='periode-{i+1}'>
                    <h4>{cellule['nom']}</h4>
                    <ul>
                        <li>No {cellule['number']}</li>
                        <li>{cellule['small']}</li>
                        <li>{cellule['molar']}</li>
                        <li>{cellule['electron']} électron(s)</li>
                    </ul>
                </td>
                """
            else:
                html += "<td></td>\n"  # Case vide là où il n'y a pas d'élément
        html += "</tr>\n"

    # Fin du fichier HTML
    html += """
                </table>
            </section>
        </main>
    </body>
    </html>
    """
    
    return html

# Fonction pour écrire le fichier HTML généré
def ecrire_html(fichier_sortie, contenu_html):
    with open(fichier_sortie, 'w') as f:
        f.write(contenu_html)

# Point d'entrée du programme
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python periodic_table.py <filename>')
        sys.exit(1)
    
    # Lecture des données du fichier
    tab_periodique = read_file(sys.argv[1])
    
    # Génération du contenu HTML
    html = generate_html(tab_periodique)
    
    # Écriture du fichier HTML
    ecrire_html('periodic_table.html', html)
