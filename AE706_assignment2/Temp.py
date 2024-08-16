# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:37:39 2024

@author: MAYANK
"""

import numpy as np

def T(x,y):
    value=0
    for n in range(1,61):
        value+=500.0*(((1-np.power(-1,n))/(n*np.pi))*((np.sinh((n*np.pi*(2.0-y))/1.0)*np.sin((n*np.pi*x)/1.0))/np.sinh(n*np.pi*2.0/1.0)))
    return value