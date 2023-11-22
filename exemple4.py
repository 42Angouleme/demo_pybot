from pybot import Robot
robot = Robot()


def lancer_robot():
    longueur = 1024
    hauteur = 800

    robot.allumer_ecran(longueur, hauteur)
    robot.changer_titre("Exemple 4")

    robot.ajout_bouton("Quitter robot", robot.eteindre_ecran)

    robot.lancer_boucle()


lancer_robot()
