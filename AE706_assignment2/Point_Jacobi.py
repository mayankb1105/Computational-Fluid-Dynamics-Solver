# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:19:09 2024

@author: MAYANK
"""

import numpy as np
def point_jacobi(T):
    beta=1.0
    count=0
    iteration=[]
    err=[]
    while(True):
        T_cpy=T.copy()
        count+=1
        for i in range(1,80):
            for j in range(1,40):
                T[i][j]=(1/(2*(1+np.power(beta,2))))*(T_cpy[i+1][j]+T_cpy[i-1][j]+beta*beta*T_cpy[i][j+1]+beta*beta*T_cpy[i][j-1])
        error=T-T_cpy
        if(error.max()<0.001):
            break
        iteration.append(count)
        err.append(error.max())
    return count,iteration,err