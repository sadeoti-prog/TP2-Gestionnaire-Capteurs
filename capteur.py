
class Capteur:
    """Représente un capteur et permet de nettoyer ses mesures."""

    def __init__(self, nom, mesures_brutes):
        self.nom = nom
        self.mesures_brutes = mesures_brutes
        self.mesures_nettoyees = []
        self.nb_anomalies = 0

    def nettoyer(self, minimum, maximum):
        """Conserve les mesures numériques comprises entre les limites."""

        self.mesures_nettoyees = []
        self.nb_anomalies = 0

        for mesure in self.mesures_brutes:

            # Essayer de convertir la mesure en nombre
            try:
                valeur = float(mesure)

            # Si impossible, compter une anomalie
            except (ValueError, TypeError):
                self.nb_anomalies += 1
                continue

            # Vérifier que la mesure respecte les limites
            if minimum <= valeur <= maximum:
                self.mesures_nettoyees.append(valeur)
            else:
                self.nb_anomalies += 1

    def nombre_valides(self):
        """Retourne le nombre de mesures valides."""
        return len(self.mesures_nettoyees)

    def moyenne(self):
        """Calcule la moyenne des mesures valides."""
        if not self.mesures_nettoyees:
            return None

        return sum(self.mesures_nettoyees) / len(self.mesures_nettoyees)

    def minimum(self):
        """Retourne la plus petite mesure valide."""
        if not self.mesures_nettoyees:
            return None

        return min(self.mesures_nettoyees)

    def maximum(self):
        """Retourne la plus grande mesure valide."""
        if not self.mesures_nettoyees:
            return None

        return max(self.mesures_nettoyees)
