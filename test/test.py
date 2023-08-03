# from random import randint
#
# n = tuple(zip((randint(1, 8) for _ in range(8)), (randint(1, 8) for _ in range(8))))
#
# for i in n:
#     print(i[0], i[1])

from itertools import combinations, permutations

# print(f'♕{chr(8197)}♕')
# print(f'♕{chr(8239)}♕')
# print(f'♕ ♕')

ALL_combinations = list(combinations([i for i in range(8)], 2))
ALL_permutations = list(permutations([i for i in range(8)], 2))
print(ALL_combinations)
print(ALL_permutations)