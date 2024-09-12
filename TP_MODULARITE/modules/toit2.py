import turtle
from trait import trait


def toit2(x: float, y_sol: float, niveau: int) -> None:
    """
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    """
    turtle.pensize(10)
    trait((x - 70), (60 * niveau), (x + 70), (60 * niveau))
    turtle.pensize(1)


if __name__ == "__main__":
    toit2(0, 0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
