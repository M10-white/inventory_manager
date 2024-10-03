import json
import tkinter as tk
from tkinter import messagebox
from gui.admin_interface import admin_window  # Import de l'interface admin
from gui.employee_interface import employee_window  # Import de l'interface employé

# Charger les utilisateurs depuis un fichier JSON
def load_users():
    try:
        with open("data/users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erreur : Fichier 'users.json' introuvable. Veuillez créer le fichier avec les utilisateurs.")
        return {}
    except json.JSONDecodeError:
        print("Erreur : Format du fichier 'users.json' incorrect.")
        return {}

# Fonction de connexion
def user_login(users, username, password):
    # Convertir le nom d'utilisateur en minuscule pour éviter la casse
    user_data = users.get(username.lower(), None)
    if user_data and user_data['password'] == password:
        return user_data['role']  # Retourne le rôle de l'utilisateur (admin/employe)
    else:
        return None

# Interface de connexion Tkinter
def login_window():
    # Charger les utilisateurs depuis le fichier JSON
    users = load_users()

    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Système de Gestion d'Inventaire - Connexion")

    # Labels et Entrées pour Nom d'utilisateur et Mot de passe
    tk.Label(root, text="Nom d'utilisateur :").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Mot de passe :").pack(pady=5)
    entry_password = tk.Entry(root, show="*")  # Masquer le mot de passe
    entry_password.pack()

    # Fonction pour gérer le bouton de connexion
    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        role = user_login(users, username, password)
        
        if role == 'admin':
            messagebox.showinfo("Succès", f"Bienvenue, Administrateur {username} !")
            root.destroy()  # Fermer la fenêtre de connexion
            admin_window()  # Lancer l'interface admin
        elif role == 'employe':
            messagebox.showinfo("Succès", f"Bienvenue, Employé {username} !")
            root.destroy()  # Fermer la fenêtre de connexion
            employee_window()  # Lancer l'interface employé
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    # Bouton de connexion
    tk.Button(root, text="Se Connecter", command=handle_login).pack(pady=20)

    # Lancer la fenêtre de connexion
    root.mainloop()

# Point d'entrée principal
if __name__ == "__main__":
    login_window()
