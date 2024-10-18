#!/bin/bash

# Vérifier si un lien a été fourni en argument
if [ -z "$1" ]; then
    echo "Usage: $0 <lien_bitly>"
    exit 1
fi

# Stocker le lien dans une variable
lien_bitly=$1

# Utiliser curl pour retrouver l'URL réelle
url_reelle=$(curl -Ls -o /dev/null -w %{url_effective} "$lien_bitly")

# Afficher l'URL réelle
echo "URL réelle : $url_reelle"

