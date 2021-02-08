"""Examples of some problems in signals."""
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig


DT, FS = 0.02, 50
FILTER_LEN = 301


def synth():
    """Return test signal."""
    freqs = [0.25, 3]
    amps = [1, 0.05]
    ts = np.arange(0, 60, DT)
    xs = amps[0] * np.cos(2*np.pi*freqs[0]*ts) + 50
    xs += amps[1] * np.cos(2*np.pi*freqs[1]*ts) + 50
    return xs, ts


def filt(xs, fband, ntaps=301):
    """Filters signal."""
    h = sig.firwin(cutoff=fband, pass_zero=False, fs=FS, numtaps=ntaps)
    return sig.lfilter(h, [1], xs)


def ex_zero():
    """Effect of zero for the filtration."""
    xs, ts = synth()
    xf = filt(xs, [2, 4], FILTER_LEN)
    xs[len(xs) // 2] = 0
    xfz = filt(xs, [2, 4], FILTER_LEN)

    plt.subplot(311)
    plt.plot(ts[FILTER_LEN:], xs[FILTER_LEN:])
    plt.grid(True)

    plt.subplot(312)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)

    plt.subplot(313)
    plt.plot(ts[FILTER_LEN:], xfz[FILTER_LEN:])
    plt.grid(True)


def ex_jumps():
    """Effect of number of jumps for the filtration."""
    xs, ts = synth()
    for i in range(5):
        xs[len(xs)//2 + i*50] = 0
    xf = filt(xs, [2, 4], FILTER_LEN)

    plt.subplot(211)
    plt.plot(ts[FILTER_LEN:], xs[FILTER_LEN:])
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)


def ex_long_zero():
    """Effect of long zero for the filtration."""
    xs, ts = synth()
    xs[len(xs)//2-300:len(xs)//2] = 0
    xf = filt(xs, [2, 4], FILTER_LEN)

    plt.subplot(211)
    plt.plot(ts[FILTER_LEN:], xs[FILTER_LEN:])
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)


def ex_skip():
    """Skip one value."""
    xs, ts = synth()
    n = len(xs)//2
    xs[n] = None
    xf = filt(xs, [2, 4], FILTER_LEN)

    plt.subplot(211)
    plt.plot(ts[FILTER_LEN:], xs[FILTER_LEN:])
    plt.plot([ts[n-1]], [xs[n-1]], 'rx')
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)


def ex_strange_dynamics():
    """Adequate range, deviating but strange dynamics."""
    bs = [5, 15, 35, -20, -10, 18, 28, 7, 7, 13, -25]
    ts = np.arange(0, 60, 1)
    xs = []
    for i in range(len(ts)):
        xs.append(bs[i % len(bs)])

    plt.plot(ts, xs)
    plt.xlabel("Time [min]")
    plt.ylabel("Temperature")
    plt.grid(True)


def ex_differ():
    """Data about same process are very differ."""
    ts = np.arange(0, 60, 0.02)
    xs1 = np.cos(2*np.pi*1*ts)
    xs2 = np.cos(2*np.pi*1*ts + 0.1)
    bs = np.arange(-0.3, 0.3, 0.01)
    for i in range(len(xs2)):
        xs2[i] = xs2[i] + bs[i % len(bs)]

    plt.subplot(211)
    plt.plot(ts, xs1)
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts, xs2)
    plt.grid(True)


def run(func):
    """Runs example with single figure output."""
    fig = plt.figure()
    func()
    plt.tight_layout()
    plt.savefig("{}.png".format(func.__name__))
    plt.close(fig)


run(ex_zero)
run(ex_jumps)
run(ex_long_zero)
run(ex_skip)
run(ex_strange_dynamics)
run(ex_differ)
