import pandas as pd
import tkinter as tk
from tkinter import ttk

# Remplacez "VotreNomUtilisateur" par votre nom d'utilisateur
file_path = "D:\Desktop\Maintenance\TD_Pareto_Tableau_données_CONTIENTOU.xlsx"

# Chargement des données
df = pd.read_excel(file_path, engine="openpyxl")

# Calcul des agrégats par sous-ensemble
summary = df.groupby("Sous-ensemble").agg(
    N=("Durée d'arrêt (mn)", 'count'),  # Nombre de défaillances
    Nt=("Durée d'arrêt (mn)", 'sum'),  # Temps total d'arrêt
    t=("Durée d'arrêt (mn)", 'mean')  # Moyenne des temps d'arrêt
).reset_index()

# Fonction pour afficher les données dans une fenêtre
def display_table(dataframe):
    root = tk.Tk()
    root.title("Tableau des défaillances")

    # Création d'une table avec Treeview
    tree = ttk.Treeview(root, columns=list(dataframe.columns), show="headings")
    
    # Configuration des colonnes
    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    
    # Remplir la table avec les données
    for _, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))
    
    # Ajout du Treeview dans la fenêtre
    tree.pack(expand=True, fill="both")
    
    # Lancer la boucle Tkinter
    root.mainloop()

# Affichage du tableau
display_table(summary)

