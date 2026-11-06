# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:18:38 2022

@author: Martin Sauter
"""



import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

from cycler import cycler



def format_func(value, tick_number):
    return f'{value:,.0f}'.replace(',', ' ')  
    # Umständlich Tausendertrennzeichen, ohne Dezimalstellen

#####################################################




plt.style.use("classic")
plt.rcParams["lines.linewidth"]=2
plt.rcParams['font.family'] = 'Arial'
plt.rcParams["font.size"]=13
plt.rcParams['axes.prop_cycle'] = cycler('color',
                                         plt.get_cmap('Paired').colors)


########################################################################


df=pd.read_csv("../data_proc/deaths/agg_20.csv",sep=";",
              index_col=0)



jahre=df.keys().values.astype(int)
lbls=df.index.values.astype(str)

#############################################################

fig,ax=plt.subplots(3,2,figsize=(12,8))
x=0;y=0
k=0



# with open("ausgabe.txt","w") as file:
#        print()

fname="Tab.1 Data CDC Trend 13-19 20y age groups.txt"
with open(fname, "w"):
    pass
   

for group in lbls:
    
    x=k%2
    y=k//2
    
    if x==0:ax[y,x].set_ylabel("Annual Deaths in Age Group")
    
    ax[y,x].grid(True)
    
    ag=df.loc[group,:].values
    ax[y,x].plot(jahre,ag,marker="x",linestyle="--",color="dodgerblue")
    
    
    lf=linregress(jahre[2:9]-2013,ag[2:9].astype(int))
    print(f"AG: {lbls[k]}, R²={(lf.stderr)} \n")
    print("----------------------------")
    
    # Fit
    trend=(jahre-2013)*lf.slope+lf.intercept  
    
    sigma_min=min(ag[2:9]/trend[2:9])-1
    sigma_max=max(ag[2:9]/trend[2:9])-1
    
    d_lo=trend*(1+sigma_min)
    d_hi=trend*(1+sigma_max)
            
    locs=["upper left"]*6
    # ,"upper left",
    #       "upper left","upper left",
    #       "upper left","upper left"]
  
        
    
    ax[y,x].plot(jahre,trend,linestyle="-",color="red",label="") 
    
    ## min/max areas
    
    ax[y,x].plot(jahre,d_lo,color="lightgrey",linestyle="--")
    ax[y,x].plot(jahre,d_hi,color="lightgrey",linestyle="--")
    
    ax[y,x].fill_between(jahre,d_hi,d_lo,color="gainsboro",
                           alpha=0.6)
    
    #handles, labels = ax[y,x].get_legend_handles_labels()
    
    blue_line = Line2D([0], [0], color="dodgerblue", linewidth=2,ls="--")
    red_line = Line2D([0], [0], color="red", linewidth=2)
    rect = Rectangle((0,0), 1, 1, fc="gainsboro", edgecolor = 'none')
    
    if x==0 and y==0:
        
        handles, labels = ax[y,x].get_legend_handles_labels()
        
        labels.append(lbls[k])
        handles.append(blue_line)
        
        labels.append("Trend 2013-19")
        handles.append(red_line)
    
        labels.append("2013-19 Min/Max")
        handles.append(rect)
    
    else: 
        handles, labels = ax[y,x].get_legend_handles_labels()
        
        labels.append(lbls[k])
        handles.append(blue_line)
 
    
    ax[y,x].legend(handles, labels,loc=locs[k],fontsize=12,edgecolor="none")
    
    ax[y,x].set_xlim(2010.5,2024.5)
    
    ax[y,x].set_xticks(np.linspace(2010,2024,15).astype(int))
    
    
    if ((x==0) & (y==2)) | ((x==1)& (y==1)):
        ax[y,x].set_xticklabels(np.linspace(2010,2024,15).astype(int),rotation="vertical")
       
    else: ax[y,x].set_xticklabels([])
    
   
    
    ax[y,x].yaxis.set_major_formatter(FuncFormatter(format_func))
    
 
    if k==0:
        # Header
        
        with open(fname, "a") as file:  
           print(
               f"{'':12}"
               f"{'2020':^24}"
               f"{'2021':^24}"
               f"{'2022':^24}"
               f"{'2023':^24}",
               file=file
           )
           
           print(
               f"{'Age group':<12}"
               + 4 *(f"{'abs.':>12}{'rel.':>12}")
               + f"{'min.':>12}{'max.':>12}"
         ,
           file=file
           )
           
    with open(fname, "a") as file:
   

            print(f"{lbls[k]:<12}",end="",file=file)
         
            for jahr in [-5,-4,-3,-2]:
            
                diff_abs=int(ag[jahr]-trend[jahr])
                psc=(ag[jahr]/trend[jahr]-1)
                 
                print(
                    f"{diff_abs:>12}"
                    f"{psc:>12.2%}",
                    end="",
                    file=file)

            print(
                f"{sigma_min:>12.2%}"
                f"{sigma_max:>12.2%}",
                file=file)

                        
    # with open(fname, "a") as file:
    #     print("",file=file)
    k+=1
    
######################################

plt.tight_layout()

fig.delaxes(ax[2,1])

# plt.savefig("../figures/Fig xx ÜS AG 13-19 20 gruppen.png",dpi=1000)

# plt.savefig("../figures/Fig xx  ÜS AG 13-19 20 gruppen.tif",dpi=600,
#             pil_kwargs={"compression": "tiff_lzw"})
