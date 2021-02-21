# github.com/aleneus/pvad

import random

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np


def get_data():
    """Get source data. Stub."""

    xs = [0,   1, 2, 3, 4,   5, 6,   7, 8, 9, 10]
    fs = [0.1, 1, 3, 1, 0.1, 1, 0.1, 1, 3, 1, 0.1]
    return xs, fs


def plot_points(xs, fs, fname, color="#880000"):
    """Plot points to file."""

    fig = plt.figure()
    plt.plot(xs, fs, "o", color=color)
    plt.grid(True)
    plt.savefig(fname)
    plt.close(fig)


def plot_curve(xs, fs, fname, color="#008800"):
    """Plot curve to file."""

    fig = plt.figure()
    plt.plot(xs, fs, color=color)
    plt.grid(True)
    plt.savefig(fname)
    plt.close(fig)


def prob_values(xs, fs):
    """Return values of probability function."""

    Xs = list(xs)
    Xs.append(xs[-1] + sampling_period(xs))

    Fs = []
    prev = 0
    for f in np.array(fs) / sum(fs):
        Fs.append(prev)
        prev += f
    Fs.append(prev)

    return Xs, Fs


def sampling_period(xs):
    """Return sampling period."""
    return xs[1] - xs[0]


def quantile_func(Xs, Fs):
    """Return quantile function. Stub."""
    return interp1d(Fs, Xs, kind='quadratic')


def custom_rand(quantile_func):
    """Return random value using quantile function."""
    return quantile_func(random.uniform(0, 1))


class CustomRandomizer:
    def __init__(self, xs, fs):
        self.func = quantile_func(*prob_values(xs, fs))

    def __call__(self):
        return custom_rand(self.func)


def main():
    xs, fs = get_data()

    plot_points(xs, fs, "source.png")

    f = interp1d(xs, fs, kind='quadratic')
    xs = np.linspace(0, 10, 100)
    fs = f(xs)

    plot_curve(xs, fs, "source-more.png")

    Xs, Fs = prob_values(xs, fs)

    plot_curve(Xs, Fs, "prob.png")
    plot_curve(Fs, Xs, "quantile.png")

    Q = quantile_func(Xs, Fs)

    vs = [custom_rand(Q) for i in range(1000)]

    fig = plt.figure()
    plt.hist(vs, bins=50, density=True)
    plt.savefig("hist.png")
    plt.close(fig)


if __name__ == "__main__":
    main()
