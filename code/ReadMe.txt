This directory contains the python scripts for aggregating, calculating and
visualising all relevant data (except standard pops)

Python scripts 01,02*:
Aggegrating death and population numbers into the relevant age bands.
Data is taken from ../data_orig and processed into ../data_proc

Script 11*
Calculating crude mortality from death and population counts.
Data is taken from ../data_proc/{deaths,pop} and processed into ../data_proc/cmr

Scripts 12{a,b,c}: 
Calculating ASMR for the relevant age bands (see file names). 
Data is taken from ../data_proc/cmr and ../std_pops and calculated into the same directory
The resulting files (e.g. ../data_proc/cmr/agg_5.csv) contains the crude mortality for the 
relevant age groups and calculates the weighted sum (ASMR) into the same directory.

Scripts Fig*

Calculating and visualisation. Each figure is saved into ../figures as raster (.png) and vector (.pdf)

Script Tab* 

Calculating and formatting of tables.

