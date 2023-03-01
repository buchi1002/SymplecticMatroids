import itertools
from collections import defaultdict
import numpy as np

def make_ground_set(n:int) -> list:
    return list(range(-n,0)) + list(range(1,n+1))

def make_admissible_permutations(n:int) -> list:
    tu_lefts = tuple(itertools.permutations(range(1,n+1)))
    tu_starreds = tuple(itertools.product((1,-1), repeat=n))

    W = list()
    for w_left in tu_lefts:
        for starred in tu_starreds:
            w = tuple([w_left[-(i+1)]*((-1)*starred[-(i+1)]) for i in range(n)] + [w_left[i]*starred[i] for i in range(n)])
            W.append(w)

    return W

def make_admissible_subsets(n:int, k:int) -> list:
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
    j = make_ground_set(len(w)//2)
    for idx in range(len(w)):
        w_ordering[w[idx]] = j[idx]

    return w_ordering

def make_base(n:int, k:int, len_basis:int) -> list:
    Jk = make_admissible_subsets(n,k)
    W = make_admissible_permutations(n)
    candidate_base = list(list(s) for s in itertools.combinations(Jk, len_basis))

    # make dict admissible permutation to admissible orderings
    w_orderings = dict()
    for w in W:
        w_orderings[w] = make_admissible_ordering(w)

    base = list()
    for candidate in candidate_base:
        # for all w, there exists "optimal set" O in candidate_base
        flag0 = True
        for w_order in w_orderings:
            # exists optimal set O
            flag1 = False
            for idxO in range(len(candidate)):
                O = candidate[idxO].copy()
                O.sort(key= lambda x:w_order[x])

                # set O is optimal in candidate
                flag2 = True
                for idxB in range(len(candidate)):
                    B = candidate[idxB].copy()
                    B.sort(key= lambda x:w_order[x])
                    for i in range(k):
                        # Oi < Bi then O is not optimal
                        if w_order[O[i]] < w_order[B[i]]:
                            flag2 = False
                            break
                    # if O is not optimal
                    if not flag2:
                        break
                # if O is optimal
                if flag2:
                    flag1 = True
                    break
            # for all w, there exists optimal O
            flag0 = flag0 and flag1
            if not flag1:
                break

        if flag0:
            base.append(candidate)

    return base


def make_isotropic_subspace(q:int, n:int, k:int, limit:int = -1, start:int = 0) -> list:

    all_row = itertools.product(range(q),repeat = n)
    all_row = tuple(map(lambda x:np.array(x), all_row))

    matrices = list(itertools.combinations_with_replacement(all_row,k))
    matrices = list(map(lambda x:np.array(x), matrices))

    matrices = matrices[start:]

    isotropic_subsspace = list()
    if limit == -1:
        for AB in itertools.combinations(matrices, 2):
            A, B = AB
            ABt = (A@B.T)%q
            if np.array_equal(ABt, ABt.T):
                isotropic_subsspace.append((A, B))

    else:
        count = 0
        for AB in itertools.combinations(matrices, 2):
            A, B = AB
            ABt = (A@B.T)%q
            if np.array_equal(ABt, ABt.T):
                isotropic_subsspace.append((A, B))
                count += 1

                if count >= limit:

                    return isotropic_subsspace

    return isotropic_subsspace
