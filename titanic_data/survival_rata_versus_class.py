#!/usr/bin/python
#####################################################################
# Author:	 Alberto Albz Marocchino + S. Romeo
# Date:		 08-05-2018
# Purpose:
# Source:    python
#####################################################################

import csv, os, path
import numpy as np
import pylab as pyl
import pandas as pd
from scipy import stats

#--- load data ---#
path='/Users/albz/Codes/python_VS_R/titanic_data'
# data = csv.reader(open(os.path.join(path,'titanic.csv'), 'r'), delimiter=',',quoting=csv.QUOTE_NONE)
df   = pd.read_csv(open(os.path.join(path,'titanic.csv')))

#--- count number of classes ---#
survived_c1=df[df['Pclass']==1]['Survived']
survived_c2=df[df['Pclass']==2]['Survived']
survived_c3=pd.asarray(df[df['Pclass']==3]['Survived'])

%matplotlib inline
dim=survived_c3.values.shape[0]
pyl.scatter(range(0,dim),3*np.ones(dim),s=15,c=survived_c3.values,marker='s')
dim=survived_c2.values.shape[0]
pyl.scatter(range(0,dim),2*np.ones(dim),s=15,c=survived_c2.values,marker='s')
dim=survived_c1.values.shape[0]
pyl.scatter(range(0,dim),1*np.ones(dim),s=15,c=survived_c1.values,marker='s',label=survived_c1.values)
pyl.xticks(size=12)
pyl.yticks([1,2,3],size=12)
pyl.xlabel('passengers',size=12)
pyl.xlim(0,500)
pyl.ylabel('ticket class',size=12)



#--- side hystograms ---#
s=[np.sum(survived_c1)]
s.append(np.sum(survived_c2))
s.append(np.sum(survived_c3))
n=[len(survived_c1)-np.sum(survived_c1)]
n.append(len(survived_c2)-np.sum(survived_c2))
n.append(len(survived_c3)-np.sum(survived_c3))

fig = pyl.figure(1)
fig.set_size_inches(3.25, 3.0, forward=True)
ax1 = pyl.subplot(111)
ax1.bar(np.array([1,2,3])-.19,s,.38,alpha=.5,label='Survived',color='lime')
ax1.bar(np.array([1,2,3])+.19,n,.38,alpha=.8,label='not Survived')
ax1.set_xlabel('class',fontsize=12)
ax1.set_ylabel('people',fontsize=12)
ax1.legend()
