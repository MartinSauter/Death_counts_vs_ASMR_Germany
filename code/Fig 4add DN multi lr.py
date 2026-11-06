# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:51:19 2023

@author: Martin Sauter
"""



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
import pandas as pd

from scipy.stats import linregress


def format_func(value, tick_number):
    return f'{value:,.0%}'
    # Umständlich Tausendertrennzeichen, ohne Dezimalstellen

def lr(x,y,start_lr,stop_lr):
    lf=linregress(x[start_lr:stop_lr+1],y[start_lr:stop_lr+1])
    fit=lf.intercept+lf.slope*x
    #psc=y/fit-1
    
    
    return fit

###########################################


df_t=pd.read_csv("../data_orig/deaths/12613-0002_de.csv",delimiter=";",
               skiprows=5,skipfooter=4,index_col=0,engine='python')

# starting 2010; delete 2010 for compatibility
j_t=df_t.index.to_numpy()[1:]
t=df_t["Insgesamt"].to_numpy()[1:]

#############################################

# new df




plt.figure(figsize=(7,6),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
#plt.xlim(0,0.11)
#plt.ylim(0,0.11)

#plt.xlabel("Death-count-based P-score (%)")
#plt.ylabel("ASMR-based P-score (%)")

ax = plt.gca()
# ax.yaxis.set_major_formatter(FuncFormatter(format_func))
# ax.xaxis.set_major_formatter(FuncFormatter(format_func))

plt.grid(True,color="black",linewidth=0.5)
ax.grid(zorder=0)
##########################################

plt.plot(j_t,t,ls="",marker="o")

for k in [0,1,2,3,4,5]:
    fit_t=lr(j_t,t,k,8)
    plt.plot(j_t,fit_t,ls="-",lw=0.5,marker="",label=j_t[k])
    
    #print(f"{j_t[k]}\t{fit_t[-2]:.0f}")
    print(j_t[k])
    print(100*(t[-5:-1]/fit_t[-5:-1]-1))
    
plt.legend(loc="upper left")
    

