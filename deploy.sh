#!/bin/bash

# Variables
REPO_URL="https://github.com/votre-nom-utilisateur/votre-repo.git"
BRANCH="main"

# Initialiser le dépôt si ce n'est pas déjà fait
if [ ! -d ".git" ]; then
  git init
  git remote add origin $REPO_URL
fi

# Ajouter tous les fichiers, commiter et pousser
git add .
read -p "Entrez le message de commit: " commit_message
git commit -m "$commit_message"
git push -u origin $BRANCH
