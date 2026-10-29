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

    
df=pd.read_csv("../data_proc/synth/df_dn_pop.csv",sep=";",
               index_col=0).astype(np.int64)



df.loc["cmr_2011"]=df.loc["Todesfaelle"]/df.loc["p_2011"]
df.loc["cmr_2022"]=df.loc["Todesfaelle"]/df.loc["p_2022"]
df.loc["cmr_2022_back"]=df.loc["Todesfaelle"]/df.loc["p_2022_back"]

years=df.keys().values.astype(int)



###########################################################

dn_fit=lr_fit(years,df.loc["Todesfaelle"].values,2,9)
cmr_2011_fit=lr_fit(years,df.loc["cmr_2011"].values,2,9)
cmr_2022_fit=lr_fit(years,df.loc["cmr_2022"].values,2,9)
cmr_2022_back_fit=lr_fit(years,df.loc["cmr_2022_back"].values,2,9)


###########################################################


fig,ax=plt.subplots(2,2,figsize=(9,8))


for i,a in enumerate(ax.flat):
    a.set_xlim(2011,2025)
    a.grid(True)
    a.xaxis.set_major_formatter(FuncFormatter(small_int_func))
    if i == 0:
        a.yaxis.set_major_formatter(FuncFormatter(int_func))
    else:
        a.yaxis.set_major_formatter(FuncFormatter(proc_func))
    
ax[0,0].plot(years,df.loc["Todesfaelle"],color="salmon",marker="o")
ax[0,0].plot(years,dn_fit,color="dodgerblue")


ax[0,1].plot(years,df.loc["cmr_2011"],color="salmon",marker="o")
ax[0,1].plot(years,cmr_2011_fit,color="dodgerblue")



ax[1,0].plot(years,df.loc["cmr_2022"],color="salmon",marker="o")
ax[1,0].plot(years,cmr_2022_fit,color="dodgerblue")



ax[1,1].plot(years,df.loc["cmr_2022_back"],color="salmon",marker="o")
ax[1,1].plot(years,cmr_2022_back_fit,color="dodgerblue")
#########################################################

def calc_plot_psc(years,data,fit,ax,tit):
    psc=data/fit-1
    max_psc=max(psc[2:9])
    min_psc=min(psc[2:9])
    
    upper_hist=fit*(1+max_psc)
    lower_hist=fit*(1+min_psc)
    
    ax.fill_between(years,lower_hist,upper_hist,color="gainsboro",
                 alpha=0.3)
    ax.set_title(tit)

    
    for i in [9,10,11,12,13]:
        ax.text(years[i],fit[i]*0.98,f"{psc[i]:.2%}")

calc_plot_psc(years,df.loc["Todesfaelle"].values,dn_fit,ax[0,0],"CDC")
calc_plot_psc(years,df.loc["cmr_2011"].values,cmr_2011_fit,ax[0,1],"CMR with Census 2011")
calc_plot_psc(years,df.loc["cmr_2022"].values,cmr_2022_fit,ax[1,0],"CMR with Census 2022")
calc_plot_psc(years,df.loc["cmr_2022_back"].values,cmr_2022_back_fit,ax[1,1],"Census 2022 with correction")
        


#########################################################
plt.tight_layout()