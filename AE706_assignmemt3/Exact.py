# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:42:08 2024

@author: MAYANK
"""

import numpy as np

def exact(alpha,delta_t):
    Ti=40
    Ts=200
    
    T=np.zeros((int(1800/delta_t) + 1,51))
    for i in range(int(1800/delta_t) + 1):
        for j in range(51):
            if j==0 or j==50:
                T[i][j]=Ts
            else:
                T[i][j]=Ti
               
    for i in range(1,int(1800/delta_t) + 1):
        for j in range(1,50):
            x=0
            for m in range(1,71):
                x=x+(np.exp(-m*m*np.pi*np.pi*alpha*i*delta_t)*((1-np.power(-1,m))/(m*np.pi))*np.sin(np.pi*m*0.02*j))
            T[i][j]=Ts + 2*(Ti-Ts)*x
        
    return T