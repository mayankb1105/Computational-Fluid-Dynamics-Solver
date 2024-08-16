# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:33:55 2024

@author: MAYANK
"""

import numpy as np

def FTCS(delta_x,delta_t,alpha,T):
    a=(alpha*delta_t)/(delta_x*delta_x)
    for n in range(int(1800/delta_t)):
        for i in range(49):
            T[n+1][i+1]=T[n][i+1] + a*(T[n][i+2]-2*T[n][i+1]+T[n][i])
