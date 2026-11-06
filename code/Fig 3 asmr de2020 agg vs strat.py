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


def lr():
    return a_80_84
###########################################

df=pd.read_csv("../data_proc/cmr/asmr_5_85.csv",delimiter=";",
               index_col=0)
               
j=df.keys().astype(int).to_numpy()

a_80_84=df.loc["80-84",:].values
a_85_p=df.loc["85+",:].values

asmr_sep=(a_80_84*3.961+a_85_p*(1.880+0.791+0.178+0.020))/100

# 3.961,1.880+0.791+0.178+0.020]) / 100

lr_sep=linregress(j[2:9]-2013,asmr_sep[2:9])


asmr_sep_fit=lr_sep.intercept+lr_sep.slope*(j-2013)


############################################

df=pd.read_csv("../data_proc/cmr/asmr_5_80.csv",delimiter=";",
               index_col=0)

asmr_tot=df.loc["80+",:].values*6.831/100

# Weighing factor hard coded

# lr

lr_tot=linregress(j[2:9]-2013,asmr_tot[2:9])


asmr_tot_fit=lr_tot.intercept+lr_tot.slope*(j-2013)


############################################


plt.figure(figsize=(10,7),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
plt.xlim(2010,2025)
plt.ylim(0.006,0.0084)

plt.xlabel("Year")
plt.ylabel("Contribution ASMR (deaths per person)")

ax = plt.gca()
ax.set_xticks(np.linspace(2010,2024,15).astype(int))
ax.set_xticklabels(np.linspace(2010,2024,15).astype(int),
                   fontsize=13,rotation=45)

plt.grid(True,color="black",linewidth=0.5)
##########################################

plt.plot(j,asmr_sep,linestyle="--",lw=0.5,marker="o",color="salmon",
         label="ASMR, 5y-Bands, Stratified (80-84, 85+)",
         markeredgecolor="salmon")

plt.plot(j,asmr_sep_fit,linestyle="-",lw=2,marker="",color="salmon",
         label="Stratified, Fit 2013-2019 ",
         markeredgecolor="salmon")



plt.plot(j,asmr_tot,linestyle="--",lw=0.5,marker="o",color="Dodgerblue",
         label="ASMR, 5y-Bands, Aggregated (80+)",
         markeredgecolor="Dodgerblue")

plt.plot(j,asmr_tot_fit,linestyle="-",lw=2,marker="",color="Dodgerblue",
         label="Aggregated (80+), Fit 2013-2019 ",
         markeredgecolor="Dodgerblue")


plt.legend(loc="upper right")


#ax.set_yticks(np.linspace(8e5,1.1e6,7))



# plt.savefig("../figures/Fig 3 asmr de_5y_varianten.png",dpi=1000)

# plt.savefig("../figures/Fig 3 asmr de_5y_varianten.pdf",
#             bbox_inches='tight')
            



