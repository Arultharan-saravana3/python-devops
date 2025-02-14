# Service de Calcul de Santé 🏥

Un microservice Python pour calculer les métriques de santé (IMC et BMR) avec une API REST. Le projet est conteneurisé avec Docker et configuré pour déploiement sur Azure via GitHub Actions.

## 🌟 Fonctionnalités
- Calculateur IMC: Calcul de l'Indice de Masse Corporelle
- Calculateur BMR: Calcul du métabolisme de base avec l'équation Harris-Benedict
- API REST: Points de terminaison documentés
- Interface Web: Interface utilisateur conviviale
- Support Docker: Application conteneurisée
- Pipeline CI/CD: Tests et déploiement automatisés

## 📂 Structure du Projet
Health_Calculator_Project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── static/
│   └── index.html
├── app.py
├── health_utils.py
├── test.py
├── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
Copy
## 📖 Documentation de l'API

### Points de Terminaison

#### POST /bmi
Calcule l'IMC
```json
{
    "height": 1.75,  // Taille en mètres
    "weight": 70     // Poids en kilogrammes
}
POST /bmr
Calcule le BMR
jsonCopy{
    "height": 175,    // Taille en centimètres
    "weight": 70,     // Poids en kilogrammes
    "age": 25,        // Âge en années
    "gender": "male"  // "male" ou "female"
}
🛠️ Développement Local
Prérequis

Python 3.12
Docker
Make (optionnel)

Installation

Cloner le dépôt

bashCopygit clone https://github.com/Arultharan-saravana3/python-devops.git
cd python-devops

Créer un environnement virtuel

bashCopypython -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

Installer les dépendances

bashCopypip install -r requirements.txt
Lancer l'Application
bashCopypython app.py
Exécuter les Tests
bashCopypytest test.py -v
🔄 Pipeline CI/CD
État Actuel du Déploiement ❌
✅ CI (Intégration Continue) : Fonctionnelle

Tests automatiques
Vérification du code
Build de l'application

❌ CD (Déploiement) : Non Fonctionnel
Important : Problème de Crédits Azure
Le pipeline est correctement configuré mais le déploiement est actuellement impossible en raison d'un compte Azure sans crédits.
Message d'erreur :
CopyÉchec de chargement des journaux de déploiement : La demande a expiré
Cause :

Compte Azure avec 0 crédits
Impossibilité d'utiliser les services Azure sans crédits actifs

Solutions temporaires :

Exécuter l'application localement
Utiliser une plateforme d'hébergement alternative gratuite
Attendre le renouvellement des crédits Azure

Note : Toute la configuration CI/CD est en place et fonctionnelle, seul le déploiement final est bloqué à cause du manque de crédits Azure.
Copy
Voulez-vous que je modifie ou ajoute d'autres sections ? CopyRetrySAfais le moi e redameEditmarkdownCopy# Service de Calcul de Santé 🏥

## Description
Un microservice Python pour calculer les métriques de santé (IMC et BMR) avec une API REST. Le projet est conteneurisé avec Docker et intègre un pipeline CI/CD GitHub Actions pour déploiement Azure.

## 🌟 Fonctionnalités
- Calcul IMC (Indice de Masse Corporelle)
- Calcul BMR (Métabolisme de Base)
- API REST documentée
- Interface web utilisateur
- Docker prêt
- Pipeline CI/CD 

## 🔧 Technologies
- Python 3.12
- Flask
- Docker
- GitHub Actions
- Azure Web Services

## 📂 Structure Projet
service/
├── .github/workflows/
│   └── ci.yml
├── app.py
├── test.py
├── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
Copy
## 🚀 Installation Locale

### Prérequis
- Python 3.12
- Docker
- pip

### Installation
```bash
git clone https://github.com/Arultharan-saravana3/python-devops.git
cd python-devops
pip install -r requirements.txt
Lancement
bashCopypython app.py
Tests
bashCopypytest test.py -v
🔄 État CI/CD
✅ Intégration Continue (CI)

Tests automatiques : OK
Vérification code : OK
Build : OK

❌ Déploiement Continu (CD)
Le déploiement est actuellement arrêté en raison d'un problème de crédits Azure.
Erreur :
CopyÉchec de chargement des journaux de déploiement : La demande a expiré
Crédits Azure : 0
Impact :

Pipeline CI/CD configuré et fonctionnel
Code prêt pour déploiement
Déploiement Azure impossible sans crédits

Solutions temporaires :

Exécution locale uniquement
Utilisation plateformes gratuites alternatives
En attente renouvellement crédits Azure

📫 Contact
GitHub : https://github.com/Arultharan-saravana3/python-devops
