import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
print(os.getcwd())
dist = pd.read_excel( 'Combinatorial_Data_Simulated_Annealing.xlsx', sheet_name= 'Dlist',index_col=0)
flow = pd.read_excel('Combinatorial_Data_Simulated_Annealing.xlsx', sheet_name='Flow',index_col = 0)

print('-------- Flow Dataframe ---------')

print('\n')

print(flow)


print('------- Original Combination ----')
print(dist)
print(dist.index)

T0 = 1000 #Initial Temperature
M = 300 #Number of times search should happen
N = 15 #Number of neighbors to search in each iteration
alpha = 0.85 #Cool down factor

X0 = ['B','A','E','C','F','H','G','D']

print('\n')
new_dist =  dist.reindex(columns = X0, index=X0)
new_arr = np.array(new_dist)
print('------ New combination -------')
print(new_dist)


# Creating a cost function
'''
Cost  = Flow * Distance

'''
cost_start = pd.DataFrame(new_arr * flow)

print('Cost Matrix Start')
print(cost_start)






