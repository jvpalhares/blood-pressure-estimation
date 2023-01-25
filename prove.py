import wfdb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

waves = '/Users/palhares/Documents/msc/blood-pressure-estimation/waves/physionet.org/files/mimic4wdb/0.1.0/waves/'

my_file = open(waves + "name_paths.txt")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()
aux = 0
for files in data_into_list:
    df = pd.read_csv(waves + files,
                     compression='gzip')

    print(files)
    print(df.columns)