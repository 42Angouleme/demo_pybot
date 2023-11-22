from .module_ecran import module as ecran


class Robot:
    def __init__(self, debug=False):
        self.ecran = ""
        self.visage = ""
        self.visages = {}
        self.debug = debug

        self.configurer()

    def allumer_ecran(self, width=400, height=300):
        self.ecran = ecran.run(self, width, height)

    def eteindre_ecran(self):
        self.ecran.quit()

    def switch_visage(self):
        # Temporary function
        import random
        face = random.choice(list(self.visages.keys()))
        self.configurer_visage(face)

    def configurer_visage(self, visage):
        self.visage = visage

    def recevoir_visage(self):
        return self.visage

    def recevoir_images_visages(self):
        return self.visages

    def enregistrer_les_visages(self, file):
        import random
        fichier = open(file, 'r')
        lignes = fichier.readlines()
        fichier.close()
        for ligne in lignes:
            ligne = ligne.replace(' ', '')
            if len(ligne) > 3:
                valeurs = ligne.split('=')
                valeurs[1] = valeurs[1].replace('\n', '')
                self.visages[valeurs[0]] = valeurs[1]
        premier_visage = random.choice(list(self.visages.keys()))
        self.configurer_visage(premier_visage)

    def configurer(self):
        self.enregistrer_les_visages("robot/assets/visages.txt")

    def lancer_boucle(self):
        self.ecran.loop()

    def changer_titre(self, title):
        self.ecran.title(title)

    def ajouter_bouton(self, titre, function):
        self.ecran.ajouter_bouton(titre, function)

    def supprimer_bouton(self, titre):
        self.ecran.supprimer_bouton(titre)

    def afficher_camera(self):
        self.ecran.afficher_camera()

    def eteindre_camera(self):
        self.ecran.eteindre_camera()

    def enregistrer_photo(self):
        self.ecran.enregistrer_photo()

    def verifier_photo(self):
        from pathlib import Path
        return Path("robot/photo.jpg").is_file()

    def afficher_photo(self):
        self.ecran.afficher_photo()

    def afficher_visage_triste(self):
        self.configurer_visage("triste")
        self.ecran.afficher_visage()

    def afficher_visage_content(self):
        self.configurer_visage("content")
        self.ecran.afficher_visage()

    def afficher_visage_fier(self):
        self.configurer_visage("fier")
        self.ecran.afficher_visage()

    def afficher_visage_colere(self):
        self.configurer_visage("colere")
        self.ecran.afficher_visage()
