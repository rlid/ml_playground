import math

import numpy as np
import matplotlib.pyplot as plt


def f_p2c(x):
    return x[0, 0] * np.cos(x[0, 1]), x[0, 0] * np.sin(x[0, 1])


def f_add(x):
    return x[0, 0] + x[0, 1]


def f_mult(x):
    return x[0, 0] * x[0, 1]


def f_min(x):
    return min(x[0, 0], x[0, 1])


def f_nn(x, f, syn1, syn2, r=0.01):
    m_in = np.matmul(x, syn1)  # 1x2 * 2*30 = 1x30
    m_out = np.tanh(m_in)  # 1x30
    fx = np.matmul(m_out, syn2)  # 1x30 * 30x2 = 1x2
    e = f(x) - fx  # 1x2

    syn2 += r * np.matmul(np.transpose(m_out), e)  # 30x1 * 1x2 = 30x2
    s = np.matmul(syn2, np.transpose(e))  # 30X2 * 2X1 = 30x1
    m_in = np.clip(m_in, -1, 1)
    sd = 1 - m_in * m_in  # 1x30
    d = np.transpose(sd) * s * x  # 30x1 * 30x1 * 1x2 = 30x2
    syn1 += r * np.transpose(d)

    return fx, e, syn1, syn2


def run():
    n_run = 100000
    b = 5
    n_in = 3
    n_out = 2
    n_neuron = 30
    syn1 = 0.1 * np.random.rand(n_in, n_neuron)
    syn2 = 0.1 * np.random.rand(n_neuron, n_out)
    s_e = 0
    f = f_min

    n = 10000
    es = np.zeros(n_run)
    for i in range(n_run):
        r = np.random.rand()
        t = math.pi * (2 * np.random.rand() - 1)
        x = np.array([[r, t, b]])

        fx, e, syn1, syn2 = f_nn(x, f=f, syn1=syn1, syn2=syn2)
        es[i] = math.sqrt(np.matmul(e, np.transpose(e)))

        s_e += es[i]
        if (i + 1) % n == 0:
            print(f'n={i + 1}, avg_e={s_e / n}, e_i={es[i]}')
            s_e = 0

    plt.plot(es, 'o', markersize=1)
    plt.grid()
    plt.show()

    fx, e, _, _ = f_nn(np.array([[0.5 * math.sqrt(2), 0.25 * math.pi, b]]), f=f, syn1=syn1, syn2=syn2)
    print(fx, math.sqrt(np.matmul(e, np.transpose(e))))


if __name__ == '__main__':
    run()
