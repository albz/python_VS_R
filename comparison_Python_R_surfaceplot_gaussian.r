#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:  comparison between python and R :: contour plot
# Source:   R
#####################################################################

sigma <- matrix(c(3,1,1,1), nrow=2)
data.grid <- expand.grid(x = seq(-5, 5, length.out=100), y = seq(-5, 5, length.out=100))
z <- cbind(data.grid, prob = mvtnorm::dmvnorm(data.grid, mean = c(0,0), sigma = sigma))
ggplot(z, aes(x=x, y=y)) +
    geom_raster(aes(fill = prob)) +
    coord_fixed(xlim = c(-5, 5), ylim = c(-5, 5), ratio = 1)
