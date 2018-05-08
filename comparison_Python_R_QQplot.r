#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:  comparison between python and R :: qqplot
# Source:   R
#####################################################################

#--- generate sample---#
set.seed(42)
x <- rnorm(n=1000,mean=0.,sd=1)
y <- rchisq(n=1000, df = 5)

#--- plot ---#
qqnorm(x)
qqline(x)

qqnorm(y)
qqline(y)
