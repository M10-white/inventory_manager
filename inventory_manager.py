import json

# Fichier d'inventaire (JSON)
INVENTORY_FILE = "./data/inventory.json"

# Charger les utilisateurs depuis un fichier JSON
def load_users():
    try:
        with open("data/users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erreur : Fichier 'users.json' introuvable. Veuillez créer le fichier avec les utilisateurs.")
        return {}

# Charger l'inventaire depuis le fichier JSON
def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Retourne un inventaire vide si le fichier n'existe pas
    except json.JSONDecodeError:
        print("Erreur : Le fichier est corrompu. Un nouvel inventaire sera créé.")
        return {}

# Sauvegarder l'inventaire dans le fichier JSON
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)

# Fonction de connexion
def user_login(users):
    print("\n--- Connexion ---")
    username = input("Nom d'utilisateur : ").lower()
    password = input("Mot de passe : ")

    user_data = users.get(username, None)
    if user_data and user_data['password'] == password:
        print(f"Bienvenue {username} !")
        return user_data['role']  # Retourne le rôle de l'utilisateur (admin/employe)
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")
        return None

# Afficher l'inventaire
def display_inventory(inventory):
    print("\n--- Inventaire ---")
    if not inventory:
        print("Aucun produit dans l'inventaire.")
    else:
        for product, info in inventory.items():
            print(f"Produit : {product}, Quantité : {info['quantity']}, Prix : {info['price']}")

# Ajouter un produit à l'inventaire
def add_product(inventory):
    product_name = input("Nom du produit : ").capitalize()
    if product_name in inventory:
        print("Le produit existe déjà. Utilisez l'option de mise à jour.")
        return

    try:
        quantity = int(input("Quantité initiale : "))
        price = float(input("Prix unitaire : "))
        inventory[product_name] = {"quantity": quantity, "price": price}
        print(f"Produit {product_name} ajouté avec succès.")
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")

# Supprimer un produit de l'inventaire
def remove_product(inventory):
    product_name = input("Nom du produit à supprimer : ").capitalize()
    if product_name in inventory:
        del inventory[product_name]
        print(f"Produit {product_name} supprimé.")
    else:
        print(f"Erreur : Le produit {product_name} n'existe pas dans l'inventaire.")

# Vérifier le niveau des stocks et générer des alertes
def check_stock_levels(inventory):
    print("\n--- Vérification des niveaux de stock ---")
    low_stock_threshold = 5  # Seuil critique pour stock faible
    for product, info in inventory.items():
        if info['quantity'] <= low_stock_threshold:
            print(f"⚠️  Alerte : Stock faible pour {product} ({info['quantity']} unités restantes)")

# Mettre à jour la quantité d'un produit
def update_quantity(inventory):
    product_name = input("Nom du produit à mettre à jour : ").capitalize()
    if product_name in inventory:
        try:
            new_quantity = int(input("Nouvelle quantité : "))
            inventory[product_name]['quantity'] = new_quantity
            print(f"Quantité de {product_name} mise à jour.")
        except ValueError:
            print("Erreur : Veuillez entrer une quantité valide.")
    else:
        print(f"Erreur : Le produit {product_name} n'existe pas dans l'inventaire.")

# Générer un rapport sur les stocks faibles ou en rupture
def generate_stock_report(inventory):
    report = []
    for product, info in inventory.items():
        if info['quantity'] <= 5:  # Seuil de stock faible
            report.append(f"Produit : {product}, Stock actuel : {info['quantity']}, Prix : {info['price']}")
    
    print("\n--- Rapport de Stock ---")
    if report:
        for line in report:
            print(line)
    else:
        print("Tous les produits ont un niveau de stock suffisant.")
    
    with open("stock_report.txt", "w") as report_file:
        report_file.write("\n".join(report))
        print("Rapport de stock enregistré dans 'stock_report.txt'.")

# Interface Employé
def employee_menu(inventory):
    while True:
        print("\n--- Interface Employé ---")
        print("1. Afficher l'inventaire")
        print("2. Mettre à jour la quantité d'un produit")
        print("3. Générer un rapport de stock")
        print("4. Déconnexion")
        print("5. Quitter")
        
        choice = input("Choisissez une option : ")
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            update_quantity(inventory)
            save_inventory(inventory)
            check_stock_levels(inventory)
        elif choice == '3':
            generate_stock_report(inventory)
        elif choice == '4':
            print("Déconnexion...")
            return  # Retourne au menu principal
        elif choice == '5':
            save_inventory(inventory)
            print("Inventaire sauvegardé. Au revoir !")
            exit()
        else:
            print("Option invalide, veuillez réessayer.")

# Interface Administrateur
def admin_menu(inventory):
    while True:
        print("\n--- Interface Administrateur ---")
        print("1. Afficher l'inventaire")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Mettre à jour la quantité d'un produit")
        print("5. Générer un rapport de stock")
        print("6. Déconnexion")
        print("7. Quitter")
        
        choice = input("Choisissez une option : ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_product(inventory)
            save_inventory(inventory)
            check_stock_levels(inventory)
        elif choice == '3':
            remove_product(inventory)
            save_inventory(inventory)
            check_stock_levels(inventory)
        elif choice == '4':
            update_quantity(inventory)
            save_inventory(inventory)
            check_stock_levels(inventory)
        elif choice == '5':
            generate_stock_report(inventory)
        elif choice == '6':
            print("Déconnexion...")
            return  # Retourne au menu principal
        elif choice == '7':
            save_inventory(inventory)
            print("Inventaire sauvegardé. Au revoir !")
            exit()
        else:
            print("Option invalide, veuillez réessayer.")

# Menu Principal
def main_menu():
    users = load_users()
    inventory = load_inventory()

    while True:
        user_role = user_login(users)
        if not user_role:
            continue  # Si l'authentification échoue, recommencez

        # Menu en fonction du rôle
        if user_role == 'admin':
            admin_menu(inventory)
        elif user_role == 'employe':
            employee_menu(inventory)
        else:
            print("Erreur : rôle non défini.")

if __name__ == "__main__":
    main_menu()
