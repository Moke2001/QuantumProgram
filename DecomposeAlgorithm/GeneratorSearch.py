###-------------------- 求一个矩阵的生成矩阵 --------------------###
from DecomposeAlgorithm.SingleBitDecompose import *
from Tool.Quaternion import *


def search_generator():
    X = np.array([[0, 1], [1, 0]])  # 泡利X门
    Y = np.array([[0, -1j], [1j, 0]])  # 泡利Y门
    Z = np.array([[1, 0], [0, -1]])  # 泡利Z门
    U = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    [alpha, beta, theta, delta] = decompose(U)
    q_1 = quaternion(np.cos(beta / 2), 0, 0, np.sin(beta / 2))
    q_2 = quaternion(np.cos(theta / 2), 0, np.sin(theta / 2), 0)
    q_3 = quaternion(np.cos(delta / 2), 0, 0, np.sin(delta / 2))
    q = q_1 * q_2
    q = q * q_3
    theta = 2 * np.arcsin(np.sqrt(q.x ** 2 + q.y ** 2 + q.z ** 2))
    C = q.x / np.sin(theta / 2) * X + q.y / np.sin(theta / 2) * Y + q.z / np.sin(theta / 2) * Z
    return [theta, C]
