"""Functions for calculation quantities."""
import math

TO_RADS = math.pi / 180


def __are_radians(angles):
    for angle in angles:
        if abs(angle) > 2 * math.pi:
            return False
    return True


def active_power_n(ums, uas, ims, ias, check_rads=True):
    """Return active powers by voltages and currents."""
    print('active_power_n()')
    coeff = 1
    if check_rads:
        if not __are_radians(uas) or not __are_radians(ias):
            coeff = TO_RADS

    return [um * im * math.cos((ia - ua) * coeff)
            for um, ua, im, ia in zip(ums, uas, ims, ias)]


def reactive_power_n(ums, uas, ims, ias, check_rads=True):
    """Return reactive powers by voltages and currents."""
    print('reactive_power_n()')
    coeff = 1
    if check_rads:
        if not __are_radians(uas) or not __are_radians(ias):
            coeff = TO_RADS

    return [um * im * math.sin((ia - ua) * coeff)
            for um, ua, im, ia in zip(ums, uas, ims, ias)]


def full_power_n(ps, qs):
    """Return full powers by active powers and reactive powers."""
    print('full_power_n()')
    res = []
    for p, q in zip(ps, qs):
        res.append((p**2 + q**2) ** 0.5)
    return res
