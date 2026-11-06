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

from scipy.stats import linregress


def lr(x,y,start_lr,stop_lr):
    lf=linregress(x[start_lr:stop_lr+1],y[start_lr:stop_lr+1])
    fit=lf.intercept+lf.slope*x
    psc=y/fit-1
    
    
    return psc

###########################################

df_a=pd.read_csv("../data_proc/cmr/asmr_5.csv",delimiter=";",
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


plt.figure(figsize=(10,7),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
plt.xlim(0,0.1)
plt.ylim(0,0.1)

plt.xlabel("P-score from Deaths")
plt.ylabel("P-score from ASMR")

ax = plt.gca()
# ax.set_xticks(np.linspace(2010,2024,15).astype(int))
# ax.set_xticklabels(np.linspace(2010,2024,15).astype(int),
#                    fontsize=13,rotation=45)

plt.grid(True,color="black",linewidth=0.5)
##########################################
colors=["red","blue","salmon","dodgerblue"]
k=0
for year in psc_a.keys().values[0:4]:
    plt.scatter(psc_a[year],psc_t[year],color=colors[k])
    k+=1
# ,linestyle="--",lw=0.5,marker="o",color="salmon",
#          label="ASMR, 5y-Bands, Stratified (80-84, 85+)",
#          markeredgecolor="salmon")

# plt.plot(j,asmr_sep_fit,linestyle="-",lw=2,marker="",color="salmon",
#          label="Stratified, Fit 2013-2019 ",
#          markeredgecolor="salmon")



# plt.plot(j,asmr_tot,linestyle="--",lw=0.5,marker="o",color="Dodgerblue",
#          label="ASMR, 5y-Bands, Aggregated (80+)",
#          markeredgecolor="Dodgerblue")

# plt.plot(j,asmr_tot_fit,linestyle="-",lw=2,marker="",color="Dodgerblue",
#          label="Aggregated (80+), Fit 2013-2019 ",
#          markeredgecolor="Dodgerblue")


#plt.legend(loc="upper right")


#ax.set_yticks(np.linspace(8e5,1.1e6,7))



# plt.savefig("../figures/Fig 3 asmr de_5y_varianten.png",dpi=1000)

# plt.savefig("../figures/Fig 3 asmr de_5y_varianten.pdf",
#             bbox_inches='tight')
            



