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
def int_func(value, tick_number):
    return f'{value:,.0f}'.replace(',', ' ')  
    # Umständlich Tausendertrennzeichen, ohne Dezimalstellen
    
def small_int_func(value, tick_number):
    return f'{value:,.0f}'.replace(',', '')  
    # Umständlich Tausendertrennzeichen, ohne Dezimalstellen

def proc_func(value, tick_number):
    return f'{value:.3%}'.replace(',', ' ')
   

def lr_fit(years,data,imin,imax):
    fit_p=linregress(years[imin:imax],data[imin:imax])
    fit_v=fit_p.intercept+fit_p.slope*years
    return fit_v

    
df=pd.read_csv("../data_proc/synth/df_dn_pop.csv",sep=";",index_col=0)

years=df.keys().values.astype(int)


###########################################################


p_2011_fit=lr_fit(years,df.loc["p_2011"].values,2,9)
p_2022_fit=lr_fit(years,df.loc["p_2022"].values,2,9)
p_2022_back_fit=lr_fit(years,df.loc["p_2022_back"].values,2,9)


###########################################################


fig,ax=plt.subplots(1,1,figsize=(9,8))


ax.set_xlim(2011,2025)
ax.grid(True)
ax.xaxis.set_major_formatter(FuncFormatter(small_int_func))
ax.yaxis.set_major_formatter(FuncFormatter(int_func))

ax.plot(years,df.loc["p_2011"].values,color="dodgerblue",ls=(0, (10, 10)),
        marker="o",lw=2,label="Census 2011", alpha=0.5,markersize=5)
# ax.plot(years,p_2011_fit,color="dodgerblue",ls="--",
#         lw=2)    

epsy=10000 # minimalversatz
epsx=0.01

ax.plot(years+epsx,df.loc["p_2022"].values+epsy,color="red",ls="-.",
        marker="o",lw=1,alpha=0.7,label="Census 2022")
# ax.plot(years,p_2022_fit,color="salmon",ls="--",
#         lw=2)    


ax.plot(years[0:12],df.loc["p_2022_back"].values[0:12],color="green",ls="--",
        marker="o",label="Census 2022, back calc.")
# ax.plot(years,p_2022_back_fit,color="green",ls="--",
#         lw=2) 



#########################################################
plt.legend(loc="upper left")
plt.tight_layout()