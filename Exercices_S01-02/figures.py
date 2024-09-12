import turtle as t


class Geometry:

    def rectangle(longueur: float, largeur: float, fill_color: str) -> None:
        # t = turtle.Turtle()
        t.color(fill_color)
        t.fillcolor(fill_color)
        t.begin_fill()
        for i in range(2):
            t.forward(longueur)
            t.left(90)
            t.forward(largeur)
            t.left(90)
        t.end_fill()

    def triangle(longueur: float, fill_color: str) -> None:
        # t = turtle.Turtle()
        t.color(fill_color)
        t.fillcolor(fill_color)
        t.begin_fill()
        for i in range(3):
            t.forward(longueur)
            t.left(120)
        t.end_fill()

    def circle(rayon: float, fill_color: str) -> None:
        # t = turtle.Turtle()
        t.pencolor(fill_color)
        t.fillcolor(fill_color)
        t.begin_fill()
        t.circle(radius=rayon)
        t.end_fill()
