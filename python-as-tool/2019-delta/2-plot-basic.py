import matplotlib.pyplot as plt
import numpy as np

from helpers import *


def plot_example():
    p = [81, 83, 80, 81, 71, 72, 71, 75, 73, 67, 68, 64, 63, 64, 67, 64, 59]
    t = [1991+i for i in range(len(p))]

    fig = plt.figure()

    plt.subplot(121)
    plt.plot(t, p, color='g')
    plt.ylim(0, 100)

    plt.subplot(122)
    plt.plot(t, p, color='r', linewidth=3)
    p1d = np.poly1d(np.polyfit(t, p, 1))
    pf = p1d(t)
    plt.plot(t, pf, color='k', linewidth=5)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    plot_example()
