# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:06:50 2025

@author: Martin Sauter
"""

import pandas as pd
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from cycler import cycler
####################################################

plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size']=13
plt.rcParams['axes.prop_cycle'] = cycler('color',
                                          plt.get_cmap('tab10',7).colors)

#########################################################
# def int_func(value, tick_number):
#     return f'{value:,.0f}'.replace(',', ' ')  
#     # Umständlich Tausendertrennzeichen, ohne Dezimalstellen
    
# def small_int_func(value, tick_number):
#     return f'{value:,.0f}'.replace(',', '')  
#     # Umständlich Tausendertrennzeichen, ohne Dezimalstellen

# def proc_func(value, tick_number):
#     return f'{value:.3%}'.replace(',', ' ')
   

# def lr_fit(years,data,imin,imax):
#     fit_p=linregress(years[imin:imax],data[imin:imax])
#     fit_v=fit_p.intercept+fit_p.slope*years
#     return fit_v

    
dn=pd.read_csv("../data_proc/deaths/agg_20.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_20.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_20.csv",sep=";")
###########################################################

  
dn=pd.read_csv("../data_proc/deaths/agg_10.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_10.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_10.csv",sep=";")
###########################################################

###########################################################

  
dn=pd.read_csv("../data_proc/deaths/agg_5.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_5.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_5.csv",sep=";")
###########################################################
  
dn=pd.read_csv("../data_proc/deaths/agg_5_80p.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_5_80p.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_5_80p.csv",sep=";")
###########################################################

