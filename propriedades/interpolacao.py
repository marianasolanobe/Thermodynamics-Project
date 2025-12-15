import numpy as np

def interp_1d(x, x_vals, y_vals):
    return np.interp(x, x_vals, y_vals)


def interp_dupla(x, y, x1, x2, y1, y2, f11, f12, f21, f22):
    """
    Interpolação bilinear
    """
    return (
        f11 * (x2 - x) * (y2 - y) +
        f21 * (x - x1) * (y2 - y) +
        f12 * (x2 - x) * (y - y1) +
        f22 * (x - x1) * (y - y1)
    ) / ((x2 - x1) * (y2 - y1))
