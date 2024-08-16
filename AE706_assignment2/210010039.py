# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:13:44 2024

@author: MAYANK
"""

import numpy as np
import matplotlib.pyplot as plt
import Point_Jacobi as PJ
import Point_Gauss_Siedel as PGS
import Point_SOR as PSOR
import Temp as Temp

#creating grid points and copy of Temperature with boundary conditions
x=np.linspace(0.0,1.0,41)
y=np.linspace(0.0,2.0,81)
T=np.zeros([81,41],dtype=float)
T[0]=250
T_PJ=T.copy()
T_PGS=T.copy()
T_PSOR=T.copy()

#Calling function to simulate Point Jacobi method
count_PJ,iteration_PJ,err_PJ=PJ.point_jacobi(T_PJ)
iter_PJ=np.array(iteration_PJ)
error_PJ=np.array(err_PJ)

#Calling function to simulate Point Gauss Seidel method
count_PGS,iteration_PGS,err_PGS=PGS.point_gauss_siedel(T_PGS)
iter_PGS=np.array(iteration_PGS)
error_PGS=np.array(err_PGS)

#Calling function to simulate Point Successive Over Relaxation method
count_PSOR,iteration_PSOR,err_PSOR=PSOR.point_sor(T_PSOR)
iter_PSOR=np.array(iteration_PSOR)
error_PSOR=np.array(err_PSOR)

#Printing the number of iterations each method takes
print("Number of iterations for convergence using Point Jacobi:", count_PJ)
print("Number of iterations for convergence using Point Gauss Seidel:", count_PGS)
print("Number of iterations for convergence using Point Successive Over Relaxation:", count_PSOR)

#Plot for error versus iterations on the log scale
plt.title('Error vs Iteration (in log scale)')
plt.yscale('log')
plt.xscale('log')
plt.plot(iter_PJ,error_PJ,label='Point Jacobi')
plt.plot(iter_PGS,error_PGS,label='Point Gauss Seidel')
plt.plot(iter_PSOR,error_PSOR,label='Point Successive Over Relaxation')
plt.xlabel('No.of iterations')
plt.ylabel('Error')
plt.grid()
plt.legend()
plt.show()

#Plotting x=0.5m midline temperature variation and its deviation from exact temperture
x_midline=Temp.T(0.5, y)
plt.title('Temperature comparison at x=0.5 midline')
plt.plot(y[2:81],x_midline[2:81],marker='o',label="Exact Solution")
plt.plot(y[2:81],T_PJ[2:81,20],marker='^',label="Point Jacobi")
plt.plot(y[2:81],T_PGS[2:81,20],marker='s',label="Point Gauss Seidel")
plt.plot(y[2:81],T_PSOR[2:81,20],marker='*',label="Point Sucessive Over Relaxation")
plt.grid()
plt.legend()
plt.xlabel('y variation')
plt.ylabel('Temperature in $^o$C')
plt.show()

plt.title('Temperature deviation from exact solution at x=0.5 midline')
plt.plot(y[2:81],T_PJ[2:81,20]-x_midline[2:81],marker='^',label="Point Jacobi")
plt.plot(y[2:81],T_PGS[2:81,20]-x_midline[2:81],marker='s',label="Point Gauss Seidel")
plt.plot(y[2:81],T_PSOR[2:81,20]-x_midline[2:81],marker='*',label="Point Sucessive Over Relaxation")
plt.grid()
plt.legend()
plt.xlabel('y variation')
plt.ylabel('Temperature deviation in $^o$C')
plt.show()

#Plotting y=1.0m midline temperature variation and its deviation from exact temperture
y_midline=Temp.T(x, 1.0)
plt.title('Temperature comparison at y=1.0 midline')
plt.plot(x,y_midline,marker='o',label="Exact Solution")
plt.plot(x,T_PJ[40,:],marker='^',label="Point Jacobi")
plt.plot(x,T_PGS[40,:],marker='s',label="Point Gauss Seidel")
plt.plot(x,T_PSOR[40,:],marker='*',label="Point Sucessive Over Relaxation")
plt.grid()
plt.legend()
plt.xlabel('x variation')
plt.ylabel('Temperature in $^o$C')
plt.show()

plt.title('Temperature deviation from exact solution at y=1.0 midline')
plt.plot(x,T_PJ[40,:]-y_midline,marker='^',label="Point Jacobi")
plt.plot(x,T_PGS[40,:]-y_midline,marker='s',label="Point Gauss Seidel")
plt.plot(x,T_PSOR[40,:]-y_midline,marker='*',label="Point Sucessive Over Relaxation")
plt.grid()
plt.legend()
plt.xlabel('x variation')
plt.ylabel('Temperature deviation in $^o$C')
plt.show()

#Making Contour plots for different temperature calculation methods
plt.title("Contour plot using Point Jacobi")
plt.contourf(x,y,T_PJ)
plt.colorbar(plt.contourf(x,y,T_PJ))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

plt.title("Contour plot using Point Gauss Seidel")
plt.contourf(x,y,T_PGS)
plt.colorbar(plt.contourf(x,y,T_PGS))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

plt.title("Contour plot using Point Successive Over Relaxation")
plt.contourf(x,y,T_PSOR)
plt.colorbar(plt.contourf(x,y,T_PSOR))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

T_exact=np.zeros([81,41])
for i in range(81):
    for j in range(41):
        T_exact[i][j]=Temp.T(x[j],y[i])
plt.title("Contour plot using Exact Solution")
plt.contourf(x,y,T_exact)
plt.colorbar(plt.contourf(x,y,T_exact))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()