#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:      comparison between python and R :: Shapiro-Wilks test
# Source:       python
#####################################################################

import numpy as np
import pylab as pyl
from scipy import stats
import numpy.polynomial.polynomial as poly

#--- generate random samples---#
N=10000
x=np.linspace(0,10,N)
y_therory=x
y_n5 =y_therory+np.random.normal(0, 5, N)
y_5n =y_therory+np.random.normal(0, 1, N)+np.random.normal(0, 1, N)+np.random.normal(0, 1, N)+np.random.normal(0, 1, N)+np.random.normal(0, 1, N)

#--- plot the two samples ---#
%matplotlib inline
pyl.plot(x,y_n5,'.',label='N ~ $\sigma$=5')
pyl.plot(x,y_5n,'.',label='5 N ~ $\sigma$=1')
pyl.legend()


#---linear interpolation---#
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
coefficients = poly.polyfit(x, y, 1)
y_reconstructed = poly.polyval(x, coefficients)


%matplotlib inline
pyl.plot(x,y,'.',label='scattered data')
pyl.plot(x,y_therory,'x',label='original data')
pyl.plot(x,y_reconstructed,'-',label='fit',lw=3)
pyl.legend()
