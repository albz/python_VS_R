#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:  comparison between python and R :: shadow graphs
# Source:   R
#####################################################################

#--- generate sample---#
x<-seq(1,10,length=100)
y<-x
y_up<-y + 1 + rnorm(n=100,mean=0.,sd=.3)
y_do<-y - 1 + rnorm(n=100,mean=0.,sd=.3)
mydata<-data.frame(x,y,y_do,y_up)

#--- plot ---#
ggplot(mydata, aes(x=x, y=y)) + geom_line(color="magenta") +
geom_ribbon( aes(ymin=y_do,ymax=y_up), fill="gray", alpha="0.75")
