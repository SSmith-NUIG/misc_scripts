#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:05:42 2020

@author: stephen
"""
import pandas as pd
import argparse
import textwrap
import numpy as np
#import sys

parser = argparse.ArgumentParser(description='pool_dna_script')

parser.add_argument('-file', metavar='-f', nargs='+', default="",
                    help= textwrap.dedent('''\
                                          path to csv qubit file'''))

parser.add_argument('-volume', metavar='-v', nargs='+', default="35",
                    help= textwrap.dedent('''\
                                          Enter the volume (microL) of the sample, defualt is 35'''))

parser.add_argument('-poolsize', metavar='-s', nargs='+', default="6",
                    help= textwrap.dedent('''\
                                          Enter the number of samples you are pooling together, default is 6'''))


options = parser.parse_args()
#setting up test dataframe (only run this once)
#df = pd.DataFrame({"number":[1,2,3,4,5,6], "conc":[35,54,29,33,43,35], "volume":[35,35,40,40,33,30]})
#df.to_csv("colony_test.csv", index=False)
#df

def  how_much_to_take(dataframe):
    
    dataframe.rename(columns={"Original sample conc.":"conc"}, inplace=True)
    dataframe["volume"] = float(options.volume[0])
    #dataframe.volume = dataframe.volume.astype(float)
    dataframe["total_dna"] = dataframe.apply(lambda row: row.conc*row.volume, axis=1)    
    dataframe["inverse_conc"] = dataframe["conc"].apply(lambda x: 1/x)
    dataframe["group"] = np.nan
    dataframe["take"] = np.nan
    dataframe = dataframe.iloc[::-1]
    new_index = list(range(1,len(dataframe["volume"])+1))
    #dataframe.reset_index(inplace=True)
    
    current_group = 1
    

    
    pool_size = int(options.poolsize[0])
    vol = float(options.volume[0])
    
    for i in range(0, len(dataframe["Run ID"])):
        if i%pool_size==0:
            for j in range(0, pool_size):           
                dataframe["group"][i+j] = current_group
            current_group +=1
    
    group_counter = 0
     
    for m in range(1, dataframe["group"].nunique()+1):
        for n in range(group_counter, len(dataframe["inverse_conc"])):
            dataframe["take"][n] = dataframe["inverse_conc"][n] * (vol / sum(dataframe.loc[dataframe['group'] == m]["inverse_conc"]))
        group_counter += len(dataframe[dataframe["group"]==m])   
    
    dataframe = dataframe.reindex(new_index, axis=1)
    
    print(dataframe[["conc","total_dna","o", "group","take"]])


df = pd.read_csv(options.file[0])


how_much_to_take(df)
