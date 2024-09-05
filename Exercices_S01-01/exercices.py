"""
import `doctest.testmod()` to test if all function are correct
"""
from doctest import testmod

# EX 10


def puissance(x: int, n: int) -> int:
    '''
    Return the power of x by n
    >>> puissance(2, 3)
    8
    '''
    r: int = x
    for _ in range(1, n):
        r *= x

    return r

# EX 11


def bissextile(a: int) -> bool:
    '''
    Take `a` as parameter, `a` need to be a year
    return if `a` is a bissextile year (True/False)
    >>> bissextile(2024)
    True
    >>> bissextile(300)
    False
    '''
    if (a % 4 == 0 or a % 400 == 0) and (a % 100 != 0):
        return True
    else:
        return False

# EX 12


def nb_jour_annee(a: int) -> int:
    '''
    Return number of day in the year passed in `a`
    >>> nb_jour_annee(2024)
    366
    >>> nb_jour_annee(300)
    365
    '''
    if bissextile(a):
        return 366
    else:
        return 365

# EX 13


def nb_jour_mois(a: int, m: int) -> int:
    '''
    Return the number of day in the month (m) with the year passed in a

    >>> nb_jour_mois(2024, 2)
    29
    >>> nb_jour_mois(2023, 2)
    28
    >>> nb_jour_mois(2024, 1)
    31
    >>> nb_jour_mois(2024, 4)
    30
    '''
    if m == 2 and bissextile(a):
        return 29
    elif m in [1, 3, 5, 7, 8, 10, 12]:  # HACK: Hard coded value
        return 31
    elif m in [4, 6, 9, 11]:  # HACK: Hard coded value
        return 30
    else:
        return 28

# EX 14
def nb_jours(j1: int, m1: int, a1: int, j2: int, m2: int, a2: int, include_end_date: bool = False) -> int:
    '''
    Return days between j1/m1/a1 and j2/m2/a2
    '''
    annee1: int = j1 + int(include_end_date) # nb_jour_annee(a1) -
    annee2: int = j2
    for m in range(1, m1):
        annee1 += nb_jour_mois(a1, m)
    for m in range(1, m2):
        annee2 += nb_jour_mois(a2, m)

    annee3: int = 0

    for year in range(a1, a2):
        annee3 += nb_jour_annee(year)

    return annee2 - annee1 + annee3


if __name__ == "__main__":
    testmod()
    print(nb_jours(4, 9, 2021, 5, 9, 2021))
