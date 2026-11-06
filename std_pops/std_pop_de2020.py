# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:56:01 2026

@author: Martin Sauter
"""

import pandas as pd
import numpy as np

df=pd.read_csv("../data_proc/pop/agg_5_85.csv",sep=";")


pop=df["2020"].values

# normalize
de20_5=pop/pop.sum()
np.set_printoptions(formatter={'float': lambda x: f"{x * 100:.4f}%"})
print("-------------------------------------")

print("5y-bands, 85+  (18 values)")
print("")

print(de20_5)
print("")
#######################################################

df=pd.read_csv("../data_proc/pop/agg_10.csv",sep=";")


pop=df["2020"].values

# normalize
de20_10=pop/pop.sum()

print("------------------------------------")
print("10y-bands, 80+ (9 values)")
print("")
print(de20_10)
print("------------------------------------")

######################################################################


np.set_printoptions(formatter={'float': lambda x: f"{x:.7f}\n"})
print("5-y-bands")

print(de20_5)
print("---------------------")

print("10y-bands")

print(de20_10)

np.savetxt("../std_pops/deu20/deu20_10.csv",de20_10)
np.savetxt("../std_pops/deu20/deu20_5_85.csv",de20_5)

#  generate array with 80+ open ended group

de20_5_80=de20_5[0:len(de20_5)-1].copy()
de20_5_80[-1]=de20_5[-1]+de20_5[-2]

print("-------------------------------------")

print("5y-bands, 80+  (17 values)")
print("")

print(de20_5_80)
print("")
np.savetxt("../std_pops/deu20/deu20_5_80.csv",de20_5_80)


"""
Results human readable:
    
-------------------------------------
5y-bands, 85+  (18 values)
[4.7632% 4.4813% 4.4524% 4.7366% 5.5412% 6.1016% 6.6081% 6.3598% 5.9026%
 6.3407% 8.0684% 8.1010% 6.7909% 5.8425% 4.4177% 4.6610% 3.9611% 2.8700%]

------------------------------------
10y-bands, 80+ (9 values)

[9.2445% 9.1890% 11.6428% 12.9678% 12.2433% 16.1694% 12.6334% 9.0788%
 6.8310%]
------------------------------------  
      
  

"""