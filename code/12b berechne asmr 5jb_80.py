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
   

def lr_fit(years,data,imin,imax):
    fit_p=linregress(years[imin:imax],data[imin:imax])
    fit_v=fit_p.intercept+fit_p.slope*years
    return fit_v





cmr=pd.read_csv("../data_proc/cmr/agg_5_80p.csv",sep=";",index_col=0)
                
cmr.columns = cmr.columns.astype(int)



std_deu=pd.read_csv("../std_pops/deu20/deu20_5_80.csv",delimiter=";",
                header=None)

std_esp=pd.read_csv("../std_pops/esp13/esp13_5_80.csv",delimiter=";",
                header=None)

std_who=pd.read_csv("../std_pops/who15/who15_5_80.csv",delimiter=";",
                header=None)
###########################################################

for year in cmr.keys():
    # Spalte als Wert, Zeile als index über umweg referenziert
    c=cmr.loc[cmr.index[0:17],year]
    # a_d=np.dot(c,std_deu)
    
    cmr.loc["asmr_de",year]=np.dot(c,std_deu)
    cmr.loc["asmr_de_fit"]=lr_fit(cmr.keys(),cmr.loc["asmr_de",:],2,9)
    cmr.loc["psc_de"]=cmr.loc["asmr_de"]/cmr.loc["asmr_de_fit"]-1
    #############################################
    cmr.loc["asmr_esp",year]=np.dot(c,std_esp)
    cmr.loc["asmr_esp_fit"]=lr_fit(cmr.keys(),cmr.loc["asmr_esp",:],2,9)
    cmr.loc["psc_esp"]=cmr.loc["asmr_esp"]/cmr.loc["asmr_esp_fit"]-1
    
    #############################################
    cmr.loc["asmr_who",year]=np.dot(c,std_who)
    cmr.loc["asmr_who_fit"]=lr_fit(cmr.keys(),cmr.loc["asmr_who",:],2,9)
    cmr.loc["psc_who"]=cmr.loc["asmr_who"]/cmr.loc["asmr_who_fit"]-1

    
cmr.to_csv("../data_proc/cmr/asmr_5_80.csv",sep=";")

