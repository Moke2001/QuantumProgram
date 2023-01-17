###-------------------- 量子门类 --------------------###
from QuantumCondition import *


class quantum_gate:

    ### 构造函数 ###
    def __init__(self, matrix):
        self.matrix = matrix  # 量子门的表示矩阵
        self.matrix_vector = None  # 量子门的分解方式
        self.n = matrix.shape[0]  # 量子门作用对象的基态个数
        self.n_qbit = int(np.log2(self.n))  # 量子门作用量子比特的个数

    ### 重载复制构造函数 ###
    def __copy__(self):
        return quantum_gate(self.matrix.copy())

    ### 重载量子门的乘法 ###
    def __mul__(self, other):
        if isinstance(other, quantum_gate):
            result = quantum_gate(self.matrix @ other.matrix)
        elif isinstance(other, quantum_condition):
            result = quantum_condition(self.matrix @ other.vec)
        else:
            result=False
        return result

    ### 将一个量子门扩展到高维度上 ###
    ## n表示扩展到几个量子比特上，n_vector表示量子门所在的量子位的序号（从0开始）
    def dimension_change(self, n, n_vector):
        n0 = self.n_qbit  # 原来有多少个量子位
        out_vector = []  # 不在原始门的量子位的序号
        ## 寻找不在原始门上的比特 ##
        for i in range(n):
            if i not in n_vector:
                out_vector.append(i)
        ## 求高维度的门的形式 ##
        matrix = np.zeros((2 ** n, 2 ** n), dtype='complex_')
        core = binary(np.zeros(n))  # 总量子比特的状态
        kernel_out = binary(np.zeros(len(out_vector)))  # 不在原始门中量子比特的状态
        for w in range(2 ** n // 2 ** n0):
            location = np.zeros(2 ** n0)  # 计算一个系列各个所在的列
            moment = core.to_decimal()  # 计算一个系列两个列的间隔
            kernel_in = binary(np.zeros(len(n_vector)))  # 在原始门中量子比特的状态
            for j in range(2 ** n0):
                location[j] = moment
                kernel_in = kernel_in + binary([1])
                core_moment = binary(core.vec.copy())
                for i in range(len(n_vector)):
                    core.vec[n_vector[i] - 1] = kernel_in.vec[i]
                moment = moment + ((core - core_moment).to_decimal())
            for i in range(2 ** n0):
                for j in range(2 ** n0):
                    matrix[int(location[i])][int(location[j])] = self.matrix[i][j]
            kernel_out = kernel_out + binary([1])
            for i in range(len(out_vector)):
                core.vec[out_vector[i] - 1] = kernel_out.vec[i]
        return matrix

    ### 输出量子门的作用效果 ###
    def result_output(self):
        moment = binary(np.zeros(self.n_qbit))
        str_vec = []
        for i in range(self.n):
            str_moment = "|"
            for j in range(self.n_qbit):
                str_moment = str_moment + str(int(moment.vec[j]))
                if j == self.n_qbit - 1:
                    str_moment = str_moment + ">"
            str_vec.append(str_moment)
            moment = moment + binary([1])
        result = []
        for i in range(self.n):
            str_moment = str_vec[i] + "→"
            for j in range(self.n):
                if j == 0:
                    str_moment = str_moment + str(self.matrix[j][i]) + str_vec[j]
                else:
                    str_moment = str_moment + "+" + str(self.matrix[j][i]) + str_vec[j]
            result.append(str_moment)
        return result

    ### 重载输出函数 ###
    def __str__(self):
        return self.result_output()
