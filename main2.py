
class Capteur:
    def __init__(self, mesures_brutes):
        self.mesures_brutes = mesures_brutes
        self.mesures_nettoyees = {}

    def nettoyer(self, limites):
        """Conserve les mesures comprises dans les limites du capteur."""
        self.mesures_nettoyees = {}

        for key, mesures in self.mesures_brutes.items():
            if key not in limites:
                raise ValueError(f"Limites manquantes pour le capteur {key}")

            minimum, maximum = limites[key]
            self.mesures_nettoyees[key] = {}

            for cle, valeur in enumerate(mesures):
                if isinstance(valeur, bool):
                    continue

                try:
                    valeur = float(valeur)
                except (ValueError, TypeError):
                    continue

                if minimum <= valeur <= maximum:
                    self.mesures_nettoyees[key][cle] = valeur

    def nombre_valeurs_valides(self, key):

        return len(self.mesures_nettoyees[key])

    def moyenne(self, key):

        if not self.mesures_nettoyees[key]:
            return None
        return sum(self.mesures_nettoyees[key].values()) / len(self.mesures_nettoyees[key])

    def minimum(self, key):

        if not self.mesures_nettoyees[key]:
            return None
        return min(self.mesures_nettoyees[key].values())

    def maximum(self, key):

        if not self.mesures_nettoyees[key]:
            return None
        return max(self.mesures_nettoyees[key].values())

    def amplitude(self, key):

        if not self.mesures_nettoyees[key]:
            return None
        return self.maximum(key) - self.minimum(key)

    def nombre_anomalies(self, key):

        return len(self.mesures_brutes[key]) - self.nombre_valeurs_valides(key)



        

        
        
        
limites = {
    "temperature_bureau": (20, 30),
    "pression_capteur_ext": (900, 1100),
    "humidite_serre": (0, 100),
    "luminosite_atelier": (0, 1000)
}
     






mesures_brutes={
  "temperature_bureau": [
    22.5,
    22.3,
    "23.1",
    22.8,
    None,
    23.2,
    999,
    22.4,
    22.6,
    "N/A",
    23.0,
    22.9,
    22.7,
    None,
    22.5,
    -150,
    23.3,
    22.8,
    22.6,
    23.1,
    22.9,
    "22.4",
    22.5,
    23.0,
    22.8
  ],
  "humidite_serre": [
    65.2,
    64.8,
    65.5,
    None,
    66.1,
    "65.3",
    65.9,
    64.7,
    None,
    65.4,
    999.9,
    66.0,
    64.5,
    65.2,
    "missing",
    65.8,
    64.9,
    65.1,
    66.2,
    65.0,
    "65.6",
    64.6,
    65.3,
    -50,
    65.7
  ],
  "pression_capteur_ext": [
    1013.25,
    1013.40,
    None,
    1013.15,
    1013.50,
    "1013.30",
    1013.20,
    "error",
    1013.35,
    1013.10,
    None,
    10000,
    1013.45,
    1013.25,
    1013.30,
    "1013.28",
    1013.40,
    None,
    1013.15,
    1013.50,
    -999,
    1013.35,
    1013.20,
    1013.25,
    "1013.22"
  ],
  "luminosite_atelier": [
    450,
    None,
    465,
    "470",
    455,
    460,
    None,
    "N/A",
    475,
    458,
    -1000,
    462,
    467,
    None,
    461,
    "464",
    459,
    99999,
    468,
    463,
    "466",
    457,
    471,
    None,
    465
  ]
}




capteur = Capteur(mesures_brutes)
capteur.nettoyer(limites)

print(capteur.nombre_valeurs_valides("temperature_bureau"))
print(capteur.moyenne("temperature_bureau"))
print(capteur.minimum("temperature_bureau"))
print(capteur.maximum("temperature_bureau"))
print(capteur.amplitude("temperature_bureau"))
print(capteur.nombre_anomalies("temperature_bureau"))

print(capteur.nombre_anomalies("humidite_serre"))
print(capteur.nombre_anomalies("pression_capteur_ext"))
print(capteur.nombre_anomalies("luminosite_atelier"))