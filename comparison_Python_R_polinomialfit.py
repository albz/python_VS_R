#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			26-02-2017
# Purpose:     comparison between python and R :: polinomail fit regression
# Source:       python
#####################################################################

import numpy as np
import pylab as pyl
from scipy import stats
import numpy.polynomial.polynomial as poly

#--- generate sample---#
x=np.linspace(-5,5,500)
y_therory=-1*x**3 +5*x**2 + x
y=y_therory+np.random.normal(0, 25, 500)

#---linear interpolation---#
coefficients = poly.polyfit(x, y, 3)
y_reconstructed = poly.polyval(x, coefficients)


#%matplotlib inline
pyl.plot(x,y,'.',label='scattered data')
pyl.plot(x,y_therory,'x',label='original data')
pyl.plot(x,y_reconstructed,'-',label='fit',lw=3)
pyl.legend()
