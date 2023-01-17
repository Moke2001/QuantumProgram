###-------------------- 将一个低维度的门延拓到高维度上 --------------------###
from Binary import *


def dimension_change(U,  n, n_vector_in):
    n_0=int(np.log2(U.shape[0]))
    n_vector_out = []
    count = 0
    i = 1

    ## 寻找不在原始门上的比特 ##
    while 1:
        if n_vector_in[count] == i:
            if count != n_0 - 1:
                count = count + 1
        elif n_vector_in[count] > i and count != n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] > i and count == n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] < i and count == n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] < i and count != n_0 - 1:
            count = count + 1
            i=i-1
        i=i+1
        if count == n_0 - 1 and i == n+1:
            break

    ## 求高维度的门的形式 ##
    matrix = np.zeros((2 ** n, 2 ** n),dtype='complex_')
    core = binary(np.zeros(n))  # 总量子比特的状态
    kernel_out = binary(np.zeros(len(n_vector_out)))  # 不在原始门中量子比特的状态
    for w in range(2 ** n // 2 ** n_0):
        location = np.zeros(2 ** n_0)  # 计算一个系列各个所在的列
        moment = core.to_decimal()  # 计算一个系列两个列的间隔
        kernel_in = binary(np.zeros(len(n_vector_in)))  # 在原始门中量子比特的状态
        for j in range(2 ** n_0):
            location[j] = moment
            kernel_in = kernel_in + binary([1])
            core_moment = binary(core.vec.copy())
            for i in range(len(n_vector_in)):
                core.vec[n_vector_in[i] - 1] = kernel_in.vec[i]
            moment = moment + ((core - core_moment).to_decimal())
        for i in range(2 ** n_0):
            for j in range(2 ** n_0):
                matrix[int(location[i])][int(location[j])] = U[i][j]
        kernel_out = kernel_out + binary([1])
        for i in range(len(n_vector_out)):
            core.vec[n_vector_out[i] - 1] = kernel_out.vec[i]
    return matrix