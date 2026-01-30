"# reconnaissance_faciale" 
Système de Reconnaissance Faciale en Temps Réel

Ce projet est une application de reconnaissance faciale en temps réel développée en Python à l’aide des bibliothèques OpenCV et DeepFace.
Il permet de comparer un visage capturé par la webcam avec une image de référence afin de vérifier l’identité d’une personne.

Description

Le programme utilise la webcam pour afficher une vidéo en direct.
À intervalles réguliers, le visage détecté est comparé à une image de référence stockée dans le dossier assets.

Lorsque les deux visages correspondent, le message "Similaire !" s’affiche en vert.
Dans le cas contraire, le message "Non Similaire !" s’affiche en rouge.

Ce projet a été réalisé dans un but pédagogique, notamment pour l’apprentissage de la vision par ordinateur avec Python.

Fonctionnalités

Capture vidéo en temps réel via la webcam

Reconnaissance faciale à l’aide de DeepFace

Optimisation des performances en évitant les comparaisons à chaque image

Affichage clair du résultat de la reconnaissance

Utilisation du multithreading pour améliorer la fluidité

Technologies utilisées

Python 3

OpenCV

DeepFace

Threading

Installation
Prérequis

Python 3.7 ou supérieur

Une webcam fonctionnelle

pip installé

Étapes d’installation

Cloner le projet :

git clone https://github.com/abdeilah4/reconnaissance_faciale.git
cd reconnaissance_faciale


Créer un environnement virtuel (optionnel mais recommandé) :

python -m venv venv
venv\Scripts\activate


Installer les dépendances :

pip install -r requirements.txt


Ajouter l’image de référence :

Placer une image de visage dans le dossier assets

Nom par défaut : img1.png

Utilisation

Lancer le programme avec la commande :

python reconnaissance_faciale.py


La vidéo de la webcam s’affiche avec le résultat de la reconnaissance

Appuyer sur la touche q pour quitter le programme