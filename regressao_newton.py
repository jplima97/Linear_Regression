import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import pylab 

sys.stdout = open("newton_regression.txt", "w")
   
# Reading data -----------------------------------------------------
data = pd.read_csv('FILE_NAME.csv')
print('This data has {} lines and {} columns.'.format(data.shape[0],data.shape[1]))

x = data['x'].values
f = data['f'].values
n = len(x)

# Newton’s Divided Difference Interpolation Formula -----------------
for i in range(n):
    a1 = f[0]
for i in range(n):
    a2 = (f[1]-f[0])/(x[1]-x[0])
for i in range(n):
    a3 = ((f[2]-f[1])/(x[2]-x[1])-a2)/(x[2]-x[0])
for i in range(n):
    a4 = (((f[3]-f[2])/(x[3]-x[2])-(f[2]-f[1])/(x[2]-x[1]))/(x[3]-x[1])
    - a3)/(x[3]-x[0])
for i in range(n):
    a5 = ((((f[4]-f[3])/(x[4]-x[3])-(f[3]-f[2])/(x[3]-x[2]))/(x[4]-x[2])
    - ((f[3]-f[2])/(x[3]-x[2])-(f[2]-f[1])/(x[2]-x[1]))/(x[3]-x[1]))/(x[4]-x[1])
    - a4)/(x[4]-x[0])

print('\nThe Coefficients are: a1={}, a2={}, a3={}, a4={}, a5={}\n'.format(a1,a2,a3,a4,a5))

# Considering a simple linear regression... ==========================
a6 = (f[4]-f[0])/(x[4]-x[0])
y1 = a1+a6*(x-x[0])
E = 0
for i in range(n):
    E = E + f[i]-(a6*x[i]+a1)
    erro = E**2
print('The global error for fitting the curve is: {}'.format(erro))
print('Linear adjustment values: {}'.format(y1))

# Considering Newton's interpolation formula ========================
y2 = a1+a2*(x-x[0])+a3*(x-x[0])*(x-x[1])+a4*(x-x[0])*(x-x[1])*(x-x[2])+a5*(x-x[0])*(x-x[1])*(x-x[2])*(x-x[3])
print('')
print('Newton adjustment values: {}'.format(y2))
E = 0
for i in range(n):
    E = E + f[i]-(a1+a2*(x[i]-x[0])+a3*(x[i]-x[0])*(x[i]-x[1])+a4*(x[i]-x[0])*(x[i]-x[1])*(x[i]-x[2])+a5*(x[i]-x[0])*(x[i]-x[1])*(x[i]-x[2])*(x[i]-x[3]))
    erro = E**2    
print('\nThe global error for fitting the curve is: {}'.format(erro))

plt.plot(x,y2,color='#FF0000',label='Regressão linear')
plt.scatter(x,y2,c='#808080',label='Dados')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('ajuste_newton.jpeg')
   