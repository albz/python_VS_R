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



raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'jan_arrests': [4, 24, 31, 2, 3],
        'feb_arrests': [25, 94, 57, 62, 70],
        'march_arrests': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']
df

ax1 = plt.subplot(111, aspect='equal')
df.plot(kind='pie', y = 'total_arrests', ax=ax1, autopct='%1.1f%%',
 startangle=90, shadow=False, labels=df['officer_name'], legend = False, fontsize=14)
