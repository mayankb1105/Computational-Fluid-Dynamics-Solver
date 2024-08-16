# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:39:06 2024

@author: MAYANK
"""

def calculate(a,b,c,d,e,psi,del_zeta,del_eta):
    for i in range(1,25):
        for j in range(1,100):
            psi[i][j]=((psi[i][j+1]+psi[i][j-1])*a[i][j]/((del_zeta)**2))+((psi[i+1][j]+psi[i-1][j])*b[i][j]/((del_eta)**2))+((psi[i+1][j+1]-psi[i-1][j+1]-psi[i+1][j-1]+psi[i-1][j-1])*c[i][j]/(2*del_zeta*del_eta))+((psi[i][j+1]-psi[i][j-1])*d[i][j]/(2*del_zeta))+((psi[i+1][j]-psi[i-1][j])*e[i][j]/(2*del_eta))
            psi[i][j]=psi[i][j]/((2*a[i][j]/(del_zeta**2))+(2*b[i][j]/(del_eta**2)))