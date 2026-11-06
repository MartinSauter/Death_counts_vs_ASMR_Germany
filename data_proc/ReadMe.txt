This directory contains processed data from directory ../data_orig

Death counts and numbers in directories ./deaths and ./pop  were aggregated 
by Python scripts in ../code in agegroups with 5year/10year and 20year agebands

The 5 year aggregation data comes in 2 variants with 80+ and 85+ as the open-ended age-group

./deaths
├── agg_10.csv
├── agg_20.csv
├── agg_5.csv
└── agg_5_80p.csv
./pop
├── agg_10.csv
├── agg_20.csv
├── agg_5.csv
└── agg_5_80p.csv


The ./cmr directory contains the data for crude mortality data (calculated by python scripts as well)
from ../data_proc/{deaths,pop}
The files agg*csv represent cmr data.

The files asmr*csv contain calculated age-standardised mortality rates for DE2020 standard population.


./cmr
├── agg_10.csv
├── agg_20.csv
├── agg_5.csv
├── agg_5_80p.csv
├── asmr_10.csv
├── asmr_5_80.csv
└── asmr_5_85.csv

If age bands are 5years, and "_80p" appears in the file name, the open ended age group contains all ages 
above 80. Otherwise, open ended group is 85+



