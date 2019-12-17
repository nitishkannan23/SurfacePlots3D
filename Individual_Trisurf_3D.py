# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:34:14 2018

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
for fname in formation_names:
    x = df_permian['Lat'][df_permian['FormationName'] == fname]
    y = df_permian['Long'][df_permian['FormationName'] == fname]
    z = df_permian['FormationTopMD'][df_permian['FormationName'] == fname] 
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x, y, z, linewidth=0.2,cmap='viridis',antialiased=True)
    ax.set_zlim(0,22000)

    ax.zaxis.set_major_locator(LinearLocator(12))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel('Latitude',fontsize=16,labelpad=15)
    ax.set_ylabel('Longitude',fontsize=16,labelpad=15)
    ax.set_zlabel('Depth',fontsize=16,labelpad=15)
    
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.suptitle(fname+': '+'Avg Depth(' +str( np.around(np.array(z).mean(),decimals=2))+'ft)', fontsize=16)
    plt.xlim(30, 34)
    plt.ylim(-105,-100 )
  
    ax.invert_zaxis()
    fig.tight_layout()
    fig.subplots_adjust(top=1)
    plt.show()
