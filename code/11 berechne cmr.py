# -*- coding: utf-8 -*-
"""
Calculating cmr in age groups
"""

import pandas as pd
import numpy as np

####################################################


    
dn=pd.read_csv("../data_proc/deaths/agg_20.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_20.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_20.csv",sep=";")
###########################################################

  
dn=pd.read_csv("../data_proc/deaths/agg_10.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_10.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_10.csv",sep=";")
###########################################################

###########################################################

  
dn=pd.read_csv("../data_proc/deaths/agg_5_85.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_5_85.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_5_85.csv",sep=";")
###########################################################
  
dn=pd.read_csv("../data_proc/deaths/agg_5_80.csv",sep=";",
               index_col=0).astype(np.int64)

pop=pd.read_csv("../data_proc/pop/agg_5_80.csv",sep=";",
               index_col=0).astype(np.int64)
cmr=dn/pop

cmr.to_csv("../data_proc/cmr/agg_5_80.csv",sep=";")
###########################################################

