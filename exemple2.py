from Robot import Robot

robot = Robot()

longueur = 800
hauteur = 600

robot.allumer_ecran()

robot.changer_titre("Exemple 2")

robot.ajout_bouton('Quitter', robot.eteindre_ecran)

robot.lancer_boucle()
