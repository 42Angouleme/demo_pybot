import module_ecran as ecran


class Robot:
    def __init__(self, debug=False):
        self.ecran = ""
        self.visage = ""
        self.visages = {}
        self.debug = debug

        self.connecte = "no"
        self.eleve = ""
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

    def eleve_connecte(self):
        return self.connecte

    def change_eleve_connecte(self, connecte):
        self.connecte = connecte

    def obtenir_eleve(self):
        return self.eleve

    def configurer_eleve(self, prenom):
        self.eleve = prenom

    def configurer(self):
        self.enregistrer_les_visages("assets/visages.txt")

    # def allumer_camera(self):
    #     self.camera.run()

    def lancer_boucle(self):
        self.ecran.loop()

    def changer_titre(self, title):
        self.ecran.title(title)
