# # -*- coding: utf-8 -*-
# """
# converting destatis excel
# to machine readable csv
# generating age table with 1year bands
# """

# import pandas as pd
# import numpy as np


# file = "statistischer-bericht-rueckgerechnete-bevoelkerung-zensus-5124105219005.xlsx"

# df = pd.read_excel(
#     file,
#     sheet_name="12411-03",
#     header=[2, 3, 4],
#     index_col=0, skipfooter=4
# )

# # # Excel-Merges nach rechts auffüllen
# cols = df.columns.to_frame(index=False)


# df.columns = pd.MultiIndex.from_frame(
#     cols,
#     names=["Jahr", "Bevölkerung", "Geschlecht"]
# )

# df.index.name = "Alter"

# ###################################
# print(df.head())

# ###################################

# df = df.drop(columns="2011 1", level="Jahr")

# df=df.drop(columns=["männlich","weiblich"],level="Geschlecht")
# df=df.drop(columns=["Deutsche Bevölkerung","Nichtdeutsche Bevölkerung"],level="Bevölkerung")

# df=df.rename(columns={"2012 2":"2012"})



# ##########################################
# # Nur noch Jahr übrig

# df.columns = df.columns.get_level_values("Jahr")

# df.columns = df.columns.astype(int)

# # "Stichtag" is always 31.12 -> so shift

# df.columns=df.columns+1



# # Generate and "Save" Total. pop
# pop_back_tot=df.loc["Insgesamt",:]
# pop_back_tot.to_csv("../../data_proc/pop_back/pop_back_tot.csv")

# #
# pop_back_age=df.drop(["Insgesamt"])


# # Generate and save age table with 1 year bands

# pop_back_age.index=np.linspace(0,100,101).astype(int)
# pop_back_age.to_csv("../../data_proc/pop_back/pop_back_age.csv")




