# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:35:58 2026

@author: Martin Sauter
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

p_back=pd.read_csv("pop back calc/pop_back_calc.csv",index_col=0)

p_back.columns=p_back.columns.astype(int)

plt.plot(p_back.keys(),p_back.loc["Insgesamt",:].values,label="Back calc")
# #################################

p_2011=pd.read_csv("pop zensus 2011/12411-0005_$F.csv",sep=";",
                   encoding="ISO 8859-1",skiprows=6,index_col=0,
                   skipfooter=4,engine='python')

p_2011.columns=np.linspace(2005,2024,20).astype(int)

plt.plot(p_2011.keys(),p_2011.loc["Insgesamt",:].values,label="Census 2011")


# #################################



p_2022=pd.read_csv("pop zensus 2022/12411-0005_de.csv",sep=";",
                   encoding="ISO 8859-1",skiprows=6,index_col=0,
                   skipfooter=4,engine='python')

p_2022.columns=np.linspace(2012,2026,15).astype(int)

plt.plot(p_2022.keys(),p_2022.loc["Insgesamt",:].values,label="Census 2022")

plt.legend(loc="upper left")
