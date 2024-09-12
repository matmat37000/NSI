from math import pi


class Aire:
    def triangle(base: float, hauteur: float) -> float:
        """
        Calcule l'aire d'un triangle
        @param: base: float
        @param hauteur: float
        _return: float
        >>> triangle(10, 4)
        20
        """

        return base * hauteur

    def circle(radius: float) -> float:
        """
        Return the aera of a circle
        @param radius: float
        _retunr: float
        """
        return pi * radius**2

