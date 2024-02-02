class Ferry:
    def __init__(self, nom, places_voiture, voitures_max, nombre_cabine):
        self.nom = nom
        self.cie = "CGM"
        self.places_voiture = places_voiture
        self.voitures_a_bord = 0
        self.voitures_max = voitures_max
        self.port_depart = "Le havre"
        self.port_arrivee = "Cherbourg"
        self.nom_capitain = ""
        self.nombre_cabine = 100

    def embarquer_voiture(self, nombre_voitures):
        if self.voitures_a_bord + nombre_voitures <= self.places_voiture:
            self.voitures_a_bord += nombre_voitures
            print(f"{nombre_voitures} voiture(s) ont été embarquée(s) sur le ferry {self.nom}.")
            return nombre_voitures
        else:
            places_disponibles = self.places_voiture - self.voitures_a_bord
            print(f"Impossible d'embarquer {nombre_voitures} voiture(s). Il reste seulement {places_disponibles} place(s) disponible(s).")
            return nombre_voitures

    def debarquer_voiture(self, nombre_voitures):
        if self.voitures_a_bord >= nombre_voitures:
            self.voitures_a_bord -= nombre_voitures
            print(f"{nombre_voitures} voiture(s) ont été débarquée(s) du ferry {self.nom}.")
            return nombre_voitures
        else:
            print(f"Impossible de débarquer {nombre_voitures} voiture(s). Il n'y a que {self.voitures_a_bord} voiture(s) à bord.")

    def changer_cie(self,nouvelle_cie):
        self.cie = nouvelle_cie
        print(f"Nouvelle cie : {nouvelle_cie}")

    def trajet(self, port_depart, port_arrivee):
        self.port_depart = port_depart
        self.port_arrivee = port_arrivee
        print(f"Arrivee : {port_arrivee}")
        print(f"Depart : {port_depart}")

    def changer_captaine(self, nom_capitain):
        self.nom_capitain = nom_capitain
        print(f"Nouveau CNE : {nom_capitain}")


    def modifier_volume_cabine(self, nombre):
        self.nombre_cabine = nombre
        print(f"Nouveau nombre de cabine : {nombre}")