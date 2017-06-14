from math import *
import numpy as np
np.seterr(all='ignore');


def my_sin_approx(x):
    x = np.float64(x)

    exact = sin(x)
    approx = x - (x ** 3) / factorial(3) + (x ** 5) / factorial(5) - (x ** 7) / factorial(7)
    actual_error = approx - exact
    relative_error = (actual_error / exact)

    return (exact, approx, actual_error, relative_error)


def my_collision(m, v_initial, theta_cue, theta_eight):
    theta1 = theta_cue * pi / 180
    theta2 = theta_eight * pi / 180

    v_eight = (v_initial) / (cos(theta2) + (sin(theta2) / sin(theta1) * cos(theta1)))
    v_cue = v_eight * sin(theta2) / sin(theta1)
    e_lost = (m / 2) * (v_initial ** 2 - v_cue ** 2 - v_eight ** 2)

    return (v_cue, v_eight, e_lost)


def my_projectile(v0, theta, t):
    g = -9.81

    theta = theta * pi / 180
    v0x = v0 * cos(theta)
    v0y = v0 * sin(theta)
    ax = 0
    a = sqrt(ax ** 2 + g ** 2)
    vx = v0 * cos(theta)
    vy = (v0 * sin(theta)) + g * t
    v = sqrt(vx ** 2 + vy ** 2)
    x = v0 * cos(theta) * t
    y = v0 * sin(theta) * t + (g * (t ** 2) / 2)
    d = sqrt(x ** 2 + y ** 2)
    tf = 2 * v0 * sin(theta) / g
    h = ((v0 * sin(theta)) ** 2) / (2 * (-g))

    return (v0x, v0y, ax, g, a, vx, vy, v, x, y, d, tf, h)


def my_projection(x, y):
    p = (np.dot(x, y) / np.dot(x, x) * x)

    return p


def my_array_metrics_num(arr):
    n_positive = sum(sum(arr > 0))

    n_negative = sum(sum(arr < 0))

    n_zero = sum(sum(arr == 0))

    int1 = np.isnan(arr);
    intNaN = sum(int1);
    int2 = np.isinf(arr);
    intinf = sum(int2);
    n_special = sum(intNaN) + sum(intinf)

    return (n_positive, n_negative, n_zero, n_special)


def my_array_metrics_lgcl(arr):
    positive = np.sum(arr > 0).any()
    negative = np.sum(arr < 0).any()
    zero = np.sum((arr == 0)).any()
    special = np.sum(np.isinf(arr)).any() | np.sum(np.isnan(arr)).any()

    return [positive, negative, zero, special]


def my_polygon_perimeter(x, y):
    len_x = len(x)

    if (len_x < 3):
        perimeter = 0
    else:
        lengthnorm = 0
        for i in range(1, len_x):
            lengthnorm += sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)
        lengthextra = sqrt((x[0] - x[len_x - 1]) ** 2 + (y[0] - y[len_x - 1]) ** 2)

        perimeter = lengthnorm + lengthextra
    return perimeter

