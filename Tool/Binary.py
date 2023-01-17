###-------------------- 二进制类 --------------------###
import numpy as np


class binary:

    ### 构造函数 ###
    def __init__(self, vec):
        self.n = len(vec)
        self.vec = vec
        self.value=self.to_decimal()

    ### 重载加法运算符 ###
    def __add__(self, x):
        a = self.vec.copy()
        b = x.vec.copy()
        w = np.max([len(a), len(b)])
        result = []
        count = 0
        while w - len(a) > 0:
            a.insert(0, 0)
        while w - len(b) > 0:
            b.insert(0, 0)
        for i in range(w):
            moment = a[self.n - i - 1] + b[self.n - i - 1] + count
            if moment == 0:
                result.insert(0, 0)
                count = 0
            if moment == 1:
                result.insert(0, 1)
                count = 0
            elif moment == 2:
                result.insert(0, 0)
                count = 1
            elif moment == 3:
                result.insert(0, 1)
                count = 1
        return binary(result)

    ### 重载减法运算符 ###
    def __sub__(self, x):
        a = self.vec.copy()
        b = x.vec.copy()
        w = np.max([len(a), len(b)])
        result = []
        count = 0
        for i in range(w):
            moment = a[self.n - i - 1] - b[self.n - i - 1] - count
            if moment == 0:
                result.insert(0, 0)
                count = 0
            elif moment == 1:
                result.insert(0, 1)
                count = 0
            elif moment == -1:
                result.insert(0, 1)
                count = 1
            elif moment == -2:
                result.insert(0, 0)
                count = 1
        return binary(result)

    ### 改变某一位上的数 ###
    def change(self, n):
        if self.vec[n] == 1:
            self.vec[n] = 0
        else:
            self.vec[n] = 1

    ### 输出某一位上的数 ###
    def out(self, n):
        return self.vec[n]

    ### 二进制转十进制整数 ###
    def to_decimal(self):
        moment = 0
        for i in range(self.n):
            moment = moment + (2 ** i) * self.vec[self.n - i - 1]
        return moment
