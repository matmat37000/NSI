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
    if (a % 4 == 0 or a % 400 == 0) and (a % 100 != 0) :
        return True
    else:
        return False

# EX 12
def nb_jour_mois(a: int) -> int:
    '''
    Return number of day in the year passed in `a`
    >>> nb_jour_mois(2024)
    366
    >>> nb_jour_mois(300)
    365
    '''
    if bissextile(a):
        return 366
    else:
        return 365

if __name__ == "__main__":
    testmod()
