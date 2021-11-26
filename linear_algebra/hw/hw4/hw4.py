import sys
import numpy as np
from numpy.lib.function_base import disp
import pandas as pd


def load(fname):
    f = open(fname, 'r').readlines()
    n = len(f)
    ret = {}
    for l in f:
        l = l.split('\n')[0].split(',')
        i = int(l[0])
        ret[i] = {}
        for j in range(n):
            if str(j) in l[1:]:
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    ret = pd.DataFrame(ret).values
    return ret


def get_tran(g):
    # TODO
    g = g.astype("float")
    for i in range(g.shape[0]):
        s = np.sum(g[:, i])
        g[:, i] /= s
    return g


def cal_rank(t, d=0.85, max_iterations=1000, alpha=0.001):
    # TODO
    n = t.shape[0]
    r = np.ones(n) / n
    damp = r * (1-d)  # 阻尼系数
    i = 0
    new_r = r
    while i < max_iterations:
        new_r = d * np.matmul(t, r) + damp
        if dist(r, new_r) < alpha:
            return new_r
        i += 1
        r = new_r
    return new_r


def save(t, r):
    # TODO
    np.savetxt("1.txt", t, "%.1f")
    np.savetxt("2.txt", r, "%.16f")


def dist(a, b):
    return np.sum(np.abs(a-b))


def main():
    # ex运行方式：python hw4.py ./ex/graph.txt
    # hw运行方式：pytohn hw4.py ./graph/graph_0.txt
    graph = load(sys.argv[1])
    transition_matrix = get_tran(graph)
    rank = cal_rank(transition_matrix)
    save(transition_matrix, rank)


if __name__ == '__main__':
    main()
