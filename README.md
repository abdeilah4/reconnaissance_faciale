Système de Reconnaissance Faciale en Temps Réel

Ce projet est une application de reconnaissance faciale en temps réel développée en Python avec OpenCV et DeepFace.
Il permet de comparer un visage capturé par la webcam à une image de référence afin de vérifier l’identité d’une personne.

Description

Le programme utilise la webcam pour afficher la vidéo en direct.
À intervalles réguliers, le visage détecté est comparé à l’image de référence stockée dans le dossier assets.

Si les visages correspondent : le message "Similaire !" s’affiche en vert.

Sinon : le message "Non Similaire !" s’affiche en rouge.

Ce projet a été réalisé à des fins pédagogiques pour l’apprentissage de la vision par ordinateur avec Python.

Fonctionnalités

Capture vidéo en temps réel via la webcam

Reconnaissance faciale avec DeepFace

Optimisation des performances en évitant les comparaisons à chaque image

Affichage clair du résultat de la reconnaissance

Multithreading pour améliorer la fluidité

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

Étapes

1-Cloner le projet

git clone https://github.com/abdeilah4/reconnaissance_faciale.git
cd reconnaissance_faciale


2-Créer un environnement virtuel (optionnel mais recommandé)

python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux / Mac


3-Installer les dépendances

pip install -r requirements.txt


4-modifier l’image de référence

Placer une image de visage dans le dossier assets

Nom par défaut : img1.png

Utilisation

Lancer le programme avec :

python reconnaissance_faciale.py


La vidéo de la webcam s’affiche avec le résultat de la reconnaissance

Appuyer sur la touche q pour quitter le programme