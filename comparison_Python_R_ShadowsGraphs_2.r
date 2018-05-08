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
y1<-1.1*x
y2<-0.8*x
y_up <- y + 1 + rnorm(n=100,mean=0.,sd=.3)
y_up1<-y1 + 1 + rnorm(n=100,mean=0.,sd=.3)
y_up2<-y2 + 1 + rnorm(n=100,mean=0.,sd=.3)
y_do <- y - 1 + rnorm(n=100,mean=0.,sd=.3)
y_do1<-y1 - 1 + rnorm(n=100,mean=0.,sd=.3)
y_do2<-y2 - 1 + rnorm(n=100,mean=0.,sd=.3)
mydata<-data.frame(x,y,y1,y2,y_do,y_do1,y_do2,y_up,y_up1,y_up2)

#--- plot ---#
ggplot(mydata, aes(x=x, y=y)) +
geom_line(color="blue") + geom_ribbon( aes(ymin=y_do,ymax=y_up), fill="blue", alpha="0.3") +
geom_line(aes(x=x, y=y1), color="black") + geom_ribbon( aes(ymin=y_do1,ymax=y_up1), fill="grey", alpha="0.3") +
geom_line(aes(x=x, y=y2), color="green") + geom_ribbon( aes(ymin=y_do2,ymax=y_up2), fill="green", alpha="0.3")
