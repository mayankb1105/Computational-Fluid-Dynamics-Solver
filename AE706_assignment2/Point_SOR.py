# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:04:21 2024

@author: MAYANK
"""

import numpy as np
def point_sor(T):
    beta=1.0
    a=np.power((np.cos(np.pi/40)+beta*beta*np.cos(np.pi/80))/(1+beta*beta),2)
    w=(2-2*np.sqrt(1-a))/a
    count=0
    iteration=[]
    err=[]
    while(True):
        T_cpy=T.copy()
        count+=1
        for i in range(1,80):
            for j in range(1,40):
                T[i][j]=((1-w)*T_cpy[i][j])+((w/(2*(1+np.power(beta,2))))*(T_cpy[i+1][j]+T[i-1][j]+beta*beta*T_cpy[i][j+1]+beta*beta*T[i][j-1]))
        error=T-T_cpy
        if(error.max()<0.001):
            break
        iteration.append(count)
        err.append(error.max())
    return count,iteration,err