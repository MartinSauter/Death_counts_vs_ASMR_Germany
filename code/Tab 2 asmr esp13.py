# -*- coding: utf-8 -*-
"""
Generatin Tab. 2 in Paper
Comparison of ASMR-p-scores
for stp. pops DE20, ESP13, WHO
"""



import pandas as pd


###########################################

df=pd.read_csv("../data_proc/cmr/asmr_5_85.csv",delimiter=";",
               index_col=0)
               

j=df.keys().astype(int).to_numpy()
#a=df.loc["asmr_de",:].to_numpy()
#a_fit=df.loc["asmr_de_fit",:].to_numpy()

p_de=df.loc["psc_de",:].to_numpy()
p_esp=df.loc["psc_esp",:].to_numpy()
p_who=df.loc["psc_who",:].to_numpy()


print(
           f"{'Year':>12}"
           f"{'2020':>12}"
           f"{'2021':>12}"
           f"{'2022':>12}"
           f"{'2023':>12}"
           f"{'min.':>12}{'max.':>12}"    
       )
       
######################################################
print(f"{'P-score DE20 ':<12}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_de[jahr]:>12.2%}",
                end="")

print(f"{min(p_de[3:9]):>12.2%}",end="")
print(f"{max(p_de[3:9]):>12.2%}",end="")

print("")
######################################################
print(f"{'P-score ESP13':<12}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_esp[jahr]:>12.2%}",
                end="")
    
print(f"{min(p_esp[3:9]):>12.2%}",end="")
print(f"{max(p_esp[3:9]):>12.2%}",end="")          
print("")
######################################################
print(f"{'P-score WHO':<12}",end="")
     
for jahr in [-5,-4,-3,-2]:
        
            print(
                f"{p_who[jahr]:>12.2%}",
                end="")
            
print(f"{min(p_who[3:9]):>12.2%}",end="")
print(f"{max(p_who[3:9]):>12.2%}",end="")          
print("")

"""
Result (Copy & Paste from Output):
    
       Year        2020        2021        2022        2023        min.        max.
P-score DE20        2.24%       4.74%       7.98%       3.41%      -2.68%       1.83%
P-score ESP13       2.26%       4.82%       7.95%       3.27%      -2.69%       1.73%
P-score WHO        1.81%       5.39%       7.93%       3.86%      -2.54%       1.64%

"""
