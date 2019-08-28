from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
len = 10
xx, yy = np.meshgrid(range(len), range(len))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Equation of Plane is : n.T * x = c 

#defining planes
n1 = np.array([1,-2,1]).reshape((3,1))
c1 = 0


#corresponding z for planes
z1 = ((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])


P = np.array([-1,1,3]).reshape((3,1))
l1 = np.array([6,7,8]).reshape((3,1))

#generating points in Line 
l1_p = line_dir_pt(l1,P)

#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)


#plotting line
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line $L_1$")









Q = np.array([1,2,3]).reshape((3,1))
l2 = np.array([3,5,7]).reshape((3,1))

#generating points in Line 
l2_p = line_dir_pt(l2,Q)

#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)


#plotting line
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line $L_2$")




R = np.array([0,0,0]).reshape((3,1))
l3 = np.array([1,-2,1]).reshape((3,1))

#generating points in Line 
l3_p = line_dir_pt(l3,R)

#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)


#plotting line
plt.plot(l3_p[0,:],l3_p[1,:],l3_p[2,:],label="Line $L_3$")

B=np.array([1,-2,1])

ax.scatter(B[0],B[1],B[2],'o',label="Point B")

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
