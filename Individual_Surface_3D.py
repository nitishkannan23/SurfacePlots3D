# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:43:40 2018

@author: nitish
"""

from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

df_permian =  pd.read_excel("./PermianTops.xlsx")
formation_names = list(np.unique(df_permian['FormationName']))
fname = 'Bell Canyon'

x = df_permian['Lat'][df_permian['FormationName'] == fname]
y = df_permian['Long'][df_permian['FormationName'] == fname]
z = df_permian['FormationTopMD'][df_permian['FormationName'] == fname]
xyz = {'x' : x , 'y' : y , 'z' : z}
df = pd.DataFrame(xyz)
df = df.reset_index()
df = df.dropna()

x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
x2, y2 = np.meshgrid(x1, y1)
z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,22000)

ax.zaxis.set_major_locator(LinearLocator(12))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('Latitude',fontsize=16,labelpad=15)
ax.set_ylabel('Longitude',fontsize=16,labelpad=15)
ax.set_zlabel('Depth',fontsize=16,labelpad=15)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.suptitle(fname+': '+'Avg Depth(' +str( np.around(np.array(z).mean(),decimals=2))+'ft)', fontsize=16)
plt.xlim(30, 34)
plt.ylim(-105,-100 )

ax.invert_zaxis()
fig.tight_layout()
fig.subplots_adjust(top=1)
plt.show()
