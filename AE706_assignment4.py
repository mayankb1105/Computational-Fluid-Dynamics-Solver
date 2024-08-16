# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:47:32 2024

@author: MAYANK
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Intialising all the matrices(Pressure, Temperature, Velocity) with give intial conditons
mu=0.2
time=0
X=np.linspace(-0.005,1.005,203)
T=300.0*np.ones((203))
u=np.zeros((203))
P=np.zeros((203))
for i in range(203):
    if(X[i]<0.5):
        P[i]=5*101325
    else:
        P[i]=1*101325

rho=P/(287.0*T)

U=np.zeros((3,203))
U[0]=rho
U[1]=rho*u
U[2]=(P/0.4)+(0.5*rho*u*u)

F=np.zeros((3,203))
F[0]=rho*u
F[1]=rho*u*u+P
F[2]=((P/0.4)+(0.5*rho*u*u)+P)*u

F_plus=np.zeros((3,203))
F_neg=np.zeros((3,203))
a=np.sqrt(1.4*287*T)
Mach_number=u/a

#Running the loop where calcultion takes place and breaking out only after total time reaches 0.75x10e-3s
while(True):
#for k in range(4000):
    for i in range(203):
        #Defining flux vector depending on mach number (using Van-Leer flux splitting method)
        if(Mach_number[i]<=-1):
            F_plus[0][i]=0
            F_plus[1][i]=0
            F_plus[2][i]=0
            F_neg[0][i]=F[0][i]
            F_neg[1][i]=F[1][i]
            F_neg[1][i]=F[2][i]
        elif(Mach_number[i]>=1):
            F_neg[0][i]=0
            F_neg[1][i]=0
            F_neg[2][i]=0
            F_plus[0][i]=F[0][i]
            F_plus[1][i]=F[1][i]
            F_plus[2][i]=F[2][i]
        else:
            F_plus[0][i]=0.25*rho[i]*a[i]*(Mach_number[i]+1)*(Mach_number[i]+1)
            F_plus[1][i]=F_plus[0][i]*(2/1.4)*a[i]*(1+0.2*Mach_number[i])
            F_plus[2][i]=F_plus[0][i]*(2/0.96)*a[i]*a[i]*(1+0.2*Mach_number[i])*(1+0.2*Mach_number[i])
            F_neg[0][i]=F[0][i]-F_plus[0][i]
            F_neg[1][i]=F[1][i]-F_plus[1][i]
            F_neg[2][i]=F[2][i]-F_plus[2][i]
    
    #Finding the delta T for given conditions and then proceeding for numerical solution
    lamda=np.max(np.abs(u[1:202])+a[1:202])
    del_t=0.005*mu/lamda
    
    #numerical calculation for one time step
    for j in range(3):
        for i in range(1,202):
            U[j][i]=U[j][i]-((del_t/0.005)*(F_plus[j][i]-F_plus[j][i-1]))-((del_t/0.005)*(F_neg[j][i+1]-F_neg[j][i]))
    
    #Calculating updated parameters from updated matrices
    rho=U[0]
    u=U[1]/rho
    P=(U[2]-(0.5*rho*u*u))*0.4
    T=P/(rho*287)
        
    #Applying boundary condition after each time step
    rho[0]=rho[1]
    P[0]=P[1]
    T[0]=T[1]
    u[0]=u[1]
        
    rho[202]=rho[201]
    P[202]=P[201]
    T[202]=T[201]
    u[202]=u[201]
    
    #Updating the Flux vector
    F[0]=rho*u
    F[1]=rho*u*u+P
    F[2]=((P/0.4)+(0.5*rho*u*u)+P)*u
    
    a=np.sqrt(1.4*287*T)
    Mach_number=u/a
    
    #Updating total time to check for breaking condition
    time+=del_t
    if(time>0.00075):
        break

theory_data=pd.read_csv('exact_solution_shock_tube.csv',skiprows=1)

#Plotting all the required properties along with its exact soultion
plt.plot(X,T,label='VFS solution')
plt.plot(theory_data['x'],theory_data['T'],'--',label='Exact Solution')
plt.title("Temperature vs X")
plt.xlabel("X in m")
plt.ylabel("Temperature in K")
plt.grid()
plt.legend()
plt.show()
plt.plot(X,P/101325,label='VFS solution')
plt.plot(theory_data['x'],theory_data['P']/101325,'--',label='Exact Solution')
plt.title("Pressure vs X")
plt.xlabel("X in m")
plt.ylabel("Pressure in atm")
plt.grid()
plt.legend()
plt.show()
plt.plot(X,u,label='VFS solution')
plt.plot(theory_data['x'],theory_data['u'],'--',label='Exact Solution')
plt.title("Velocity vs X")
plt.xlabel("X in m")
plt.ylabel("Velocity in m/s")
plt.grid()
plt.legend()
plt.show()
plt.plot(X,Mach_number,label='VFS solution')
plt.plot(theory_data['x'],theory_data['u']/np.sqrt(1.4*theory_data['P']/theory_data['rho']),'--',label='Exact Solution')
plt.title("Mach Number vs X")
plt.xlabel("X in m")
plt.ylabel("Mach Number")
plt.grid()
plt.legend()
plt.show()