# LITReview
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
## Présentation
LITReview est une application permettant de demander et de consulter des critiques de livres.

Il est possible de :
- créer un ticket de demande de critique d'un livre,
- publier une critique en réponse à un ticket ou à partir d'un nouveau ticket,
- modifier et supprimer ses tickets et critiques,
- suivre d'autres utilisateurs,
- consulter les tickets et critiques d'autres utilisateurs.

Le flux de la page principale affiche les demandes et critiques par ordre de parution la plus récente :
- de vos propres tickets et critiques,
- des tickets et critiques des utilisateurs que vous suivez,
- des réponses à vos tickets de tous les utilisateurs.

La base de données `db.sqlite3` contient déjà des utilisateurs afin de pouvoir tester rapidement l'application.

Les utilisateurs présents vont de **user1** à **user4**. Le mot de passe est identique à l'identifiant.

Il est également possible de créer d'autres utilisateurs depuis la page de connexion.
## Installation
1. Cloner le répertoire depuis Github, puis se placer dans le répertoire principal.
```shell
git clone https://github.com/rducrot/litreview
cd litreview
```
2. Mettre en place l'environnement virtuel.
```shell
python3 -m venv venv
source venv/bin/activate
```
3. Installer les dépendances depuis l'environnement virtuel.
```shell
pip3 install -r requirements.txt
```
## Exécution
Lancer la commande depuis le répertoire de l'application :
```shell
python3 manage.py runserver
```
Le site est accessible par défaut à l'adresse http://127.0.0.1:8000.
## Qualité du code
Un rapport flake8 est présent au format HTML dans le dossier `flake8_rapport` afin de vérifier que le code respecte bien la PEP8. Il est possible de générer un nouveau rapport avec la commande :
```bash
flake8 --format=html --htmldir=flake8_rapport
```