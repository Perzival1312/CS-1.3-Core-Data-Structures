from itertools import permutations as perm

list(perm('abcdefgh'))
# list is ~7millisec
# set is ~12 millisec
