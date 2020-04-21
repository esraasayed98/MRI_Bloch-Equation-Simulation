# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:58:54 2020

@author: ALIENWARE
"""

import prettytable
from prettytable import PrettyTable
import random
import matplotlib.pyplot as plt

random.seed(1)
NonUniform_B=[]
X=[]
for i in range(15):
    NonUniform_B.append(random.uniform(2.5 , 3.5))
    
    X.append((42.58*2*3.14)*NonUniform_B[i])
    i+=1
    
x = PrettyTable()
column_names = ["Angular_freq.( rad/sec)", "Magnetic Field(T)"]
x.add_column(column_names[0] , X)
x.add_column(column_names[1] , NonUniform_B)

print(x)

figure , axs = plt.subplots(3)


axs[0].set_xlim(2.5, 3.5)
axs[0].set_ylim(500,1200)
axs[0].plot(NonUniform_B , X , label='x_axis:Bz(T) & y_axis:F( rad/sec)')
axs[0].set_ylabel('angular_freq.( rad/sec)')
axs[0].set_xlabel('Bz(T)')
axs[0].legend(loc='upper center')

axs[1].set_ylim(0, 6)
axs[1].set_xlim(0,14)
axs[1].plot(NonUniform_B , label='x_axis:Z_axis & y_axis:Bz(T)')
axs[1].set_ylabel('Bz(T)')
axs[1].set_xlabel('z-axis')
axs[1].legend(loc='upper center')

axs[2].set_ylim(500, 1200)
axs[2].set_xlim(0,14)
axs[2].plot(X , label='x_axis:Z_axis & y_axis:F( rad/sec)')
axs[2].set_ylabel('angular_freq.( rad/sec)')
axs[2].set_xlabel('z-axis')
axs[2].legend(loc='upper center')





plt.show()