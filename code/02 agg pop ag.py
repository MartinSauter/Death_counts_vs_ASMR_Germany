# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:06:50 2025

@author: Martin Sauter
"""

import pandas as pd
import numpy as np




pop=pd.read_csv("../data_orig/pop/12411-0005_$F.csv",
                     sep=";",encoding="ISO8859-1",
                     skiprows=6,skipfooter=4,engine="python",index_col=0)



pop.columns=np.linspace(2005,2024,20).astype(int)

ver=pop.loc[["Insgesamt"]]

pop=pop.drop(["Insgesamt"])
pop=pop.drop(columns=np.linspace(2005,2010,6))

pop.index=np.linspace(0,85,86).astype(int)


####################################################


alter = (
    pop.index.to_series().astype(int)
)
########################################################

gruppen20 = pd.cut(
    alter,
    bins=[0, 20, 40, 60, 80, float("inf")],
    right=False,
    labels=["0-19", "20-39", "40-59", "60-79", "80+"]
)

df_agg_20 = pop.groupby(gruppen20,observed=False).sum()

df_agg_20.to_csv("../data_proc/pop/agg_20.csv",sep=";")

#########################################################

gruppen10 = pd.cut(
    alter,
    bins=[0,10,20,30,40,50,60,70,80, float("inf")],
    right=False,
    labels=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
)

df_agg_10 = pop.groupby(gruppen10,observed=False).sum()

df_agg_10.to_csv("../data_proc/pop/agg_10.csv",sep=";")
########################################################

gruppen5 = pd.cut(
    alter,
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85, float("inf")],
    right=False,
    labels=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
            "45-49","50-54","55-59","60-64","64-69","70-74","75-79","80-84","85+"]
)

df_agg_5 = pop.groupby(gruppen5,observed=False).sum()

df_agg_5.to_csv("../data_proc/pop/agg_5.csv",sep=";")


#####################################################
gruppen5_80p = pd.cut(
    alter,
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80, float("inf")],
    right=False,
    labels=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
            "45-49","50-54","55-59","60-64","64-69","70-74","75-79","80+"]
)

df_agg_5_80p = pop.groupby(gruppen5_80p,observed=False).sum()

df_agg_5_80p.to_csv("../data_proc/pop/agg_5_80p.csv",sep=";")
