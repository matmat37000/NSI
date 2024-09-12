import turtle


def trait(x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    """
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.pendown()


if __name__ == "__main__":
    trait(0, 0, 100, 100)
    # help(turtle.goto)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
