# Système de Reconnaissance Faciale en Temps Réel

Ce projet est une application de reconnaissance faciale en temps réel performante développée en Python. Elle utilise **OpenCV** pour la capture vidéo et **DeepFace** pour l'analyse biotmétrique.

L'application compare instantanément le visage capturé par votre webcam avec une image de référence pour authentifier une identité.

---

## Description

Le programme analyse le flux vidéo de la webcam. À intervalles optimisés (via multithreading), il compare le visage détecté à une image de référence stockée dans le dossier `assets/`.

* **Succès** : Le message **"Similaire !"** s’affiche en vert si le visage correspond.
* **Échec** : Le message **"Non Similaire !"** s’affiche en rouge si aucune correspondance n'est trouvée.



---

## Fonctionnalités

*  **Capture Vidéo fluide** : Intégration directe avec la webcam via OpenCV.
*  **Intelligence Artificielle** : Utilisation de DeepFace pour une reconnaissance précise.
*  **Optimisation Multithreading** : La vérification faciale s'exécute en arrière-plan pour ne pas ralentir le flux vidéo.
*  **Interface Visuelle** : Feedback immédiat sur l'écran avec texte coloré.

---

## Structure du Projet

```text
OpenCvTest/
├── assets/
│   └── img1.png          # Image de référence pour la comparaison
├── reconnaissance_faciale.py # Script principal de l'application
├── requirements.txt      # Dépendances du projet
└── README.md             # Documentation
```

---

## Installation

### Prérequis
*   Python 3.8+
*   Une webcam fonctionnelle
*   `pip` (gestionnaire de paquets Python)

### Étapes

1.  **Cloner le projet**
    ```bash
    git clone https://github.com/abdeilah4/reconnaissance_faciale.git
    cd reconnaissance_faciale
    ```


2. **Installer les dépendances**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurer l'image de référence**
    *   Placez une photo claire de votre visage dans le dossier `assets/`.
    *   Nommez-la impérativement `img1.png` (ou modifiez le script à la ligne 11).

---

## Utilisation

Lancez simplement le script :

```bash
python reconnaissance_faciale.py
```

*   **Quitter** : Appuyez sur la touche `q` pour fermer l'application.

---


##  Auteur

**Abdelilah TAHIRI**
