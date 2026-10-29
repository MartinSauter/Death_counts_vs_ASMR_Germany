# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:06:50 2025

@author: Martin Sauter
"""

import pandas as pd
import numpy as np


df=pd.read_csv("../data_orig/pop back calc/pop_back_age.csv",
               sep=",",index_col=0)





####################################################


alter = (
    df.index.to_series().astype(int)
)
#########################################################

gruppen20 = pd.cut(
    alter,
    bins=[0, 15, 30, 40, 60, 80, float("inf")],
    right=False,
    labels=["0-14", "15-29", "30-39", "40-59", "60-79", "80+"]
)

df_agg_20 = df.groupby(gruppen20,observed=False).sum()

df_agg_20.to_csv("../data_proc/pop_back/agg_20.csv")

#########################################################

gruppen10 = pd.cut(
    alter,
    bins=[0,10,20,30,40,50,60,70,80, float("inf")],
    right=False,
    labels=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
)

df_agg_10 = df.groupby(gruppen10,observed=False).sum()

df_agg_10.to_csv("../data_proc/pop_back/agg_10.csv")
#########################################################

gruppen5 = pd.cut(
    alter,
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80, float("inf")],
    right=False,
    labels=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
            "45-49","50-54","55-59","60-64","64-69","70-74","75-79","80+"]
)

df_agg_5 = df.groupby(gruppen10,observed=False).sum()

df_agg_5.to_csv("../data_proc/pop_back/agg_5.csv")



