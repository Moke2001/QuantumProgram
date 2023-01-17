###-------------------- 分解双量子门的算法 --------------------###
from Base.QuantumGate import *


### 构造受控U门 ###
def create_CU(g,flag,U_0):
    c=0
    if g==1:
        c=2
    if g==2:
        c=1
    if flag==True:
        pin=1
    else:
        pin=0
    U=np.zeros((4,4),dtype='complex_')
    moment=binary(np.zeros(2))
    moment_0=binary(np.zeros(2))
    count=0
    for i in range(4):
        if moment.vec[c-1]==pin:
            for j in range(4):
                if j== moment.to_decimal():
                    U[j][i]=1
                else:
                    U[j][i]=0
        if moment.vec[c-1]==pin:
            for j in range(4):
                if moment_0.vec[c-1]==1 and moment_0.vec[g-1]==0:
                    U[j][i]=U_0[0][count]
                elif moment_0.vec[c-1]==1 and moment_0.vec[g-1]==1:
                    U[j][i] = U_0[1][count]
                else:
                    U[j][i]=0
                moment_0=moment_0+binary([1])
            count=count+1
        moment=moment+binary([1])
    return U


### 构造基态旋转门 ###
def create_U(v_1,v_2,U_0):

    ## 广义C-NOT门 ##
    A=CNOT
    B=X(2,1)@CNOT@X(2,1)
    C=H(2,1)@H(2,2)@CNOT@H(2,2)@H(2,1)
    D=X(2,2)@H(2,1)@H(2,2)@CNOT@H(2,2)@H(2,1)@X(2,2)

    c_1 = binary(v_1)
    c_2 = binary(v_2)
    gray=-1
    count=0
    U_vector=[]
    for i in range(c_1.n):
        if c_1.vec[i]!=c_2.vec[i]:
            c_2.vec[i]=c_1.vec[i]
            gray=i
            count=count+1
            if c_2.vec[i]==1:
                U_vector.append(A)
            else:
                U_vector.append(B)
    c_2.change(gray)
    if len(U_vector)>0:
        del U_vector[len(U_vector)-1]
    U_vector.append(create_CU(gray+1,False,U_0))
    flag=len(U_vector)-1
    U=np.zeros((len(U_vector[0]),len(U_vector[0])))
    for i in range(flag-1):
        U_vector.append(flag-i-1)
    for i in range(len(U_vector)):
        U[i][i]=1
    for i in range(len(U_vector)):
        if i==0:
            U=U_vector[i]
        else:
            U=U_vector[i]@U
    return [U_vector,U]


### 构造任意双量子门的分解 ###
def two_dimensions_decompose(U):
    q=quantum_gate(U)


### 主函数 ###
if __name__ == "__main__":
    U=RX(np.pi/3)
    [U_vector,U]=create_U([0,0],[0,1],U)
    U=quantum_gate(U)
    U.result_output()