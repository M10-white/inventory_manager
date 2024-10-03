import tkinter as tk
from tkinter import messagebox
import json

INVENTORY_FILE = "./data/inventory.json"

def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_quantity():
    product = entry_product.get().capitalize()
    new_quantity = entry_quantity.get()

    if product in inventory:
        try:
            inventory[product]['quantity'] = int(new_quantity)
            save_inventory()
            messagebox.showinfo("Succès", f"Quantité de {product} mise à jour.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur valide.")
    else:
        messagebox.showerror("Erreur", f"Produit {product} non trouvé.")

def save_inventory():
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)

def employee_window():
    global entry_product, entry_quantity, inventory
    inventory = load_inventory()

    window = tk.Tk()
    window.title("Interface Employé - Gestion d'Inventaire")
    window.geometry("800x600")
    
    tk.Label(window, text="Produit :").grid(row=0, column=0)
    entry_product = tk.Entry(window)
    entry_product.grid(row=0, column=1)

    tk.Label(window, text="Nouvelle Quantité :").grid(row=1, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=1, column=1)

    tk.Button(window, text="Mettre à jour", command=update_quantity).grid(row=2, column=0, columnspan=2)

    window.mainloop()