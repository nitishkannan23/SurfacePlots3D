# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:13:24 2018

@author: nitish
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import matplotlib as mpl
import pandas as pd
from mpltools import color

tops_df = pd.read_excel("./PermianTops.xlsx")
topid =np.asarray(tops_df['FormationTopID'])
lat=np.asarray(tops_df['Lat'])
long_=np.asarray(tops_df['Long'])
depth=np.asarray(tops_df['FormationTopMD'])
name=tops_df['FormationName'].unique()

#creating colors
import matplotlib.cm as cm
cm = plt.get_cmap('gist_rainbow')
colors= [cm(1.*i/20) for i in range(20)]

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')
    
for i in range(len(name)):
    X= tops_df['Lat'][tops_df['FormationName']==name[i]]
    Y= tops_df['Long'][tops_df['FormationName']==name[i]]
    Z=tops_df['FormationTopMD'][tops_df['FormationName']==name[i]]
    
    ax.scatter(X,Y, Z, marker='.',color=colors[i])

    ax.set_xlabel('Latitude',fontsize=16,labelpad=15)
    ax.set_ylabel('Longitude',fontsize=16,labelpad=15)
    ax.set_zlabel('Depth',fontsize=16,labelpad=15)
    
ax.legend(name,prop={'size': 10},loc=2, borderaxespad=0.,markerscale=5)
ax.invert_zaxis()

plt.xlim(30, 34)
plt.ylim(-105,-100 )
ax.set_zlim(0,22000)
ax.zaxis.set_major_locator(LinearLocator(12))

ax.invert_zaxis()
plt.show()

