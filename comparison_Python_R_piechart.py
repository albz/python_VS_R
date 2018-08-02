#!/usr/bin/python
#####################################################################
# Author:		Alberto Albz Marocchino
# Date:			19-02-2017
# Purpose:  comparison between python and R :: pie plot
# Source:   python
#####################################################################

#--- import packages ---#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#--- generate sample---#
data = {'fruit':['apple','peach','melon'], 'percentage':[25,25,50]}
df   = pd.DataFrame(data)

#--- plot ---#
%matplotlib inline
ax1 = plt.subplot(111, aspect='equal')
df.plot(kind='pie', y='percentage', ax=ax1, autopct='%1.1f%%', startangle=90, shadow=False, labels=df['fruit'], legend = False, fontsize=14)
