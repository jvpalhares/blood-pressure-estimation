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

    if 'ABPs [mmHg]' in df:
        aux += 1
        file_name = str(waves.split("/")[0] + files + str(aux)).replace('/', '_')
        sns.scatterplot(data=df, x="time", y='ABPs [mmHg]', alpha=0.1)
        plt.title(waves.split("/")[0] + files)
        plt.savefig('./waves_fig/' + file_name + '_fig.png')
        plt.clf()
        print(file_name)
        print(aux)

    else:
        pass
