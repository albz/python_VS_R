#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			26-02-2017
# Purpose:     comparison between python and R :: surface plot multivaraite gaussian
# Source:       python
#####################################################################

import numpy as np
import pylab as pyl

#--- generate mesh ---#
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
xx, yy = np.meshgrid(x, y)
z = np.exp(-xx**2/6 - yy**2/2 + xx*yy/2)

%matplotlib inline
plt.contourf(x,y,z,100)
