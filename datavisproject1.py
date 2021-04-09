#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 02:59:39 2020

@author: mac
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame, read_html

import urllib, json
from urllib.request import urlopen

from random import gauss, seed, randint
import os 
from datetime import datetime as dt
#for viz
from __future__ import division

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline

filepath=r"/Users/mac/Desktop/data vis"
act=pd.read_excel(filepath+os.sep+'activités domestiques maroc .xlsx')
act.head()
act.columns


data_p1 = act[act['Affichage et export de tableaux'] =='Femmes']
act_dom_femmes=data_p1[['Unnamed: 3']].loc[7:11]
data_p2 = act[act['Affichage et export de tableaux'] =='Hommes']
act_dom_hommes=data_p2[['Unnamed: 3']].loc[13:17]
objects = ('15-24 ans', '25-34 ans', '35-44 ans', '45-59 ans', '60 ans et plus')
y_pos = np.arange(len(objects))
performance =act_dom_hommes['Unnamed: 3'].values.tolist()
performance2=act_dom_femmes['Unnamed: 3'].values.tolist()
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)

# data to plot
n_groups = np.arange(len(objects))
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = n_groups
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, performance, bar_width,
alpha=opacity,
color='b',
label='hommes')

rects2 = plt.bar(index + bar_width, performance2, bar_width,
alpha=opacity,
color='r',
label='femmes')

plt.xlabel('Age')
plt.ylabel('% des personnes qui font des activités menageres')
plt.title('Activités domestiques par femmes et hommes')
plt.xticks(index + bar_width, objects)
plt.legend()

plt.tight_layout()
plt.show()