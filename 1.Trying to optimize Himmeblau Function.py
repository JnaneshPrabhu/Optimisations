## Trying to optimize Himmeblau Function using Simulated Annealing
# Equation: = f(x,y) = (x**2 + y -11)**2 + (x + y**2 -7)**2
# This has got 4 solutions, lets see which one we get???


import numpy as np 
import matplotlib.pyplot as plt 


x0 , y0 = 10, -100 # initializing with 0s

k = 0.1 # distance factor to nearest neighbor
T0 = 1000 #intial temperature
alpha = 0.85 # cool down factor
M = 300 # number of iterations in search space
N = 20  # number of neighbors to check

def Himmeblau(x0,y0):
    return ((x0**2) + y0 - 11)**2 + (x0 + (y0**2) - 7)**2

f = Himmeblau(x0,y0) ##Himelblau function

print('Initial values of x:',x0, 'y: ',y0, 'OF: ', f)

temp = []
min_f = []

for i in range(M):
    for j in range(N):
        xt,yt = 0,0
        ran_x_1 = np.random.rand()
        ran_x_2 = np.random.rand()
        ran_y_1 = np.random.rand()
        ran_y_2 = np.random.rand()

        print(ran_x_1,ran_y_1)
        print(ran_x_2,ran_y_2)


        if ran_x_1 > 0.5:
            x1 = k*ran_x_2
        else:
            x1 = -k * ran_x_2

        if ran_y_1 > 0.5:
            y1 = k*ran_y_2
        else:
            y1 = -k * ran_y_2

        xt = x0 + x1
        yt = y0 + y1

        f_new = Himmeblau(xt,yt)
        f_orig = Himmeblau(x0,y0)

        ran = np.random.rand()
        form = 1/(np.exp((f_new-f_orig)/T0))

        if f_new <= f_orig or ran <= form:
            x0,y0 = xt,yt
        
    temp.append(T0)
    min_f.append(f_orig)
    T0 *= alpha


print('x: ',x0, 'y: ', y0, 'OF: ',f_orig)

plt.plot(temp,min_f)
plt.title('Himmelblau function OF vs Temperature T',  fontweight = 'bold')
plt.xlabel('Temperature', fontsize=18, fontweight = 'bold')
plt.ylabel('OF', fontsize=18, fontweight = 'bold')
plt.xlim(1000,0)
plt.xticks(np.arange(min(temp),min(min_f),100), fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.show()














