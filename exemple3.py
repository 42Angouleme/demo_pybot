from Robot import Robot

robot = Robot()


def afficher_camera():
    robot.afficher_camera()
    robot.afficher_bouton("Prendre photo", robot.prendre_photo)


longueur = 800
hauteur = 600

robot.allumer_ecran()

robot.changer_titre("Exemple 2")

robot.ajout_evenement('q', robot.eteindre_ecran)

robot.ajout_bouton('Afficher camera', afficher_camera)

robot.lancer_boucle()
