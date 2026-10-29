# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:06:50 2025

@author: Martin Sauter
"""

import pandas as pd
import numpy as np


df=pd.read_csv("../data_orig/deaths/12613-0002_de.csv",sep=";",
               skiprows=5,skipfooter=4,engine="python",index_col=0)

df=df.drop(columns=["männlich","weiblich"])

df = df.drop(df.index[0])  # lösche 2010


df= df.transpose()
df.index=["Todesfaelle"]

#####################################################

pop_2011=pd.read_csv("../data_orig/pop zensus 2011/12411-0005_$F.csv",
                     sep=";",encoding="ISO8859-1",
                     skiprows=6,skipfooter=4,engine="python",index_col=0)

pop_2011=pop_2011.loc[["Insgesamt"]]
pop_2011.columns=np.linspace(2005,2024,20).astype(int)
pop_2011=pop_2011.drop(columns=np.linspace(2005,2010,6))

pop_2011.index=["p_2011"]

df=pd.concat([df,pop_2011])

#####################################################

pop_2022=pd.read_csv("../data_orig/pop zensus 2022/12411-0005_de.csv",
                     sep=";",encoding="ISO8859-1",
                     skiprows=6,skipfooter=4,engine="python",index_col=0)

pop_2022=pop_2022.loc[["Insgesamt"]]
pop_2022.columns=np.linspace(2012,2026,15).astype(int)
pop_2022.insert(0, 2011,81751602)

pop_2022=pop_2022.drop(columns=[2025,2026])

pop_2022.index=["p_2022"]
df=pd.concat([df,pop_2022])
######################################################

pop_2022_back=pd.read_csv("../data_orig/pop back calc/pop_back_tot.csv",
                          index_col=0).transpose()

pop_2022_back.insert(0, 2011,81751602)

pop_2022_back.insert(12,2023,83118501)
 
pop_2022_back.insert(13,2024,83456045)

pop_2022_back.index=["p_2022_back"]
df=pd.concat([df,pop_2022_back])

#####################################################

df.to_csv("../data_proc/synth/df_dn_pop.csv",sep=";")