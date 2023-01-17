###-------------------- 对酉矩阵进行分解 --------------------###
import numpy as np


def decompose(U):
    a = U(1, 1)
    c = U(2, 1)
    #a1 = np.real(U[0][0])
    a2 = np.imag(U[0][0])
    #b1 = np.real(U[0][1])
    b2 = np.imag(U[0][1])
    #c1 = np.real(U[1][0])
    c2 = np.imag(U[1][0])
    #d1 = np.real(U[1][1])
    d2 = np.imag(U[1][1])
    if a == 0:
        theta = 0
        delta = (np.arcsin(c2) - np.arcsin(b2)) / 2
        alpha = 0
        beta = (-np.arcsin(c2) - np.arcsin(b2)) / 2
    elif c == 0:
        theta = np.pi
        delta = (np.arcsin(a2) + np.arcsin(d2)) / 2
        alpha = 0
        beta = np.arcsin(d2) - np.arcsin(a2)
    else:
        theta = 2 * np.arctan(np.abs(a) / np.abs(c))
        alpha = np.arcsin(c2) - np.arcsin(a2)
        beta = np.arcsin(b2) - np.arcsin(a2) - np.pi
        delta = 0.5 * (-np.arcsin(b2) + np.arcsin(c2) - np.pi)
    return [alpha, beta, theta, delta]
