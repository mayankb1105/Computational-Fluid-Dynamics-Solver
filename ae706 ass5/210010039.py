# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:22:02 2024

@author: MAYANK
"""
import numpy as np
import matplotlib.pyplot as plt
import main3 as calc

zeta=np.linspace(0,1,101)
eta=np.linspace(0,1,26)

x=np.zeros((26,101))
y=np.zeros((26,101))
for i in range(26):
    x[i]=np.linspace(0,4,101)
for i in range(101):
    if ((x[0][i]<1) or (x[0][i]>3)):
        y[0][i]=0
    else:
        y[0][i]=(1-np.cos((x[0][i]-1)*np.pi))/10
    y[:,i]=np.linspace(y[0][i],1,26)

zeta_dx=np.zeros((26,101))
zeta_dy=np.zeros((26,101))
eta_dx=np.zeros((26,101))
eta_dy=np.zeros((26,101))
zeta_dx2=np.zeros((26,101))
zeta_dy2=np.zeros((26,101))
eta_dx2=np.zeros((26,101))
eta_dy2=np.zeros((26,101))
a=np.zeros((26,101))
b=np.zeros((26,101))
c=np.zeros((26,101))
d=np.zeros((26,101))
e=np.zeros((26,101))

for i in range(len(eta)):
    for j in range(len(zeta)):
        if(zeta[j]<0.25 or zeta[j]>0.75):
            zeta_dx[i][j]=0.25
            zeta_dy[i][j]=0
            eta_dx[i][j]=0
            eta_dy[i][j]=1
            zeta_dx2[i][j]=0
            zeta_dy2[i][j]=0
            eta_dx2[i][j]=0
            eta_dy2[i][j]=0
        else:
            zeta_dx[i][j]=0.25
            zeta_dy[i][j]=0
            eta_dx[i][j]=(np.pi*np.sin((x[i][j]-1)*np.pi)/10)*(y[i][j]-1)/((1-y[0][j])**2)
            eta_dy[i][j]=1/(1-y[0][j])
            zeta_dx2[i][j]=0
            zeta_dy2[i][j]=0
            eta_dx2[i][j]=(np.pi*np.pi*(y[i][j]-1)/100)*(9*np.cos((x[i][j]-1)*np.pi)+7*np.cos((x[i][j]-1)*np.pi)*np.cos((x[i][j]-1)*np.pi)+2)/((1-y[0][j])**3)
            eta_dy2[i][j]=0
            
        a[i][j]=zeta_dx[i][j]**2+zeta_dy[i][j]**2
        b[i][j]=eta_dx[i][j]**2+eta_dy[i][j]**2
        c[i][j]=zeta_dx[i][j]*eta_dy[i][j]+zeta_dy[i][j]*eta_dx[i][j]
        d[i][j]=zeta_dx2[i][j]+zeta_dy2[i][j]
        e[i][j]=eta_dx2[i][j]+eta_dy2[i][j]


stream_func_comp=np.zeros((26,101))
stream_func_comp[0]=0
stream_func_comp[25]=100
stream_func_comp[:,0]=np.linspace(0,100,26)
stream_func_comp[:,100]=np.linspace(0,100,26)

ERROR=[]
iterations=0
while(True):
    stream_og=stream_func_comp.copy()
    calc.calculate(a, b, c, d, e, stream_func_comp, 0.01 , 0.04)
    error=stream_func_comp-stream_og
    err=np.sum(np.abs(error))
    ERROR.append(err)
    iterations+=1
    if(err<1e-4):
        break

print("Number of iterations for convergence",iterations)

x_vel=np.zeros((24,99))
y_vel=np.zeros((24,99))

for i in range(24):
    for j in range(99):
        y_vel[i][j]=-(stream_func_comp[i+1][j+2]-stream_func_comp[i+1][j])*zeta_dx[i][j]/(zeta[j+2]-zeta[j])
        x_vel[i][j]=(stream_func_comp[i+2][j+1]-stream_func_comp[i][j+1])*eta_dy[i][j]/(eta[i+2]-eta[i])

total_vel=np.sqrt(x_vel**2+y_vel**2)

plt.contourf(x,y,stream_func_comp,100)
plt.colorbar()
plt.title("Contour map of stream function")
plt.show()
plt.contourf(x[1:25,1:100],y[1:25,1:100],x_vel,100)
plt.colorbar()
plt.title("Contour map of x component of velocity")
plt.show()
plt.contourf(x[1:25,1:100],y[1:25,1:100],y_vel,100)
plt.colorbar()
plt.title("Contour map of y component of velocity")
plt.show()
plt.contourf(x[1:25,1:100],y[1:25,1:100],total_vel,100)
plt.colorbar()
plt.title("Contour map of total velocity")
plt.show()
plt.plot(y[:,13],stream_func_comp[:,13],label='x=0.5')
plt.plot(y[:,25],stream_func_comp[:,25],label='x=1.0')
plt.plot(y[:,50],stream_func_comp[:,50],label='x=2.0')
plt.plot(y[:,75],stream_func_comp[:,75],label='x=3.0')
plt.plot(y[:,87],stream_func_comp[:,87],label='x=3.5')
plt.title("Variation of stream function along vertical lines")
plt.xlabel("y")
plt.ylabel("Stream function value")
plt.legend()
plt.show()
plt.plot(y[1:25,13],x_vel[:,13],label='x=0.5')
plt.plot(y[1:25,25],x_vel[:,25],label='x=0.5')
plt.plot(y[1:25,50],x_vel[:,50],label='x=0.5')
plt.plot(y[1:25,75],x_vel[:,75],label='x=0.5')
plt.plot(y[1:25,87],x_vel[:,87],label='x=0.5')
plt.title("Variation of x component of velocity along vertical lines")
plt.xlabel("y")
plt.ylabel("x component of velocity")
plt.legend()
plt.show()
plt.plot(y[1:25,13],y_vel[:,13],label='x=0.5')
plt.plot(y[1:25,25],y_vel[:,25],label='x=1.0')
plt.plot(y[1:25,50],y_vel[:,50],label='x=2.0')
plt.plot(y[1:25,75],y_vel[:,75],label='x=3.0')
plt.plot(y[1:25,87],y_vel[:,87],label='x=3.5')
plt.title("Variation of y component of velocity along vertical lines")
plt.xlabel("y")
plt.ylabel("y component of velocity")
plt.legend()
plt.show()
plt.plot(y[1:25,13],total_vel[:,13],label='x=0.5')
plt.plot(y[1:25,25],total_vel[:,25],label='x=1.0')
plt.plot(y[1:25,50],total_vel[:,50],label='x=2.0')
plt.plot(y[1:25,75],total_vel[:,75],label='x=3.0')
plt.plot(y[1:25,87],total_vel[:,87],label='x=3.5')
plt.title("Variation of total velocity along vertical lines")
plt.xlabel("y")
plt.ylabel("Total Velocity")
plt.legend()
plt.show()
plt.plot(np.linspace(1,iterations,iterations),np.array(ERROR))
plt.yscale('log')
plt.title("log(ERROR) vs iterations")
plt.xlabel("iterations")
plt.ylabel("log(ERROR)")
plt.show()



