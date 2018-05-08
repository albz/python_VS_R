#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:     comparison between python and R :: Linear Regression
# Source:       python
#####################################################################

#--- generate sample---#
x<-seq(1,10,length=100)
y_therory<-x
y=y_therory+rnorm(n=100,mean=0.,sd=1.)
mydata<-data.frame(x,y,y_therory)

#---linear interpolation---#
linear_model <- lm(data=mydata,y~x)
mydata$prediction<-predict(linear_model,newdata=mydata, se=FALSE)

#--- plot ---#
ggplot(mydata, aes(x=x, y=y)) + geom_point() +
geom_line(aes(x=x,y=prediction),colour="#CC0000",size=1.3)+
geom_point(aes(x=x,y=y_therory),shape = 2) +
xlab("x")+ylab("y")
