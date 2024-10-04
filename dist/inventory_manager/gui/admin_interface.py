import tkinter as tk
from tkinter import messagebox
import json

# Chemin vers le fichier d'inventaire
INVENTORY_FILE = "./data/inventory.json"

# Charger l'inventaire depuis le fichier JSON
def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Retourne un inventaire vide si le fichier n'existe pas
    except json.JSONDecodeError:
        print("Erreur : Le fichier d'inventaire est corrompu.")
        return {}

# Sauvegarder l'inventaire dans le fichier JSON
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)

# Ajouter un nouveau produit à l'inventaire
def add_product():
    product_name = entry_product_name.get().capitalize()
    try:
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())
    except ValueError:
        messagebox.showerror("Erreur", "Quantité et Prix doivent être des valeurs numériques.")
        return

    if product_name in inventory:
        messagebox.showwarning("Attention", "Le produit existe déjà.")
    else:
        inventory[product_name] = {"quantity": quantity, "price": price}
        save_inventory(inventory)
        messagebox.showinfo("Succès", f"Produit {product_name} ajouté avec succès.")
        refresh_inventory_list()

# Supprimer un produit de l'inventaire
def remove_product():
    selected_item = inventory_listbox.get(tk.ACTIVE)
    if selected_item:
        product_name = selected_item.split(" : ")[0]
        if product_name in inventory:
            del inventory[product_name]
            save_inventory(inventory)
            messagebox.showinfo("Succès", f"Produit {product_name} supprimé.")
            refresh_inventory_list()
        else:
            messagebox.showerror("Erreur", "Produit non trouvé.")
    else:
        messagebox.showwarning("Attention", "Aucun produit sélectionné.")

# Mettre à jour la quantité d'un produit
def update_quantity():
    selected_item = inventory_listbox.get(tk.ACTIVE)
    if selected_item:
        product_name = selected_item.split(" : ")[0]
        if product_name in inventory:
            try:
                new_quantity = int(entry_update_quantity.get())
                inventory[product_name]['quantity'] = new_quantity
                save_inventory(inventory)
                messagebox.showinfo("Succès", f"Quantité de {product_name} mise à jour.")
                refresh_inventory_list()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer une quantité valide.")
        else:
            messagebox.showerror("Erreur", "Produit non trouvé.")
    else:
        messagebox.showwarning("Attention", "Aucun produit sélectionné.")

# Afficher l'inventaire dans la liste
def refresh_inventory_list():
    inventory_listbox.delete(0, tk.END)  # Vider la liste avant d'ajouter les éléments
    for product, info in inventory.items():
        inventory_listbox.insert(tk.END, f"{product} : {info['quantity']} unités, {info['price']} €")

# Générer un rapport de stock faible
def generate_stock_report():
    low_stock_threshold = 5
    report = []
    for product, info in inventory.items():
        if info['quantity'] <= low_stock_threshold:
            report.append(f"Produit : {product}, Stock actuel : {info['quantity']}, Prix : {info['price']}")

    if report:
        with open("./reports/stock_report.txt", "w") as report_file:
            report_file.write("\n".join(report))
        messagebox.showinfo("Rapport", "Rapport de stock généré dans 'stock_report.txt'.")
    else:
        messagebox.showinfo("Rapport", "Tous les produits ont un niveau de stock suffisant.")

def display_stock_report():
    try:
        with open("./reports/stock_report.txt", "r") as report_file:
            report_content = report_file.read()
        
        # Créer une nouvelle fenêtre pour afficher le rapport
        report_window = tk.Toplevel()
        report_window.title("Rapport de Stock")
        
        # Afficher le contenu du rapport dans une zone de texte
        report_text = tk.Text(report_window, wrap=tk.WORD)
        report_text.insert(tk.END, report_content)
        report_text.pack(expand=True, fill=tk.BOTH)
        
        # Ajouter un bouton pour fermer la fenêtre
        tk.Button(report_window, text="Fermer", command=report_window.destroy).pack(pady=5)
    
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier 'stock_report.txt' n'existe pas.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Interface principale pour l'administrateur
def admin_window():
    global inventory
    inventory = load_inventory()

    # Fenêtre principale
    global window  # Déclare la fenêtre comme globale pour qu'elle soit accessible
    window = tk.Tk()
    window.title("Interface Administrateur - Gestion d'Inventaire")
    window.geometry("800x600")  

    # Frame pour l'inventaire
    frame_inventory = tk.Frame(window)
    frame_inventory.pack(pady=10)

    # Liste d'inventaire
    global inventory_listbox
    inventory_listbox = tk.Listbox(frame_inventory, width=50, height=15)
    inventory_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame_inventory)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    inventory_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=inventory_listbox.yview)

    # Rafraîchir l'affichage de l'inventaire
    refresh_inventory_list()

    # --- Zone d'ajout de produits ---
    tk.Label(window, text="Nom du produit :").pack()
    global entry_product_name
    entry_product_name = tk.Entry(window)
    entry_product_name.pack()

    tk.Label(window, text="Quantité initiale :").pack()
    global entry_quantity
    entry_quantity = tk.Entry(window)
    entry_quantity.pack()

    tk.Label(window, text="Prix unitaire (€) :").pack()
    global entry_price
    entry_price = tk.Entry(window)
    entry_price.pack()

    tk.Button(window, text="Ajouter Produit", command=add_product).pack(pady=5)

    # --- Zone de mise à jour de quantité ---
    tk.Label(window, text="Nouvelle Quantité :").pack()
    global entry_update_quantity
    entry_update_quantity = tk.Entry(window)
    entry_update_quantity.pack()

    tk.Button(window, text="Mettre à Jour Quantité", command=update_quantity).pack(pady=5)

    # --- Suppression d'un produit ---
    tk.Button(window, text="Supprimer Produit", command=remove_product).pack(pady=5)

    # --- Générer un rapport de stock ---
    tk.Button(window, text="Générer Rapport Stock Faible", command=generate_stock_report).pack(pady=5)

    tk.Button(window, text="Afficher Rapport de Stock", command=display_stock_report).pack(pady=5)
    
    # --- Quitter ---
    tk.Button(window, text="Quitter", command=window.destroy).pack(pady=20)

    # Lancer la fenêtre
    window.mainloop()

# Si ce fichier est exécuté directement, on lance l'interface admin
if __name__ == "__main__":
    admin_window()
