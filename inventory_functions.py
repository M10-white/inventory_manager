import json

# Définition du fichier d'inventaire
INVENTORY_FILE = "./data/inventory.json"

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

# Afficher l'inventaire
def display_inventory(inventory):
    if not inventory:
        print("Aucun produit dans l'inventaire.")
    else:
        for product, info in inventory.items():
            print(f"Produit : {product}, Quantité : {info['quantity']}, Prix : {info['price']}")

# Ajouter un produit à l'inventaire
def add_product(inventory, product_name, quantity, price):
    if product_name in inventory:
        print("Le produit existe déjà. Utilisez l'option de mise à jour.")
    else:
        inventory[product_name] = {"quantity": quantity, "price": price}
        print(f"Produit {product_name} ajouté avec succès.")

# Supprimer un produit de l'inventaire
def remove_product(inventory, product_name):
    if product_name in inventory:
        del inventory[product_name]
        print(f"Produit {product_name} supprimé.")
    else:
        print(f"Erreur : Le produit {product_name} n'existe pas dans l'inventaire.")

# Mettre à jour la quantité d'un produit
def update_quantity(inventory, product_name, new_quantity):
    if product_name in inventory:
        inventory[product_name]['quantity'] = new_quantity
        print(f"Quantité de {product_name} mise à jour à {new_quantity}.")
    else:
        print(f"Erreur : Le produit {product_name} n'existe pas dans l'inventaire.")

# Vérifier les niveaux de stock et générer des alertes
def check_stock_levels(inventory):
    low_stock_threshold = 5  # Seuil critique pour stock faible
    low_stock_items = []
    for product, info in inventory.items():
        if info['quantity'] <= low_stock_threshold:
            low_stock_items.append((product, info['quantity']))
    return low_stock_items

# Générer un rapport sur les stocks faibles ou en rupture
def generate_stock_report(inventory):
    report = []
    for product, info in inventory.items():
        if info['quantity'] <= 5:  # Seuil de stock faible
            report.append(f"Produit : {product}, Stock actuel : {info['quantity']}, Prix : {info['price']}")
    
    # Sauvegarder le rapport dans un fichier texte
    with open("stock_report.txt", "w") as report_file:
        if report:
            report_file.write("\n".join(report))
        else:
            report_file.write("Tous les produits ont un niveau de stock suffisant.")
    print("Rapport de stock enregistré dans 'stock_report.txt'.")
