import itertools
from collections import defaultdict
import numpy as np

def ConfirmProp(N:int = 3):
    Np = list(range(1, N+1))
    Nm = list(range(-N,0))

    J = Nm + Np

    AnsSet = set()
    for v in itertools.permutations(J):
        d = defaultdict(lambda:set())
        for e1 in range(len(v)-1):
            for e2 in range(e1+1,len(v)):
                d[v[e1]].add(v[e2])

        flag = True
        for e1 in range(len(v)-1):
            for e2 in range(e1+1,len(v)):
                if ((-v[e1]) in d[-v[e2]]) == False:
                    flag = False

        if flag:
            AnsSet.add(v)

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

SearchSymmetrycABt()
print("end")
