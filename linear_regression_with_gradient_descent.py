import math
import numpy as np


def generate_data(w, b, n=1000):
    xs = 5 * np.random.rand(n)
    ys = w * xs + b + np.random.normal(0, 1, n)
    return xs, ys


def f_lr(x, xs, ys, w, b, r=0.001):
    n = len(xs)
    dl_dw = -2 * np.matmul(np.transpose(xs), ys - (w * xs + b)) / n
    dl_db = -2 * np.matmul(np.ones(n), ys - (w * xs + b)) / n
    # Note: normalise L by sample size so the hyperparameters such as learning rate are not sensitive to sample size

    w -= r * dl_dw
    b -= r * dl_db

    return w * x + b, w, b


def avg_loss(xs, ys, w, b):
    e = ys - (w * xs + b)
    return np.linalg.norm(e) / math.sqrt(len(xs))


data_x, data_y = generate_data(3, 2)
e_w = 1
e_b = 0
n_run = 15000
for i in range(n_run):
    y, e_w, e_b = f_lr(x=1, xs=data_x, ys=data_y, w=e_w, b=e_b)
    if i % (n_run / 15) == 0:
        print(i, y, avg_loss(data_x, data_y, e_w, e_b))
