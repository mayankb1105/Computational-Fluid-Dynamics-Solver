# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:20:16 2024

@author: MAYANK
"""

import numpy as np
import matplotlib.pyplot as plt

w=[332.0,276.0,245.0,214.0,188.0]
OD=61.0
d0=20.0
mox=40.0
l=120.0

rho=4*w[0]/(np.pi*(OD*OD-d0*d0)*l)

di=d0
r_dot=np.zeros((4))
G_ox=np.zeros((4))
for i in range(4):
    df=np.sqrt((4*(w[i]-w[i+1])/(np.pi*rho*l))+di**2)
    print(df)
    r_dot[i]=(df-di)/2
    G_ox[i]=1600*mox/(np.pi*(df+di)**2)
    di=df

coeff=np.polyfit(np.log(G_ox),np.log(r_dot),1)
m=coeff[0]
c=coeff[1]
x=np.exp(c)
G_ox_theory=np.linspace(2, 10,100)
r_dot_theory=np.power(G_ox_theory,m)*x

print('a value is ',x)
print('n value is ',m )
plt.xscale('log')
plt.yscale('log')
plt.plot(G_ox,r_dot,'-o', label='Experimental')
plt.plot(G_ox_theory,r_dot_theory,'--', label='Regression model with a=0.383, n=1.271')
plt.title("Regression rate vs Mass flux of oxidiser")
plt.xlabel('$G_{ox}$ in $\\frac{g}{cm^2s}$')
plt.ylabel('$\\.r$ in mm/s')
plt.grid()
plt.legend()
plt.show()