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
        r = r * x

    return r

# EX 11



if __name__ == "__main__":
    testmod()
