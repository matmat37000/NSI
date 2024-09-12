from rectangle import rectangle
import turtle


def fenetre(x: float, y: float) -> None:
    """
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    """
    rectangle(x, y, 30, 30)
    pass


if __name__ == "__main__":
    fenetre(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
