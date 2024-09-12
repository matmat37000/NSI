def somme(nums: list[int]) -> int:
    """
    Return the somme of all the numbers of the list passed as arguments
    >>> somme([1, 3, 7, 14, 5])
    30
    """
    nums_somme: int = 0
    for num in nums:
        nums_somme += num
    return nums_somme


def moyenne(nums: list[int]) -> int:
    """
    Return the 'moyenne' in the list passed as arguments
    >>> moyenne([1, 3, 7, 14, 5])
    6.0
    """
    # num_moyenne: int = 0
    # for num in nums:
    #     num_moyenne += num
    return somme(nums) / len(nums)


if __name__ == "__main__":
    x: list[int] = [1, 3, 7, 14, 5]
    print(somme(x))

    print(moyenne(x))
