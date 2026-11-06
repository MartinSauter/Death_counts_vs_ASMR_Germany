This directory contains data about the standard population numbers used her.

.
├── deu20
│   ├── deu20_10.csv
│   ├── deu20_5.csv
│   └── deu20_5_80.csv
├── esp13
│   ├── esp13_10.csv
│   ├── esp13_5_80.csv
│   └── esp13_5_85.csv
├── std_pops_esp_who.py
├── std_pop_de2020.py
└── who15
    ├── who15_10.csv
    ├── who15_5_80.csv
    └── who15_5_85.csv
	
The python scripts generate the .csv files in the subdirectories.

Deu20 (representing DE2020) is calculated by std_pop_de2020.py 
from the pop. data in ../data_proc
using the various age bands and open-ended age groups.

std_pops_esp_who.py generates the csv files in {who15,esp13}. 
Necessary data is hardcoded in the .py scripts

