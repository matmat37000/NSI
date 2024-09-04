# Feuille exercices S01-01: Les Fonctions

## Exercice 1

> Fais en cours

la fonction `ma_fonction` est déclaré et prend comme argument positionel `x` et renvoie `y` qui est un resulta du calcule $3 * x + 2$. La fonction est ensuite appelé avec `x = 4` et renvoie donc dans la variable `solution` $14$.

## Exercice 2

```python
def ma_fonction(x: float) -> float:
    y: float = x**2 + 2 * x + 10
    return y
```

## Exercice 3

La fonction `une_autre_fonction(5, 3)` renvoie le resulta du calcule $3 * x + b$ soit $3 * 5 + 3 = 18$.

## Exercice 4

La fonction `dit_bonjour('toto', 10)` renvoie le formated string suivant: `"Bonjour toto, vous avez 10 ans."`. Elle n'écrit rien dans la console, elle ne contient pas de `print` ou `input`.

## Exercice 5

La fonction suivante renvoie juste la chaine de char suivante `"voici une fonction qui ne sert à rien"`, elle ne prend aucun argument et n'écrit pas dans la mémoire -> dans la console.

## Exercice 6

````python
def valeur_absolue(valeur: int) -> int:
    '''
    Renvois la valeur absolue du nombre entier passé en argument.
    Exemple:
    >>> valeur_absolue(3)
    3
    >>> valeur_absolue(-5)
    5
    '''
    if valeur < 0:
        return valeur * -1
    else:
        return valeur
````

## Exercice 7

```python
def max2(a: int, b: int) -> int:
    '''
    Renvoie les plus grand entier passé en argument
    '''

    if a > b:
        return a
    else: 
        return b


```

## Exercice 8

```python
def max3(a: int, b: int, c: int) -> int:
    '''
    Renvoie les plus grand entier passé en argument
    > Depand de la fonction max2(a, b)
    '''

    if max2(a, b) < c:
        return c
    else:
        return max2(a, b)
```

## Exercice 9

```python
def test_pythagore(a: int, b: int, c: int) -> bool:
    '''
    Prend 3 entier en arguments et renvoie un booléen indiquand si
    a² + b² = c²
    '''
    if c != max3(a, b, c):
        return false
    else:
        return a**2 + b**2 == c**2

```
