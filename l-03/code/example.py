import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import random

xs = [0,   1, 2, 3, 4,   5, 6,   7, 8, 9, 10]
ys = [0.1, 1, 3, 1, 0.1, 1, 0.1, 1, 3, 1, 0.1]

fig = plt.figure()
plt.plot(xs, ys, "ro")
plt.grid(True)
plt.savefig("source.png")
plt.close(fig)

f = interp1d(xs, ys, kind="quadratic")
xs = np.linspace(0, 10, 100)
ys = f(xs)

fig = plt.figure()
plt.plot(xs, ys, "g")
plt.grid(True)
plt.savefig("source-more.png")
plt.close(fig)

Ys = []
Y = 0
for y in np.array(ys) / sum(ys):
    Ys.append(Y)
    Y += y

Ys.append(1)
Xs = list(xs)
Xs.append(xs[-1] + (xs[-1] - xs[-2]))

fig = plt.figure()
plt.plot(Xs, Ys, "b")
plt.grid(True)
plt.savefig("prob.png")
plt.close(fig)

fig = plt.figure()
plt.plot(Ys, Xs, "b")
plt.grid(True)
plt.savefig("quantile.png")
plt.close(fig)

Q = interp1d(Ys, Xs, kind="quadratic")

vs = []
for i in range(0, 10000):
    r = random.uniform(0, 1)
    vs.append(Q(r))

fig = plt.figure()
plt.hist(vs, bins=50, density=True)
plt.plot(xs, ys / (sum(ys) * 10/100), "g")
plt.grid(True)
plt.savefig("hist.png")
plt.close(fig)
