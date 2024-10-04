# Système de Gestion d'Inventaire

## Description
Ce projet est un système de gestion d'inventaire développé en Python avec une interface graphique utilisant Tkinter. L'application permet aux utilisateurs de gérer des produits, de suivre les stocks, et de générer des rapports sur les niveaux de stock.

## Fonctionnalités
- **Gestion des Produits** : Ajouter, supprimer et mettre à jour les produits de l'inventaire.
- **Rapports de Stock** : Générer des rapports sur les produits avec un stock faible.
- **Interface Utilisateur** : Interface graphique conviviale pour interagir avec le système.
- **Authentification** : Système de connexion pour les administrateurs et les employés.

## Arborescence des Fichiers
Voici l'arborescence des fichiers du projet :

```bash
gestion_inventaire/
├── gui/
│   ├── admin_interface.py     # Interface pour les administrateurs
│   ├── employee_interface.py   # Interface pour les employés
│   └── login_interface.py      # Interface de connexion
├── data/
│   ├── users.json             # Fichier JSON contenant les utilisateurs
│   └── inventory.json         # Fichier JSON contenant l'inventaire
├── reports/
│   └── stock_report.txt       # Rapport des produits avec un stock faible
└── inventory_manager.py        # Fichier principal pour gérer l'inventaire
```

## Utilisation

Lancez l'application :

```bash
py inventory_manager.py
```

Connectez-vous avec vos identifiants d'administrateur ou d'employé.
Gérez votre inventaire à partir de l'interface.

## Roadmap

```mmdc
    title Roadmap du Projet de Gestion d'Inventaire (30/09/2024 - 04/10/2024)
    dateFormat  YYYY-MM-DD
    section Planning & Design
    Conception du projet              :a1, 2024-09-30, 1d
    Définition des besoins            :a2, 2024-09-30, 1d

    section Développement
    Implémentation de la structure de base :a3, 2024-10-01, 1d
    Création de l'interface de connexion   :a4, 2024-10-01, 0.5d
    Gestion des utilisateurs               :a5, 2024-10-01, 0.5d
    Développement des interfaces (Admin/Employé) :a6, 2024-10-02, 1d

    section Finalisation & Tests
    Ajout des fonctionnalités supplémentaires (stock faible) :a7, 2024-10-03, 1d
    Correction des bugs et tests               :a8, 2024-10-04, 1d
    Présentation finale                        :a9, 2024-10-04, 0.5d
```

## Auteurs
Chaouki Brahim - M10_white
