import matplotlib.pyplot as plt
import sys
import numpy as np

import matplotlib
matplotlib.use('Agg')


def plot_wave(x, path='./wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)


def plot_ak(a, path='./freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)


def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    return np.matmul(np.linalg.inv(B), x)


def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    return np.matmul(B, a)


def gen_basis(N):
    # TODO
    k = 1000  # 根据ppt图示，取超参k为1000
    b = np.zeros((N, k))
    for i in range(N):
        for j in range(k):
            if j == 0:
                b[i, j] = 1 / np.math.sqrt(N)
            else:
                b[i, j] = np.math.sqrt(
                    2/N) * np.math.cos((i+0.5)*j*np.math.pi/N)
    return b


if __name__ == '__main__':

    signal_path = sys.argv[1]

    N = 1000  # 先验知识N等于1000

    # test 运行方法：python hw3.py test.txt
    # test_x = np.loadtxt(signal_path).reshape((1000,))
    # plot_wave(test_x, "./img/test_wave.png")
    # B = gen_basis(N)
    # test_a = CosineTrans(test_x, B)
    # plot_ak(test_a, "./img/test_a.png")
    # # 区分s1和s2两个波形
    # s1_a = test_a.copy()
    # s1_a[100:] = 0
    # s2_a = test_a.copy()
    # s2_a[:100] = 0
    # plot_ak(s1_a, "./img/s1_a.png")
    # plot_ak(s2_a, "./img/s2_a.png")
    # s1_x = InvCosineTrans(s1_a, B)
    # s2_x = InvCosineTrans(s2_a, B)
    # plot_wave(s1_x, "./img/s1_wave.png")
    # plot_wave(s2_x, "./img/s2_wave.png")

    # hw 随便找了一个学号的作业 运行方法：python hw3.py b03602036.txt
    hw_x = np.loadtxt(signal_path).reshape((1000,))
    plot_wave(hw_x, "./img/hw_wave.png")
    B = gen_basis(N)
    hw_a = CosineTrans(hw_x, B)
    plot_ak(hw_a, "./img/hw_a.png")
    # 提取f1和f3两个波形
    f1_a = hw_a.copy()
    f1_a[100:] = 0
    f3_a = hw_a.copy()
    f3_a[:400] = 0
    f3_a[550:] = 0
    f1_x = InvCosineTrans(f1_a, B)
    f3_x = InvCosineTrans(f3_a, B)
    np.savetxt("f1_x.txt", f1_x)
    np.savetxt("f3_x.txt", f3_x)
    plot_wave(f1_x, "./img/f1_wave.png")
    plot_wave(f3_x, "./img/f3_wave.png")
