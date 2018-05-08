#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			26-02-2017
# Purpose:     comparison between python and R :: surface plot
# Source:       python
#####################################################################

import numpy as np
import pylab as pyl

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


#--- generate mesh ---#
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
xx, yy = np.meshgrid(x,y)
z = np.sin(xx)*np.cos(yy)*np.exp(-xx**2/6 - yy**2/3)

#--- plot ---#
fig = plt.figure()
ax = fig.gca(projection='3d')

# Customize the axes.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(0))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.xaxis.set_major_locator(LinearLocator(0))
ax.yaxis.set_major_locator(LinearLocator(0))

ax.plot_surface(xx,yy,z,cmap=cm.plasma,linewidth=0.1, antialiased=False)
plt.show()
