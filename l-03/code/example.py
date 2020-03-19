import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import random

xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [0, 1, 3, 1, 0, 1, 0, 1, 3, 1, 0]

fig = plt.figure()
plt.plot(xs, ys, "ro")
plt.grid(True)
plt.savefig("e1.png")
plt.close(fig)


xs = np.array([0, 0.5, 1, 2, 3, 3.5, 4,   5, 6,   6.5, 7, 8, 9, 9.5, 10])
ys = np.array([0, 0.3, 1, 3, 1, 0.3, 0.1, 1, 0.1, 0.3, 1, 3, 1, 0.3, 0])

f = interp1d(xs, ys, kind="cubic")
xis = np.linspace(0, xs[-1], 100)
yis = f(xis)

yis = yis / (sum(yis) * 10/100)

fig = plt.figure()
plt.plot(xis, yis, "b")
plt.grid(True)
plt.savefig("e2.png")
plt.close(fig)


F = []
xfs = []
val = 0
for x, y in zip(xis, yis):
    s = y * 10/100
    val = val + s
    if val > 1:
        break
    F.append(val)
    xfs.append(x)

fig = plt.figure()
plt.plot(xfs, F, "b")
plt.grid(True)
plt.savefig("e3.png")
plt.close(fig)


fig = plt.figure()
plt.plot(F, xfs, "b")
plt.grid(True)
plt.savefig("e4.png")
plt.close(fig)


Q = interp1d(F, xfs, kind="cubic")

vs = []
for i in range(0, 10000):
    r = random.uniform(0, 1)
    if r < 0 or r > max(F):
        continue
    vs.append(Q(r))

fig = plt.figure()
plt.hist(vs, bins=50, density=True)
plt.plot(xis, yis, "b")
plt.grid(True)
plt.savefig("e5.png")
plt.close(fig)
