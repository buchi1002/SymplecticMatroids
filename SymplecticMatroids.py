import itertools
from collections import defaultdict
import numpy as np

def make_admissible_orderings(N:int = 3):

    # J = [n]∪[n]*の作成.
    Np = list(range(1, N+1))
    Nm = list(range(-N,0))

    J = Nm + Np

    # 全ての順列について, admissible かどうか調べる.
    AnsSet = set()
    for p in itertools.permutations(J):
        # 順列作成
        w_dict = defaultdict(lambda:set())
        for e1 in range(len(p)-1):
            for e2 in range(e1+1,len(p)):
                w_dict[p[e1]].add(p[e2])

        # admissible 判定
        flag = True
        for e1 in range(len(p)-1):
            for e2 in range(e1+1,len(p)):
                if ((-p[e1]) in w_dict[-p[e2]]) == False:
                    flag = False

        if flag:
            AnsSet.add(p)

    for Ans in AnsSet:
        print("---")
        print(tuple(J))
        print(Ans)

    print("---")
    print(len(AnsSet))

def SearchSymmetrycABt(N:int = 3) -> list:
    L = list(range(N))
    all = list(itertools.combinations_with_replacement(L,N)
)
    matrices = []
    for row1 in all:
        for row2 in all:
            for row3 in all:
                arr = np.array([row1, row2, row3])
                matrices.append(arr)
    matrices = matrices[1:]

    founds = list()
    length = len(matrices)
    O = np.array([[0,0,0] for _ in range(N)])
    for idx_A in range(length-1):
        for idx_B in range(idx_A+1,length):
            A = matrices[idx_A]
            B = matrices[idx_B]

            ABt = np.dot(A,B.T)%3
            BtA = ABt.T
            if (np.array_equal(ABt, O) == False) and np.array_equal(ABt, BtA):
                if np.linalg.matrix_rank(np.hstack((A, B)), tol=None) == 3:
                    founds.append([A, B, ABt])

    for A, B, ABt in founds:
        print("A")
        print(A)
        print("B")
        print(B)
        print("ABt")
        print(ABt)

    print(len(founds))

makep()
print("end")
