# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:51:19 2023

@author: Martin Sauter
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
import pandas as pd




# def format_func(value, tick_number):
#     return f'{value:,.0f}'.replace(',', ' ')  
#     # Umständlich Tausendertrennzeichen, ohne Dezimalstellen

def add_arrow(idx,j,a,a_fit,ax):
    """idx: Index in Arrays j,a,a_fit
    j: Jahre (x)
    a: Werte observed
    a_fit: linearer fit
    ax: Grafik
    """
    # arrow
    start=min(a[idx],a_fit[idx])
    stop=max(a[idx],a_fit[idx])
    r = patches.FancyArrowPatch((j[idx],start*1.002), (j[idx],stop*0.998), 
                                   arrowstyle='<->', mutation_scale=20)
    ax.add_patch(r)
    
    # text
    p=a[idx]/a_fit[idx]-1 
    txt=f"{p:.2%}"
    if p>0:
        ax.annotate(txt,(j[idx]+0.1,stop*1.002),color="dodgerblue")
    else:
        ax.annotate(txt,(j[idx]+0.1,start*0.998),color="dodgerblue")

###########################################

df=pd.read_csv("../data_proc/cmr/asmr_5.csv",delimiter=";",
               index_col=0)
               

j=df.keys().astype(int).to_numpy()
a=df.loc["asmr_de",:].to_numpy()
a_fit=df.loc["asmr_de_fit",:].to_numpy()

p_a=df.loc["psc_de",:].to_numpy()


################################
plt.figure(figsize=(10,7),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
plt.xlim(2010,2025)
plt.ylim(0.0112,0.0126)

plt.plot(j,a,linestyle="--",lw=0.5,marker="o",color="salmon",
         label="ASMR Germany, 5y-Bands, Open-Ended Group 85+, ",
         markeredgecolor="salmon")

plt.grid(True,color="black",linewidth=0.5)

ax = plt.gca()
ax.set_xticks(np.linspace(2010,2024,15).astype(int))
ax.set_xticklabels(np.linspace(2010,2024,15).astype(int),
                   fontsize=13,rotation=45)

#ax.set_yticks(np.linspace(8e5,1.1e6,7))

# Formatter für die y-Achse setzen
#ax.yaxis.set_major_formatter(FuncFormatter(format_func))


plt.xlabel("Year")
plt.ylabel("Age Standardised Mortality Rate")
ax.spines[:].set_color('black')


plt.plot(j,a_fit,marker="",linewidth=2,
             label="Linear Regression 2013-2019 ",
             ls="-",color="dodgerblue",alpha=1)
   
##############################################################
#
# P-score und Pfeile

# min/max indizes and values of pscore prev.years

min_val,max_val=np.min(p_a[2:9]),np.max(p_a[2:9])
min_idx,max_idx=np.argmax(p_a==min_val),np.argmax(p_a==max_val)


add_arrow(min_idx,j,a,a_fit,ax)

add_arrow(max_idx,j,a,a_fit,ax)


for idx in [9,10,11,12]:
    add_arrow(idx,j,a,a_fit,ax)

#################################################################

plt.legend(loc="upper left",facecolor="white",
           edgecolor="white")

plt.tight_layout()



# plt.savefig("../figures/Fig 2 asmr de_5y_85p.png",dpi=1000)

# plt.savefig("../figures/Fig 2 asmr de_5y_85p fit.pdf",
#             bbox_inches='tight')
            
