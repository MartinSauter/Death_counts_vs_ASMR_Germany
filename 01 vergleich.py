# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:35:58 2026

@author: Martin Sauter
"""

import pandas as pd

file = "statistischer-bericht-rueckgerechnete-bevoelkerung-zensus-5124105219005.xlsx"

df = pd.read_excel(
    file,
    sheet_name="12411-03",
    header=[2, 3, 4],
    index_col=0, skipfooter=4
)

# # Excel-Merges nach rechts auffüllen
cols = df.columns.to_frame(index=False)


df.columns = pd.MultiIndex.from_frame(
    cols,
    names=["Jahr", "Bevölkerung", "Geschlecht"]
)

df.index.name = "Alter"

###################################
print(df.head())

###################################

df = df.drop(columns="2011 1", level="Jahr")

df=df.drop(columns=["männlich","weiblich"],level="Geschlecht")
df=df.drop(columns=["Deutsche Bevölkerung","Nichtdeutsche Bevölkerung"],level="Bevölkerung")

df=df.rename(columns={"2012 2":"2012"})

##########################################
# Nur noch Jahr übrig

df.columns = df.columns.get_level_values("Jahr")

df.columns = df.columns.astype(int)

df.to_csv("pop_back_calc.csv")



