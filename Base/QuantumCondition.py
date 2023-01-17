###-------------------- 量子线路状态类 --------------------###
from Base.Gate import *
import numpy as np


class quantum_condition:

    ### 构造函数 ###
    def __init__(self, vec):
        self.vec = vec
        self.n = len(vec)
        self.n_qbit = int(np.log2(len(vec)))

    ### 重载复制构造函数 ###
    def __copy__(self):
        return quantum_condition(self.vec.copy())

    ### 用基态的方式输出向量代表的量子态 ###
    def state_output(self):
        num = len(self.vec)
        str_vec = []
        num_qbit = int(np.log2(num))
        moment = binary(np.zeros(num_qbit))
        for i in range(num):
            str_moment = "|"
            for j in range(num_qbit):
                str_moment = str_moment + str(int(moment.vec[j]))
                if j == num_qbit - 1:
                    str_moment = str_moment + ">"
            str_vec.append(str_moment)
            moment = moment + binary([1])
        str_moment = ""
        for i in range(num):
            if i == 0:
                str_moment = str_moment + str(self.vec[i]) + str_vec[i]
            else:
                str_moment = str_moment + "+" + str(self.vec[i]) + str_vec[i]
        return str_moment

    ### 判断量子态是否合法 ###
    def fit_judge(self):
        moment = 0
        for i in range(self.n):
            moment = np.pow(self.vec[i], 2)
        if moment == 1:
            return True
        else:
            return False

    ### 重载输出运算符 ###
    def __str__(self):
        return self.state_output()
