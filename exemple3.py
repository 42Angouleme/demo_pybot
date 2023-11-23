from pybot import Robot
robot = Robot()


def afficher_camera():
    robot.supprimer_bouton("Afficher camera")
    robot.supprimer_bouton("Afficher photo")
    robot.supprimer_bouton("Quitter robot")
    robot.ajouter_bouton("Enregistrer photo", robot.enregistrer_photo)
    robot.ajouter_bouton("Eteindre camera", eteindre_camera)
    robot.afficher_camera()


def eteindre_camera():
    robot.supprimer_bouton("Enregistrer photo")
    robot.supprimer_bouton("Eteindre camera")
    robot.ajouter_bouton("Quitter robot", robot.eteindre_ecran)
    robot.ajouter_bouton("Afficher photo", afficher_photo)
    robot.ajouter_bouton("Afficher camera", afficher_camera)
    robot.eteindre_camera()


def afficher_photo():
    if robot.verifier_photo():
        robot.afficher_photo()
    else:
        robot.afficher_visage_content()


def lancer_robot():
    longueur = 1024
    hauteur = 800

    robot.allumer_ecran(longueur, hauteur)
    robot.changer_titre("Exemple 3")

    robot.ajouter_bouton("Quitter robot", robot.eteindre_ecran)
    robot.ajouter_bouton("Afficher camera", afficher_camera)
    robot.ajouter_bouton("Afficher photo", afficher_photo)

    robot.lancer_boucle()


lancer_robot()
