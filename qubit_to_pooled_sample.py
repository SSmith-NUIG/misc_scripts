#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:05:42 2020

@author: stephen
"""
import pandas as pd
import numpy as np
import sys

#setting up test dataframe (only run this once)
#df = pd.DataFrame({"number":[1,2,3,4,5,6], "conc":[35,54,29,33,43,35], "volume":[35,35,40,40,33,30]})
#df.to_csv("colony_test.csv", index=False)
#df

def  how_much_to_take(dataframe):
    dataframe.rename(columns={"Original sample conc.":"conc"}, inplace=True)
    dataframe["volume"] = sys.argv[2]
    dataframe.volume = dataframe.volume.astype(float)
    dataframe["total_dna"] = dataframe.apply(lambda row: row.conc*row.volume, axis=1)    
    dataframe["ratio"] = dataframe["conc"].apply(lambda x: 1/x)
    dataframe["group"] = np.nan
    dataframe["take"] = np.nan

    current_group = 1
    for i in range(0, len(dataframe["Run ID"])):

        if i%3==0:
            for j in range(0, 3):           
                dataframe["group"][i+j] = current_group
            current_group +=1
    
    group_counter = 0
     
    for m in range(1, dataframe["group"].nunique()+1):
        for n in range(group_counter, len(dataframe["ratio"])):
            dataframe["take"][n] = dataframe["ratio"][n] * (35 / sum(dataframe.loc[dataframe['group'] == m]["ratio"]))
        group_counter += len(dataframe[dataframe["group"]==m])   
    print(dataframe[["conc","total_dna","ratio", "group","take"]])

df = pd.read_csv(sys.argv[1])


how_much_to_take(df)
