import turtle


def toit1(x: float, y_sol: float, niveau: int) -> None:
    """
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    """
    turtle.begin_fill()
    turtle.begin_poly()
    # Base of roof
    turtle.penup()
    turtle.goto((x - 70), (60 * niveau))
    turtle.pendown()
    turtle.goto((x + 70), (60 * niveau))
    # Right of roof
    turtle.penup()
    turtle.goto((x + 70), (60 * niveau))
    turtle.pendown()
    turtle.goto((x), (60 * niveau + 40))
    # Left of roof
    turtle.penup()
    turtle.goto((x), (60 * niveau + 40))
    turtle.pendown()
    turtle.goto((x - 70), (60 * niveau))

    turtle.end_fill()


if __name__ == "__main__":
    toit1(0, 0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
