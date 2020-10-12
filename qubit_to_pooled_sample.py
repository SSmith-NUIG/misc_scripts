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
    #set up the dataframe columns. 
    #Rename a column.
    dataframe.rename(columns={"Original sample conc.":"conc"}, inplace=True)
    dataframe["volume"] = sys.argv[2]
    dataframe.volume = dataframe.volume.astype(float)
    
    #create a total_dna column, this is needed when sending samples for sequencing
    dataframe["total_dna"] = dataframe.apply(lambda row: row.conc*row.volume, axis=1)
    
   #get the inverse of the concentration, this is used later
    dataframe["one_over_conc"] = dataframe["conc"].apply(lambda x: 1/x)
    dataframe["group"] = np.nan
    dataframe["take"] = np.nan
    
    #set the current group to 1 then loop over your dataframe assigning groups based on how many
    #samples you want in each group, this will change depending on experiment set-up
    current_group = 1
    for i in range(0, len(dataframe["Run ID"])):
        if i%3==0:
            for j in range(0, 3):           
                dataframe["group"][i+j] = current_group
            current_group +=1
    
    #create a group counter variable. This is used to keep track of where we have left off in the dataframe.
    #e.g if there are 3 samples in group 1 then we will have left off at index 2 and we will start at index 3 next time
    group_counter = 0
    
    #get m, the "id" of the group
    for m in range(1, dataframe["group"].nunique()+1):
        #use n which is the start index (using group_counter) to the end of the dataframe to assign values to "take"
        for n in range(group_counter, len(dataframe["one_over_conc"])):
            dataframe["take"][n] = dataframe["ratio"][n] * (35 / sum(dataframe.loc[dataframe['group'] == m]["one_over_conc"]))
        
        #increase group_counter based on how many samples we have just looped over
        group_counter += len(dataframe[dataframe["group"]==m])   
    print(dataframe[["conc","total_dna","one_over_conc", "group","take"]])

df = pd.read_csv(sys.argv[1])


how_much_to_take(df)
