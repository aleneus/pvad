import matplotlib.pyplot as plt

xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [0, 1, 3, 1, 0, 1, 0, 1, 3, 1, 0]

plt.plot(xs, ys, "ro")
plt.grid(True)
plt.savefig("e1.png")
