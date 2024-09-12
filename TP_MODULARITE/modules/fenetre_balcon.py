import turtle
from rectangle import rectangle
from trait import trait


# FIXE: Correct but not perfect
def fenetre_balcon(x: float, y: float) -> None:
    """
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    """
    # porte-fenetre

    rectangle(x, y, 30, 50)

    # balcon
    turtle.pensize(3)
    rectangle(x, y - 25, 36, 25)
    x -= 18
    for xb in range(8):
        trait(x - xb, y - 25, x - xb, y)
        x += 6

    pass


if __name__ == "__main__":
    fenetre_balcon(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
