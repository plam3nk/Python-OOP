from itertools import permutations


def possible_permutations(lst):
    for item in list(permutations(lst)):
        yield list(item)


[print(n) for n in possible_permutations([1, 2, 3])]