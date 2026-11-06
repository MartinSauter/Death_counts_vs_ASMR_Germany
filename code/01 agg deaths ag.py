# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:06:50 2025

@author: Martin Sauter
"""

import pandas as pd
import numpy as np


df=pd.read_csv("../data_orig/deaths/12613-0003_de.csv",sep=";",
               skiprows=5,skipfooter=5,engine="python",index_col=None)

df=df[df["Unnamed: 0"]=="Insgesamt"]

df=df.drop(columns=["Unnamed: 0"])#,"Unnamed: 1"])
df = df.set_index("Unnamed: 1")



#####################################################


alter = (
    df.index.to_series()
      .str.extract(r'(\d+)')[0]
      .fillna(0)
      .astype(int)
)
###########################################################
gruppen20 = pd.cut(
    alter,
    bins=[0, 20, 40, 60, 80, float("inf")],
    right=False,
    labels=["0-19", "20-39", "40-59", "60-79", "80+"]
)

df_agg_20 = df.groupby(gruppen20,observed=True).sum()
df_agg_20.to_csv("../data_proc/deaths/agg_20.csv",sep=";")
###########################################################
gruppen10 = pd.cut(
    alter,
    bins=[0,10,20,30,40,50,60,70,80, float("inf")],
    right=False,
    labels=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
)

df_agg_10 = df.groupby(gruppen10,observed=False).sum()

df_agg_10.to_csv("../data_proc/deaths/agg_10.csv",sep=";")

########################################################

gruppen5 = pd.cut(
    alter,
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85, float("inf")],
    right=False,
    labels=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
            "45-49","50-54","55-59","60-64","64-69","70-74","75-79","80-84","85+"]
)

df_agg_5 = df.groupby(gruppen5,observed=False).sum()

df_agg_5.to_csv("../data_proc/deaths/agg_5_85.csv",sep=";")

########################################################

gruppen5_80p = pd.cut(
    alter,
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80, float("inf")],
    right=False,
    labels=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
            "45-49","50-54","55-59","60-64","64-69","70-74","75-79","80+"]
)

df_agg_5_80p = df.groupby(gruppen5_80p,observed=False).sum()

df_agg_5_80p.to_csv("../data_proc/deaths/agg_5_80.csv",sep=";")