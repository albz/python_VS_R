#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			26-02-2017
# Purpose:     comparison between python and R :: polinomail fit regression
# Source:       python
#####################################################################

#--- generate sample---#
x<-seq(-5,5,length=500)
y_therory<--1*x^3 +5*x^2 + x
y=y_therory+rnorm(n=500,mean=0.,sd=25.)
mydata<-data.frame(x,y,y_therory)

#---linear interpolation---#
poly_fit <- lm(mydata$y~poly(x,3))
mydata$prediction<-predict(poly_fit,newdata=mydata, se=FALSE)

#--- plot ---#
ggplot(mydata, aes(x=x, y=y)) + geom_point() +
geom_point(aes(x=x,y=y_therory),shape = 2,color="orange") +
geom_line(aes(x=x,y=prediction),colour="blue",size=1.3)+
xlab("x")+ylab("y")
