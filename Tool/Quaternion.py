###-------------------- 四元数类 --------------------###
import numpy as np


class quaternion:

    ### 四元数类的构造函数 ###
    def __init__(self, s, x, y, z):
        self.s = s
        self.x = x
        self.y = y
        self.z = z
        self.vector = [x, y, z]
        self.all = [s, x, y, z]

    ### 重载输出运算符 ###
    def __str__(self):
        op = [" ", "i ", "j ", "k"]
        q = self.all.copy()
        result = ""
        for i in range(4):
            if q[i] < -1e-8 or q[i] > 1e-8:
                result = result + str(round(q[i], 4)) + op[i]
        if result == "":
            return "0"
        else:
            return result

    ### 重载加法运算符 ###
    def __add__(self, qu):
        q = self.all.copy()
        for i in range(4):
            q[i] += qu.all[i]
        return quaternion(q[0], q[1], q[2], q[3])

    ### 重载减法运算符 ###
    def __sub__(self, qu):
        q = self.all.copy()
        for i in range(4):
            q[i] -= qu.all[i]
        return quaternion(q[0], q[1], q[2], q[3])

    ### 重载乘法运算符 ###
    def __mul__(self, qu):
        q = self.all.copy()
        p = qu.all.copy()
        s = q[0] * p[0] - q[1] * p[1] - q[2] * p[2] - q[3] * p[3]
        x = q[1] * p[0] + q[0] * p[1] - q[3] * p[2] + q[2] * p[3]
        y = q[0] * p[2] - q[1] * p[3] + q[2] * p[0] + q[3] * p[1]
        z = q[0] * p[3] + q[1] * p[2] - q[2] * p[1] + q[3] * p[0]
        return quaternion(s, x, y, z)

    ### 右除运算 ###
    def divide(self, q):
        result = self * q.inverse()
        return result

    ### 求模的平方 ###
    def mod_pow(self):
        q = self.all
        return sum([i ** 2 for i in q])

    ### 求模 ###
    def mod(self):
        return np.pow(self.mod_pow(), 1 / 2)

    ### 求转置 ###
    def conj(self):
        q = self.all.copy()
        for i in range(1, 4):
            q[i] = -q[i]
        return quaternion(q[0], q[1], q[2], q[3])

    ### 求逆 ###
    def inverse(self):
        q = self.all.copy()
        mod = self.mod_pow()
        for i in range(4):
            q[i] /= mod
        return quaternion(q[0], -q[1], -q[2], -q[3])
