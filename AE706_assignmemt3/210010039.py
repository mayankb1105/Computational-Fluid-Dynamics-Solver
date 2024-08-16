# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:28:51 2024

@author: MAYANK
"""
#importing required packages
import numpy as np
import matplotlib.pyplot as plt
import FTCS_main as ftc
import CN_main as CN
import Exact

#initializing required constants
alpha= 2.6e-6
delta_x=0.02
delta_t=60 #for stable results it needs to be less than 78.9 sec so we take 1 minute
delta_t2=90

#Making required arrays and initializing the Temperature with intial conditions
x=np.linspace(0,1,51)
t=np.linspace(30,1800,60)
T=np.zeros((int(1800/delta_t) + 1,51))
for i in range(int(1800/delta_t) + 1):
    for j in range(51):
        if j==0 or j==50:
            T[i][j]=200
        else:
            T[i][j]=40

#Calling function that computes the equation usng FTCS method
T_FTCS=T.copy()
ftc.FTCS(delta_x, delta_t, alpha, T_FTCS)

#Calling the function that computes the equation using Crank-Nicolson method
T_CN=T.copy()
CN.crank_nicolson(delta_x, delta_t, alpha, T_CN)

#Recalling FTCS method function with an unstable delta t to verify the stability condition
T_FTCS_unstable=T.copy()
ftc.FTCS(delta_x, delta_t2, alpha, T_FTCS_unstable)

#Calling the function that gives exact solution
T_exact=Exact.exact(alpha,delta_t)

#Caculating the error matrix using the exact solution and the solutions obtained using the two methods
error_FTCS=(T_FTCS-T_exact)*100/T_exact
error_CN=(T_CN-T_exact)*100/T_exact

#PLOTS
plt.plot(x,T_FTCS[int(360/delta_t)],label="FTCS")
plt.plot(x,T_CN[int(360/delta_t)],label="Crank-Nicolson")
plt.plot(x,T_exact[int(360/delta_t)],label="Exact")
plt.xlabel("X (in m)")
plt.ylabel("Temperature (in degree Celcius)")
plt.title("Temperature at time 0.1 hr")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,T_FTCS[int(1080/delta_t)],label="FTCS")
plt.plot(x,T_CN[int(1080/delta_t)],label="Crank-Nicolson")
plt.plot(x,T_exact[int(1080/delta_t)],label="Exact")
plt.xlabel("X (in m)")
plt.ylabel("Temperature (in degree Celcius)")
plt.title("Temperature at time 0.3 hr")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,T_FTCS[int(1800/delta_t)],label="FTCS")
plt.plot(x,T_CN[int(1800/delta_t)],label="Crank-Nicolson")
plt.plot(x,T_exact[int(1800/delta_t)],label="Exact")
plt.xlabel("X (in m)")
plt.ylabel("Temperature (in degree Celcius)")
plt.title("Temperature at time 0.5 hr")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,T_FTCS_unstable[int(360/delta_t)],label="0.1 hr")
plt.plot(x,T_FTCS_unstable[int(1080/delta_t)],label="0.3 hr")
plt.plot(x,T_FTCS_unstable[int(1800/delta_t)],label="0.5 hr")
plt.xlabel("X (in m)")
plt.ylabel("Temperature (in degree Celcius)")
plt.title("Temperature using FTCS with unstable time step")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,error_FTCS[int(360/delta_t)],label="FTCS")
plt.plot(x,error_CN[int(360/delta_t)],label="Crank-Nicolson")
plt.xlabel("X (in m)")
plt.ylabel("Error Percentage (%)")
plt.title("Error at time 0.1 hr")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,error_FTCS[int(1080/delta_t)],label="FTCS")
plt.plot(x,error_CN[int(1080/delta_t)],label="Crank-Nicolson")
plt.xlabel("X (in m)")
plt.ylabel("Error Percentage (%)")
plt.title("Error at time 0.3 hr")
plt.grid()
plt.legend()
plt.show()

plt.plot(x,error_FTCS[int(1800/delta_t)],label="FTCS")
plt.plot(x,error_CN[int(1800/delta_t)],label="Crank-Nicolson")
plt.xlabel("X (in m)")
plt.ylabel("Error Percentage (%)")
plt.title("Error at time 0.5 hr")
plt.grid()
plt.legend()
plt.show()