# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:51:19 2023

@author: Martin Sauter
"""



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# from matplotlib.ticker import FuncFormatter
import pandas as pd





###########################################

df=pd.read_csv("../data_proc/cmr/asmr_5_85.csv",delimiter=";",
               index_col=0)
               

j=df.keys().astype(int).to_numpy()


p_de_5_85=df.loc["psc_de",:].to_numpy()

############################################

df=pd.read_csv("../data_proc/cmr/asmr_5_80.csv",delimiter=";",
               index_col=0)
p_de_5_80=df.loc["psc_de",:].to_numpy()

############################################

df=pd.read_csv("../data_proc/cmr/asmr_10.csv",delimiter=";",
               index_col=0)
p_de_10_80=df.loc["psc_de",:].to_numpy()

############################################

print(
           f"{'Year':^24}"
           f"{'2020':>12}"
           f"{'2021':>12}"
           f"{'2022':>12}"
           f"{'2023':>12}"
           f"{'min.':>12}{'max.':>12}"    
       )
       
######################################################
print(f"{'P-score DE2020,  5y, 85+ ':^24}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_de_5_85[jahr]:>12.2%}",
                end="")

print(f"{min(p_de_5_85[3:9]):>12.2%}",end="")
print(f"{max(p_de_5_85[3:9]):>12.2%}",end="")

print("")

######################################################
print(f"{'P-score DE2020,  5y, 80+ ':^24}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_de_5_80[jahr]:>12.2%}",
                end="")

print(f"{min(p_de_5_80[3:9]):>12.2%}",end="")
print(f"{max(p_de_5_80[3:9]):>12.2%}",end="")

print("")
######################################################
print(f"{'P-score DE2020, 10y, 80+ ':^24}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_de_10_80[jahr]:>12.2%}",
                end="")

print(f"{min(p_de_10_80[3:9]):>12.2%}",end="")
print(f"{max(p_de_10_80[3:9]):>12.2%}",end="")

print("")


""" 
Results (Copy & paste from output):
        Year                  2020        2021        2022        2023        min.        max.
P-score DE2020,  5y, 85+        2.24%       4.74%       7.98%       3.41%      -2.68%       1.83%
P-score DE2020,  5y, 80+        1.82%       4.83%       8.97%       5.78%      -2.56%       2.34%
P-score DE2020, 10y, 80+        1.09%       3.39%       6.78%       3.25%      -2.62%       2.34%
    
"""