# **************************************************************#
#                                                              #
#              Python Robot - mdaadoun - 2023                  #
#                                                              #
# **************************************************************#

from .Ecran import Ecran


def run(robot, width, height):
    win = Ecran(robot)
    return win.run(width, height)
