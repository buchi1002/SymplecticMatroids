import itertools
from collections import defaultdict
import numpy as np

def make_base(n:int = 3) -> list:
    return list(range(-n,0)) + list(range(1,n+1))

def make_admissible_permutations(n:int = 3) -> list:
    tu_lefts = tuple(itertools.permutations(range(1,n+1)))
    tu_starreds = tuple(itertools.product((1,-1), repeat=n))

    W = list()
    for w_left in tu_lefts:
        for starred in tu_starreds:
            w = tuple([w_left[-(i+1)]*((-1)*starred[-(i+1)]) for i in range(n)] + [w_left[i]*starred[i] for i in range(n)])
            W.append(w)

    return W

def make_admissible_subsets(n:int = 3, k:int = 2) -> list:
    li_nums = tuple(range(1,n+1))
    li_starreds = tuple(itertools.product((1,-1), repeat=k))

    Jk = list()
    for nums in itertools.combinations(li_nums, k):
        for starreds in li_starreds:
            K = list(nums[i]*starreds[i] for i in range(k))
            K.sort()

            Jk.append(K)

    return Jk

def make_admissible_ordering(w:tuple) -> dict:
    w_ordering = dict()
    j = make_base(len(w)//2)
    for idx in range(len(w)):
        w_ordering[w[idx]] = j[idx]

    return w_ordering


def make_isotropic_subspace(p:int = 3, n:int = 3, k:int = 4) -> list:
    F = list(range(p))
    all_row = itertools.combinations_with_replacement(F,n)
    all_row = tuple(map(lambda x:np.array(x), all_row))

    matrices = list(itertools.combinations_with_replacement(all_row,k))
    matrices = list(map(lambda x:np.array(x), matrices))
    matrices = matrices

    isotropic_subsspace = list()
    for AB in itertools.combinations(matrices, 2):
        A, B = AB
        ABt = np.dot(A, B.T)%p
        if np.array_equal(ABt, ABt.T):
            isotropic_subsspace.append((A, B))

    return isotropic_subsspace
