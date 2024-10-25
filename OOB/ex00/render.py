#!/usr/bin/python3

import os
import re
import sys
import settings

def check_variables():
    REQUIRED_VARIABLES = ["last_name", "first_name", "age", "profession"]
    # Vérifie que chaque variable requise est définie dans settings
    for var in REQUIRED_VARIABLES:
        if not hasattr(settings, var):
            print(f"Erreur : La variable '{var}' est manquante dans settings.py")
            sys.exit(1)



def extract_info(file_template):
    # Vérifie l'extension et l'existence du fichier
    if not file_template.endswith('.template') or not os.path.exists(file_template):
        sys.exit(f"Erreur : le fichier doit avoir l'extension .template et exister")
    with open(file_template) as file:
        template = file.read()
    check_variables()
    # Remplace toutes les variables encadrées de {{...}} par leurs valeurs dans `settings`
    template = re.sub(r"\{\{(\w+)\}\}", lambda m: str(vars(settings).get(m.group(1), m.group(0))), template)
    # Création et écriture dans le fichier de sortie
    output_file = file_template.replace('.template', '.html')
    with open(output_file, 'w') as file:
        file.write(template)
    print(f"Le fichier {output_file} a été créé avec succès.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_template>")
        sys.exit(1)
    extract_info(sys.argv[1])

if __name__ == '__main__':
    main()
