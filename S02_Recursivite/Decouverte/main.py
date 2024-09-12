from sys import getrecursionlimit, setrecursionlimit


def somme(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + somme(n - 1)


def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    pass
