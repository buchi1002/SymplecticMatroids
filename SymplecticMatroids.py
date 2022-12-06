import itertools
from collections import defaultdict
import numpy as np

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
            K = tuple(nums[i]*starreds[i] for i in range(k))

            Jk.append(K)

    return Jk

def make_admissible_orderings(w:tuple) -> set:
    admissible_orderings = set()
    for es in range(len(w)):
        for eb in range(es,len(w)):
            admissible_orderings.add(es,eb)

    return admissible_orderings


def make_isotropic_subspace(p:int = 3, n:int = 3, k:int = 4) -> list:
    F = list(range(p))
    all_row = itertools.combinations_with_replacement(F,n)
    all_row = list(map(list, all_row))

    matrices = list(itertools.combinations_with_replacement(all_row,k))
    matrices = list(map(lambda x:np.array(list(x)), matrices))
    matrices = matrices[1:]

    isotropic_subsspace = list()
    for idx_A in range(len(matrices)-1):
        for idx_B in range(idx_A + 1,len(matrices)):
            A = matrices[idx_A]
            B = matrices[idx_B]

            ABt = np.dot(A, B.T)%p
            BtA = ABt.T
            if np.array_equal(ABt, BtA) and np.linalg.matrix_rank(np.hstack((A, B)), tol=None) == k:
                isotropic_subsspace.append([A, B, ABt])

    return isotropic_subsspace
