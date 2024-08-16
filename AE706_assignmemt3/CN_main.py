# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:10:49 2024

@author: MAYANK
"""

import numpy as np

def crank_nicolson(delta_x,delta_t,alpha,T):
    b=(alpha*delta_t)/(2*delta_x*delta_x)
    A=np.zeros((49,49))
    d=np.zeros(49)
    for n in range(int(1800/delta_t)):
        for i in range(49):
            if i==0:
                d[i]=(1-2*b)*T[n][i+1]+b*T[n][i+2]+400*b
            elif i==48:
                d[i]=b*T[n][48]+(1-2*b)*T[n][49]+400*b
            else:
                d[i]=b*T[n][i]+(1-2*b)*T[n][i+1]+b*T[n][i+2]
        for i in range(49):
            if i==0:
                A[0][0]=1+2*b
                A[0][1]=-b
            elif i==48:
                A[i][i]=1+2*b
                A[i][i-1]=-b
            else:
               A[i][i]=1+2*b
               A[i][i-1]=-b
               A[i][i+1]=-b
        x=np.linalg.solve(A,d)
        T[n+1]=np.append(np.append(np.array([200]),x),np.array([200]))
        

