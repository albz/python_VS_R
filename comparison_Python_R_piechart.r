#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:     comparison between python and R :: cake plot
# Source:       python
#####################################################################

#--- generate sample---#
df <- data.frame(
  group = c("apple", "peach", "melon"),
  value = c(25, 25, 50)
  )

library(ggplot2)

pie <- ggplot(df, aes(x="", y=value, fill=group)) + 
       geom_bar(width = 1, stat = "identity") + theme_void() +
       coord_polar("y",start=0) +
       geom_text(aes(x=1, y = c(12.5,87.5,50), label=value))

pie


