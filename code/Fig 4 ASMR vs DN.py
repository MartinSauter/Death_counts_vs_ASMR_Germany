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
    psc=y/fit-1
    
    
    return psc

###########################################

df_a=pd.read_csv("../data_proc/cmr/asmr_5_85.csv",delimiter=";",
               index_col=0)

#starting with 2011      
j_a=df_a.keys().astype(int).to_numpy()

a=df_a.loc["asmr_de"].values 


############################################


df_t=pd.read_csv("../data_orig/deaths/12613-0002_de.csv",delimiter=";",
               skiprows=5,skipfooter=4,index_col=0,engine='python')

# starting 2010; delete 2010 for compatibility
j_t=df_t.index.to_numpy()[1:]
t=df_t["Insgesamt"].to_numpy()[1:]

#############################################

# new df

cols = ["2020","2021","2022","2023","Min.","Max."]

# new empty df

psc_t = pd.DataFrame(columns=cols)
psc_a = pd.DataFrame(columns=cols)


# Schleife
# Index 8 = 2019
# k=0,1,2,3,4,5 -> 2011...2016


#for k in [2]:
for k in [0,1,2,3,4,5]:
    tmp_t=lr(j_t,t,k,8)
    print(tmp_t[-5:-1])
    minval,maxval=min(tmp_t[k:8]),max(tmp_t[k:8])
    
    psc_t.loc[j_t[k]]=np.array(np.array([*tmp_t[-5:-1], minval, maxval]))
    
    tmp_a=lr(j_a,a,k,8)
    print(tmp_a[-5:-1])
    psc_a.loc[j_t[k]]=np.array(np.array([*tmp_a[-5:-1], minval, maxval]))

# ############################################


plt.figure(figsize=(7,6),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
plt.xlim(0,0.11)
plt.ylim(0,0.11)

plt.xlabel("Death-count-based P-score (%)")
plt.ylabel("ASMR-based P-score (%)")

ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(format_func))
ax.xaxis.set_major_formatter(FuncFormatter(format_func))

plt.plot([0, 0.11], [0, 0.11], '--', label='Identity line',color="grey",alpha=0.5)

plt.grid(True,color="black",linewidth=0.5)
ax.grid(zorder=0)
##########################################
colors=["darkorange","seagreen","salmon","dodgerblue"]
markers = ["o", "s", "^", "D", "*", "X"]

k=0;
for year in psc_a.keys().values[0:4]:
    
    for l in range(6):
    
        plt.scatter(psc_a[year].values[l],psc_t[year].values[l],color=colors[k],
                    marker=markers[l],s=50)
    k+=1
##########################################

# Color legend
year_legend = [
    Line2D([0], [0],
           marker='o',
           color='none',
           linestyle='None',
           markerfacecolor=colors[i],
           markeredgecolor=colors[i],
           markersize=8,
           label=str(year))
    for i, year in enumerate(psc_a.keys().values[0:4])
]

leg1 = plt.legend(handles=year_legend,
                  title="Year",
                  loc="upper left",
                  numpoints=1,
                  frameon=True) 

plt.gca().add_artist(leg1)


frame=leg1.get_frame()
frame.set_facecolor("white")
frame.set_alpha(1.0)
frame.set_edgecolor("white")

#########################################
# Trend Legend

trends = [
    "2011–2019",
    "2012–2019",
    "2013–2019",
    "2014–2019",
    "2015–2019",
    "2016–2019"
]

marker_legend = [
    Line2D(
        [0], [0],
        marker=markers[i],
        linestyle='None',
        markerfacecolor='black',
        markeredgecolor='black',
        markersize=8,
        label=trend
    )
    for i, trend in enumerate(trends)
]

leg2 = plt.legend(
    handles=marker_legend,
    title="Reference period",
    loc="lower right",
    numpoints=1,
    frameon=True
)

frame = leg2.get_frame()
frame.set_facecolor("white")
frame.set_alpha(1.0)
frame.set_edgecolor("white")

plt.gca().add_artist(leg1)

plt.savefig("../figures/Fig 4 asmr dn trends",dpi=1000)

plt.savefig("../figures/Fig 4 asmr dn trends.pdf",
            bbox_inches='tight')
            



