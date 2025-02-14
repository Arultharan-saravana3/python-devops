.PHONY: init run test build clean

# Installation des dépendances
init:
	@echo "Installation des dépendances..."
	pip install -r requirements.txt

# Lancement de l'appli en local
run:
	@echo "Lancement de l'application Flask..."
	python app.py

# Lancement des test unitaires
test:
	@echo "Lancement des tests..."
	python -m unittest test.py

# Création de l'image Docker healthcalculator 
build:
	@echo "Création de l'image Docker..."
	docker build -t healthcalculator .
