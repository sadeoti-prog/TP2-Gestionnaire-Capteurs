
from capteur import Capteur
import json

# Limites choisies selon le type de capteur
LIMITES = {
    "temperature_bureau": (0, 50),
    "humidite_serre": (0, 100),
    "pression_capteur_ext": (900, 1100),
    "luminosite_atelier": (0, 10000)
}


def trier_capteurs(capteurs):
    """Tri à bulles décroissant selon le nombre d'anomalies.

    Complexité temporelle : O(n²) dans le pire cas.
    Complexité mémoire supplémentaire : O(n) pour la liste.
    Le tri Python sorted() utilise O(n log n) dans le pire cas.
    """

    classement = list(capteurs.values())
    n = len(classement)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            if classement[j].nb_anomalies < classement[j + 1].nb_anomalies:
                classement[j], classement[j + 1] = classement[j + 1], classement[j]

    return classement


# Lire les données du JSON
with open("mesures_capteurs_reseau.json", "r", encoding="utf-8") as fichier:
    donnees = json.load(fichier)

# Dictionnaire : nom du capteur -> objet Capteur
# Ce choix permet de retrouver facilement un objet par son nom.
capteurs = {}

for noms_capteurs, mesures_capteurs in donnees.items():

    capteur = Capteur(noms_capteurs, mesures_capteurs)

    # Récupérer les limites du capteur
    minimum, maximum = LIMITES[noms_capteurs]

    # Nettoyer ses mesures
    capteur.nettoyer(minimum, maximum)

    # Conserver l'objet dans le dictionnaire
    capteurs[noms_capteurs] = capteur


# Trier les capteurs
classement = trier_capteurs(capteurs)

print("CLASSEMENT DES CAPTEURS PAR NOMBRE D'ANOMALIES")

for capteur in classement:
    moyenne = capteur.moyenne()

    if moyenne is None:
        moyenne_texte = "N/A"
    else:
        moyenne_texte = f"{moyenne:.2f}"

    print(f"\nCapteur : {capteur.nom}")
    print(f"Anomalies : {capteur.nb_anomalies}")
    print(f"Valeurs valides : {capteur.nombre_valides()}")
    print(f"Moyenne : {moyenne_texte}")
    print(f"Minimum : {capteur.minimum()}")
    print(f"Maximum : {capteur.maximum()}")
