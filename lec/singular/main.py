"""Example of using the singular decomposition to compress image."""

from matplotlib import pyplot as plt
import numpy as np


SETTINGS = {
    'file': 'forest.png',
    'factor': 10,
}


def main():
    """The entry point."""

    A = plt.imread(SETTINGS['file'])

    r = A.shape[1] // SETTINGS['factor']

    A1, A2, A3 = to_channels(A)

    t1 = Triade(*trunc(A1, r))
    t2 = Triade(*trunc(A2, r))
    t3 = Triade(*trunc(A3, r))

    im = Image(t1, t2, t3)

    before = A.shape[0]*A.shape[1]*A.shape[2]
    print(round(1 - (im.size() / before), 2))

    plt.subplot(121)
    plt.imshow(A)

    plt.subplot(122)
    plt.imshow(im.get_matrix())

    plt.show()


class Triade:
    """Result of singular decomposition."""

    def __init__(self, u, s, v):
        self.u = u
        self.s = s
        self.v = v

    def get_tuple(self):
        """Return self as a tuple."""

        return (self.u, self.s, self.v)


class Image:
    """Compressed image."""

    def __init__(self, t1, t2, t3):
        self.ts = [t1, t2, t3]

    def get_matrix(self):
        """Get matrix (for visualization)."""

        bs = [None, None, None]
        for i in range(3):
            bs[i] = restore(*self.ts[i].get_tuple())
        return from_channels(*bs)

    def size(self):
        """Calculate size."""

        s = 0
        for i in range(3):
            s += self.ts[i].u.shape[0] * self.ts[i].u.shape[1]
            s += self.ts[i].s.shape[0] * self.ts[i].s.shape[1]
            s += self.ts[i].v.shape[0] * self.ts[i].v.shape[1]
        return s


def trunc(A, r):
    """Singular decomposition and truncate result. There is
    TruncatedSVD in numpy."""

    m = A.shape[0]
    n = A.shape[1]

    u, s, vh = np.linalg.svd(A)

    sm = np.zeros((m, n))
    sm[:n, :m] = np.diag(s)

    u = u[:, :r]
    sm = sm[:, :r]
    vh = vh[:r, :]

    return u, sm, vh


def restore(u, s, vh):
    """Restore matrix from triade."""

    m = s.shape[0]
    r = s.shape[1]

    u_ = np.zeros((m, m))
    u_[:, :r] = u
    return u_.dot(s.dot(vh))


def to_channels(m):
    """Split image matrix to channels."""

    ms = [[], [], []]
    for row in m:
        rs = [[], [], []]
        for elem in row:
            for i in range(3):
                rs[i].append(elem[i])

        for i in range(3):
            ms[i].append(rs[i])

    return np.array(ms[0]), np.array(ms[1]), np.array(ms[2])


def from_channels(m1, m2, m3):
    """Build image matrix from channels."""

    m = []
    for r1, r2, r3 in zip(m1, m2, m3):
        r = []
        for e1, e2, e3 in zip(r1, r2, r3):
            e = [e1, e2, e3]
            r.append(e)
        m.append(r)
    return np.array(m)


if __name__ == "__main__":
    main()
