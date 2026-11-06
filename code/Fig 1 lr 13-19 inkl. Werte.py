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



def format_func(value, tick_number):
    return f'{value:,.0f}'.replace(',', ' ')  
    # Umständlich Tausendertrennzeichen, ohne Dezimalstellen
##################################################

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


df=pd.read_csv("../data_orig/deaths/12613-0002_de.csv",delimiter=";",
               skiprows=5,skipfooter=4,index_col=0,engine='python')

j=df.index.to_numpy()
t=df["Insgesamt"].to_numpy()




################################
plt.figure(figsize=(10,7),dpi=100)
plt.clf()
plt.style.use("classic")
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 13
plt.xlim(2009,2025)
plt.ylim(8e5,1.1e6)

plt.plot(j,t,linestyle="--",lw=0.5,marker="o",color="salmon",
         label="Observed Deaths in Germany",
         markeredgecolor="salmon")

plt.grid(True,color="black",linewidth=0.5)

ax = plt.gca()
ax.set_xticks(np.linspace(2010,2024,15).astype(int))
ax.set_xticklabels(np.linspace(2010,2024,15).astype(int),
                   fontsize=13,rotation=45)

ax.set_yticks(np.linspace(8e5,1.1e6,7))

# Formatter für die y-Achse setzen
ax.yaxis.set_major_formatter(FuncFormatter(format_func))


plt.xlabel("Year")
plt.ylabel("Annual Deaths")
ax.spines[:].set_color('black')

#


lf=linregress(j[3:10]-2013,t[3:10].astype(int))
# Fit
t_f=(j-2013)*lf.slope+lf.intercept  
# p-score
p_t=t/t_f-1

print("-------------------------------------------------------------------")
print(f"Intercept D0 {lf.intercept:g};Slope mtot {lf.slope/lf.intercept:.5f}; ")
print("-------------------------------------------------------------------\n")





plt.plot(j,t_f,marker="",linewidth=2,
             label="Linear Regression 2013-2019 ",
             ls="-",color="dodgerblue",alpha=1)
   
##############################################################
#
# P-score und Pfeile


min_val,max_val=np.min(p_t[2:9]),np.max(p_t[2:9])
min_idx,max_idx=np.argmax(p_t==min_val),np.argmax(p_t==max_val)


add_arrow(min_idx,j,t,t_f,ax)

add_arrow(max_idx,j,t,t_f,ax)


for idx in [10,11,12,13]:
    add_arrow(idx,j,t,t_f,ax)




#################################################################

plt.legend(loc="upper left",facecolor="white",
           edgecolor="white")

plt.tight_layout()

################################################################
print("Absolute Excess, Tab. 1 1st line")
print("-------------------------------------------------------------------")

print(
    f"{'2020':>12}"
    f"{'2021':>12}"
    f"{'2022':>12}"
    f"{'2023':>12}"
)

for k in [-5,-4,-3,-2]:
    print(f"{(t[k]-t_f[k]).astype(int):>12g}",end="")

print("")     
print("-------------------------------------------------------------------\n")


# plt.savefig("../figures/Fig 1 de fit 13-19 inkl psc.png",dpi=1000)

# plt.savefig("../figures/Fig 1 de fit 13-19 inkl psc.pdf",
#             bbox_inches='tight')
            
