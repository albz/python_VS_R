#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-01-2018
# Purpose:      QQ-plot with python :: comparison between python and R
# Source:       python
#####################################################################

import numpy as np
import statsmodels.api as sm
import pylab as pyl

#--- generate sample---#
test1 = np.random.normal(0,1, 100)
test2 = np.random.chisquare(5,100)

#--- qqplot ---#
%matplotlib inline
sm.qqplot(test1, line='45')
sm.qqplot(test2, line='45')
pyl.show()
