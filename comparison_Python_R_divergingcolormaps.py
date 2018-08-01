#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			01-07-2018
# Purpose:     comparison between python and R :: diverging colormaps
# Source:       python
#####################################################################

import numpy as np
import pylab as pyl

#--- generate mesh ---#
x=np.linspace(0.,1.,100)
y=np.linspace(0.,1.,100)
xx, yy = np.meshgrid(x, y)
z = 2*xx-1

%matplotlib inline
ax1  = pyl.subplot(111)
extent = (np.min(x),np.max(x),np.min(y),np.max(y))
im = ax1.imshow(z,interpolation = 'bicubic', cmap = plt.get_cmap('plasma'), aspect = 'auto' , extent=extent)
cbar_bck = plt.colorbar(im,ax = ax1,cmap=plt.get_cmap('plasma'),format = '%1.1f' ,ticks = [-1,-0.5,0,0.5,1])

#---*** Diverging colormap ***---#
ax1  = pyl.subplot(111)
extent = (np.min(x),np.max(x),np.min(y),np.max(y))
im = ax1.imshow(z,interpolation = 'bicubic', cmap = plt.get_cmap('bwr'), aspect = 'auto' , extent=extent)
cbar_bck = plt.colorbar(im,ax = ax1,cmap=plt.get_cmap('bwr'),format = '%1.1f' ,ticks = [-1,-0.5,0,0.5,1])
