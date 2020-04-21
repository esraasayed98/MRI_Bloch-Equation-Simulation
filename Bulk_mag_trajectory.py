import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

import imageio

fig =plt.figure(figsize=(10,10))
ax=fig.gca(projection='3d')


images=[] 
random.seed(1)
NonUniform_B=[]
X=[]
for i in range(15):
    NonUniform_B.append(random.uniform(2.5 , 3.5))
    
    X.append((42.58*2*3.14)*NonUniform_B[i])
    i+=1



def vector_processing(t,t1,t2,f):
   phi = f
   a=[[np.exp(-t/t2), 0, 0],[0 ,np.exp(-t/t2), 0],[ 0, 0, np.exp(-t/t1)]]
   B=[0,0,1-np.exp(-t/t1)]
   A=np.dot(a,zrot(phi))
   return (A,B)


def zrot(theta):
    Rz = [[np.cos(theta),-np.sin(theta), 0],[np.sin(theta),np.cos(theta),0],[0,0,1]]
    return(Rz)

def vector(a,b):
    M=np.empty((n,3))
    
    M[0,:]=np.array([1,0,0])
    for i in range(n-1):
        M[i+1,:]=np.dot(a,M[i,:])+b
    return (M[:,0],M[:,1])

xdata1=[[],[],[]]
ydata1=[[],[],[]]


n=100

zp=np.arange(100)
for i in range (3):
     a,b = vector_processing(1,600,100,X[i+2])
     
     xdata1[i],ydata1[i]=vector(a,b)
    
plotting1x=[]
plotting1y=[]

plotting2x=[]
plotting2y=[]

plotting3x=[]
plotting3y=[]
    
for i in range (100):
    
    plotting1x.append(xdata1[0][i])
    plotting1y.append(ydata1[0][i])
    
    plotting2x.append(xdata1[1][i])
    plotting2y.append(ydata1[1][i])
    
    plotting3x.append(xdata1[2][i])
    plotting3y.append(ydata1[2][i])
    
    ax.plot(plotting1x,plotting1y,zp[:i+1],'red')
    ax.plot(plotting2x,plotting2y,zp[:i+1],'green')
    ax.plot(plotting3x,plotting3y,zp[:i+1],'blue')
    pyplot.savefig('temp_file.png') 
    images.append(imageio.imread('temp_file.png'))
imageio.mimsave('bulk_mag_trajectory.gif', images, duration=0.1)
    





