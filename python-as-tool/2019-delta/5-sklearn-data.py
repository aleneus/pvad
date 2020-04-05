import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits, load_iris
from sklearn.decomposition import PCA

from helpers import *


def digits_example_1():
    digits = load_digits()
    print(dir(digits))
    print(digits.DESCR)
    pause()
    print(digits.data.shape)
    print(digits.target_names)
    print(digits.target)
    pause()
    # plt.figure()
    plt.gray()
    plt.matshow(digits.images[9])
    plt.show()


def digits_example_2():
    digits, targets = load_digits(return_X_y=True)
    print(digits.shape)
    print(targets.shape)
    pause()
    for i in range(10):
        s = ""
        for j in range(8):
            s += "{}  ".format(digits.data[i, j])
        print("{}... : {}".format(s, targets[i]))


def iris_example():
    iris = load_iris()
    X = iris.data
    print(X.shape)
    pause()
    y = iris.target

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    colors = ['r', 'g', 'b']
    print(X_pca.shape)
    pause()

    plt.figure()
    for color, i, target in zip(colors, [0, 1, 2], iris.target_names):
        plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1])
    plt.show()


if __name__ == "__main__":
    # digits_example_1()
    # digits_example_2()
    iris_example()
