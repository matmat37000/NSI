import turtle


def rectangle(x: float, y: float, w: float, h: float) -> None:
    """
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    """
    turtle.penup()
    turtle.setpos((x - w) / 2, (y - h) / 2)
    turtle.pendown()
    for i in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)


if __name__ == "__main__":
    rectangle(0, 0, 150, 100)
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
    turtle.circle(3)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
